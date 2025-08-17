# AI Chat System

A RESTful API for an AI-powered chat system built with Django and Django REST framework.

## Features

- User registration and authentication
- JWT-based authentication
- AI chat functionality with token deduction (100 tokens per request)
- Token balance checking
- Chat history tracking
- Admin interface for user and chat management

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- SQLite (included with Python)

## Setup and Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai_chat_system
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser_custom
   ```
   This will create a superuser with:
   - Username: admin
   - Password: admin123
   - Tokens: 10000

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## API Documentation

### Base URL
`http://localhost:8000/api/`

### Authentication
- `POST /register/` - Register a new user
  - Request body: `{"username": "string", "password": "string", "password2": "string"}`
  - Response: User data and tokens

- `POST /token/` - Obtain JWT token (login)
  - Request body: `{"username": "string", "password": "string"}`
  - Response: Access and refresh tokens

- `POST /token/refresh/` - Refresh JWT token
  - Request body: `{"refresh": "string"}`
  - Response: New access token

### Chat
- `POST /chat/` - Send a message to the AI (costs 100 tokens)
  - Headers: `Authorization: Bearer YOUR_ACCESS_TOKEN`
  - Request body: `{"message": "string"}`
  - Response: AI response and remaining tokens

- `GET /chat/` - Get chat history
  - Headers: `Authorization: Bearer YOUR_ACCESS_TOKEN`
  - Response: List of previous chats

### User
- `GET /user/balance/` - Get token balance
  - Headers: `Authorization: Bearer YOUR_ACCESS_TOKEN`
  - Response: `{"tokens": number}`

- `GET /user/profile/` - Get user profile
  - Headers: `Authorization: Bearer YOUR_ACCESS_TOKEN`
  - Response: User data

## Admin Interface

Access the admin interface at `http://localhost:8000/admin/` using your superuser credentials to:
- View and manage users
- View chat history
- Adjust user token balances
- Manage user permissions

## Example Usage with cURL

1. Register a new user:
   ```bash
   curl -X POST http://localhost:8000/api/register/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "testpass123", "password2": "testpass123"}'
   ```

2. Get JWT token:
   ```bash
   curl -X POST http://localhost:8000/api/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "testpass123"}'
   ```

3. Send a message to the AI (replace YOUR_ACCESS_TOKEN with the actual token):
   ```bash
   curl -X POST http://localhost:8000/api/chat/ \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello, AI!"}'
   ```

4. Check token balance:
   ```bash
   curl -X GET http://localhost:8000/api/user/balance/ \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
   ```

## Testing

To run tests:
```bash
python manage.py test
```

## Deployment

For production deployment, consider:
1. Setting `DEBUG = False` in settings.py
2. Configuring a production database (PostgreSQL recommended)
3. Setting up a proper web server (Nginx + Gunicorn)
4. Using environment variables for sensitive data
5. Setting up HTTPS

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
"# AI_task_upnuyx" 
