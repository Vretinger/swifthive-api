# 🐝 SwiftHive Backend

The backend API for **SwiftHive**, a freelance job marketplace connecting talented freelancers with clients who need quality work done. Built with **Django** and **PostgreSQL**, this backend manages user roles, job postings, applications, and profiles through a secure and scalable RESTful API.

---

## 🧠 Project Overview

SwiftHive is designed to empower:

- **Clients** to post jobs and find the best freelancers.
- **Freelancers** to showcase their skills and apply for relevant jobs.

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

## 🚀 Getting Started

### 🔧 Installation

1. **Clone the repo:**

```bash
git clone https://github.com/Vretinger/swifthive-api.git
cd swift-hive-backend
```

2. **Create and activate a virtual environment:**

```bash
python -m venv env
source env/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Create `.env` file:**

```
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://...
CLOUDINARY_URL=cloudinary://...
```

5. **Apply migrations:**

```bash
python manage.py migrate
```

6. **Create superuser:**

```bash
python manage.py createsuperuser
```

7. **Run the server:**

```bash
python manage.py runserver
```

---

## 🌐 API Overview

> Base URL: `/api/`

| Endpoint | Method | Description |
|----------|--------|-------------|
|admin/
| `/auth/registration/` | POST | Register a new user |
| `/auth/ login/`  | POST | Login and get token |
| `/job-listings/` | GET | List all job postings |
| `/job-listings/create/` | POST | Create a new job (client only) |
| `/accounts/freelancers/` | GET | Get freelancer profiles |
| `/accounts/clients/` | GET | Get client profiles |

---

## ✅ Running Tests

```bash
py manage.py test
```

---

## ☁️ Deployment

### Deploy to Heroku

```bash
# Log in and create a new Heroku app
heroku login
heroku create swift-hive-backend

# Set environment variables
heroku config:set SECRET_KEY=...
heroku config:set DATABASE_URL=...
heroku config:set CLOUDINARY_URL=...

# Push code
git push heroku main

# Apply migrations on Heroku
heroku run python manage.py migrate
```

---

## 🔗 Related Repos

- 💻 [SwiftHive Frontend](https://github.com/Vretinger/swifthive)

---

