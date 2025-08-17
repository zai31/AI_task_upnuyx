from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from .models import Chat
from .serializers import (
    UserRegisterSerializer, 
    CustomTokenObtainPairSerializer, 
    ChatSerializer, 
    ChatRequestSerializer,
    TokenBalanceSerializer,
    UserSerializer
)
from core.settings import TOKEN_COST_PER_REQUEST

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegisterSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ChatView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = ChatRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = request.user
        message = serializer.validated_data['message']
        
        # Check if user has enough tokens
        if user.tokens < TOKEN_COST_PER_REQUEST:
            return Response(
                {"error": "Insufficient tokens"}, 
                status=status.HTTP_402_PAYMENT_REQUIRED
            )
        
        # Deduct tokens
        if not user.deduct_tokens(TOKEN_COST_PER_REQUEST):
            return Response(
                {"error": "Failed to deduct tokens"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        # Generate a simple AI response (in a real app, this would call an AI service)
        response_text = f"AI Response to: {message}"
        
        # Save the chat
        chat = Chat.objects.create(
            user=user,
            message=message,
            response=response_text
        )
        
        return Response({
            "message": message,
            "response": response_text,
            "tokens_remaining": user.tokens
        }, status=status.HTTP_200_OK)
    
    def get(self, request):
        # Get chat history for the authenticated user
        chats = Chat.objects.filter(user=request.user).order_by('-timestamp')
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)


class TokenBalanceView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request):
        serializer = TokenBalanceSerializer({"tokens": request.user.tokens})
        return Response(serializer.data)


class UserProfileView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user
