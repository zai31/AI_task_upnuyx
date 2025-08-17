from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    # Authentication
    path('register/', views.RegisterView.as_view(), name='register'),
    path('token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Chat
    path('chat/', views.ChatView.as_view(), name='chat'),
    
    # User
    path('user/balance/', views.TokenBalanceView.as_view(), name='token_balance'),
    path('user/profile/', views.UserProfileView.as_view(), name='user_profile'),
]
