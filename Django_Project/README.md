# Django REST + Celery + Telegram Bot Project

## Features

- Django + Django REST Framework
- User Registration API with JWT Authentication
- Public & Protected API Endpoints
- Celery Background Task (Sends Email After Registration)
- Telegram Bot Integration (/start saves username to DB)

---

## API Endpoints

| Endpoint               | Method | Access        | Description                            |
|------------------------|--------|---------------|----------------------------------------|
| `/api/public/`         | GET    | Public        | Sample public API                      |
| `/api/protected/`      | GET    | Auth Required | JWT token required                     |
| `/auth/register/`      | POST   | Public        | Register new user + trigger Celery     |
| `/auth/token/`         | POST   | Public        | Get JWT token (login)                  |

---

## Setup Instructions

### 1. Clone the repo & create virtualenv

```bash
git clone https://github.com/Sumathisree-A/django-project
cd Django_Project
python -m venv venv
venv\Scripts\activate   # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file in the root folder

```env
DEBUG=False
SECRET_KEY=your-secret-key
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Run Redis (in a separate terminal)

```bash
redis-server
```

### 6. Run Celery Worker

```bash
celery -A django_assignment worker --loglevel=info
```

### 7. Run Django Server

```bash
python manage.py runserver
```

### 8. Run Telegram Bot

```bash
python manage.py run_telegram_bot
```