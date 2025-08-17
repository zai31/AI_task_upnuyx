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
documentation url---> https://www.postman.com/tools6-2392/workspace/ai-task/documentation/40425168-e9f631bb-dd04-49cf-87cc-0c5c6c20be83

Access the admin interface at `http://localhost:8000/admin/` using your superuser credentials to:
- View and manage users
- View chat history
- Adjust user token balances
- Manage user permissions

