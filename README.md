# 🐝 SwiftHive Backend

The backend API for **SwiftHive**, a freelance job marketplace connecting talented freelancers with clients who need quality work done. Built with **Django** and **PostgreSQL**, this backend manages user roles, job postings, applications, and profiles through a secure and scalable RESTful API.

---

## 🧠 Project Overview

### 🚀 Project Purpose
Swifthive is a full-stack platform designed to connect freelancers with clients. Users can register as freelancers or job posters and publish or apply for job listings.

### 🎯 Goals
- **Allow users to register as freelancers or clients.**
- **Enable clients to post jobs with categories, deadlines, and budgets.**
- **Let freelancers apply for jobs and track their applications.**
- **Implement a messaging system between freelancers and clients.**
- **Ensure real-time interactivity and a responsive UI.**
- **Support admin moderation tools to manage users and posts.**

### 🎯 Core Features

| Role | Feature |
|------|---------|
| 👤 **Client** | Post new jobs |
| 👤 **Client** | View applicants per job |
| 👤 **Client** | Select the best candidate |
| 🧑‍💻 **Freelancer** | Create a profile with skills and experience |
| 🧑‍💻 **Freelancer** | Browse and apply to jobs with a custom message |

---

## 🛠️ Tech Stack

- **Backend Framework**: Django
- **Database**: PostgreSQL
- **Authentication**: Django auth with custom user model
- **File Uploads**: Cloudinary (for profile images, resumes, etc.)
- **API**: Django REST Framework
- **Hosting**: Heroku
- **Testing**: Django TestCase

---

## 📁 Project Structure

```
swifthive-api/
├── apps/
│   ├── accounts/           # Custom user model and authentication
│   ├── applications/            # job application logic
│   ├── contact/        # contact mail logic
│   └── job_listings/        # Job posting logic
├── swift_hive/          # Project config
├── requirements.txt
├── manage.py
└── .env                 # Environment variables (not committed)
```

---

## 📦 Deployment Instructions (Back-End)

### 🔧 Installation
#### Prerequisites
- **Python 3.10+**
- **PostgreSQL (or SQLite for local testing)**
- **Django 4+**
- **Cloudinary (for media if used)**
- **Heroku/Render/Fly.io account**

### Local Setup

```bash
git clone https://github.com/vretinger/swifthive.git
cd swifthive/backend
```

Create a `.env` file:

```env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
ALLOWED_HOSTS=localhost,127.0.0.1
CLOUDINARY_URL=cloudinary://...
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

Start the server:

```bash
python manage.py runserver
```
### Deployment (Heroku/Render)

Follow your platform's deployment guide, including:

- Add environment variables (SECRET\_KEY, DEBUG, DATABASE\_URL, ALLOWED\_HOSTS)
- Set up PostgreSQL database
- Run migrations and collectstatic

---
### 🚀 Deployment Breakdown (Back-End API)

#### Using Heroku (Command Line)

1. **Install Heroku CLI**\
   👉 [https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)

2. **Login via Terminal**

```bash
heroku login
```

3. **Create a New Heroku App**

```bash
heroku create swifthive-backend
```

4. **Push Code to Heroku**

```bash
git push heroku main
```

5. **Set Environment Variables**

```bash
heroku config:set SECRET_KEY='your-django-secret'
heroku config:set DEBUG='False'
heroku config:set ALLOWED_HOSTS='swifthive-backend.herokuapp.com'
heroku config:set DATABASE_URL='your-database-url'
heroku config:set CLOUDINARY_URL='cloudinary://user:pass@cloudname'
```

> 🔐 **Security Tip:** Store sensitive variables locally in `.env` and use [django-environ](https://pypi.org/project/django-environ/) to load them.

6. **Apply Migrations**

```bash
heroku run python manage.py migrate
```

7. **Create Superuser (Optional)**

```bash
heroku run python manage.py createsuperuser
```

8. **Collect Static Files**

```bash
heroku run python manage.py collectstatic --noinput
```

---

## 🧪 Manual Testing (Back-End)

Test your API manually using Postman or curl:

### Register New User

```http
POST /auth/registration/
{
  "email": "test@example.com",
  "password": "password123",
  "role": "freelancer"
}
```

### Login User

```http
POST /auth/login/
{
  "email": "test@example.com",
  "password": "password123"
}
```

### Create Job

```http
POST /job-listings/create/
Authorization: Bearer <token>
{
  "title": "Design Logo",
  "description": "Need a professional logo for my site",
  "budget": 500
}
```

---

## 📡 API Endpoint Reference

| Endpoint                 | Method | Auth Required | Description               | Sample Response |
| ------------------------ | ------ | ------------- | ------------------------- | --------------- |
| `/admin/`                | GET    | ✅             | Admin panel               | -               |
| `/auth/registration/`    | POST   | ❌             | Register a new user       | 201 Created     |
| `/auth/login/`           | POST   | ❌             | Login and get token       | 200 OK          |
| `/job-listings/`         | GET    | ❌             | List all job postings     | 200 OK          |
| `/job-listings/create/`  | POST   | ✅             | Create a new job (client) | 201 Created     |
| `/accounts/freelancers/` | GET    | ✅             | Get freelancer profiles   | 201 Created     |
| `/accounts/clients/`     | GET    | ✅             | Get client profiles       | 200 OK          |

---

## 🔗 Related Repos

- 💻 [SwiftHive Frontend](https://github.com/Vretinger/swifthive)

---
## ✍️ Author

**Hampus Vretinger** – [GitHub](https://github.com/vretinger)
