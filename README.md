# 🛠️ Edvent Service — Backend for Edvent Online Learning Platform

This repository contains the backend services for the [Edvent](https://github.com/dilshod1405/edvent) online learning platform.  
The platform offers professional courses in **Architecture, Civil Engineering, IT, and Finance**.

---

## 🚀 Features

- 🔒 User Authentication
- 🎓 Course Management
- 💳 National Payme Payment Provider Integration
- ✉️ Google Email notification Integration
- 🌐 RESTful API Endpoints
- 🐳 Dockerized for easy deployment

---

## 🧰 Tech Stack

- Python
- Django & Django REST Framework
- Docker & Docker Compose
- PostgreSQL
- Nginx
- Certbot (for SSL)

---

## 📁 Project Structure

```
edvent-service/
├── authentication/       # Handles user authentication logic
├── content/              # Manages course content and data
├── payment/              # Payment service logic
├── eduvix/               # Django core project settings
├── nginx/                # Nginx configurations for deployment
├── certbot/              # SSL certificate handling
├── Dockerfile            # Docker image setup
├── docker-compose.yml    # Docker services setup
├── manage.py             # Django management utility
└── requirements.txt      # Python packages list
```

---

## ⚙️ Installation & Setup

1. **Clone this repository:**

```bash
git clone https://github.com/dilshod1405/edvent-service.git
cd edvent-service
```

2. **Create a `.env` file** in the project root:

```bash
SECRET_KEY=your_secret_key
DB_NAME=database_name
DB_USER=database_user
DB_PASSWORD=database_password
DB_HOST=database_host
DB_PORT=database_host
DEBUG=False
ALLOWED_HOSTS=your allowed hosts
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=youremail@gmail.com
EMAIL_HOST_PASSWORD=Google SMTP password
CORS_ALLOWED_ORIGINS=http://localhost:3000
CSRF_TRUSTED_ORIGINS=http://localhost:3000
CORS_ALLOW_CREDENTIALS=True
SERVER_NAME=http://localhost:8000
SUCCESSFUL_CODE_URL=redirect url after email confirmation
PAYME_ID=payme_id
PAYME_KEY=payme_key
```

3. **Build and run using Docker:**

```bash
docker-compose up --build
```

4. **Access your app locally:**

- API Base URL: `http://localhost:8000/authentication/` for users entrypoints
- Admin Panel: `http://localhost:8000/admin/` for admin panel. You can change this url in production deployment

---

## 🧪 Running Tests

To run tests inside the Docker container:

```bash
docker-compose exec web python manage.py test
```

---

## 📝 API Documentation

If enabled, your Swagger / DRF-generated API docs will be available at:

```
http://localhost:8000/docs/ for swagger API documentation
http://localhost:8000/redoc/ for redoc API documentation
```

---

## 💡 Deployment

- Make sure you’ve properly configured `nginx/` and `certbot/` for production.
- Use Docker Compose on your production server as well:

```bash
docker-compose docker-compose up -d --build
```

## 📬 Contact

- 📧 Email: [dilshod.normurodov1392@gmail.com](mailto:dilshod.normurodov1392@gmail.com)
- 💬 Telegram: [@dilshod1405](https://t.me/dilshod1405)

---

# 💻 Edvent — Frontend

This repository contains the frontend for Edvent, built with **Next.js, TailwindCSS, Axios, and Auth.js (Google OAuth2)**.

Repository link: [https://github.com/dilshod1405/edvent](https://github.com/dilshod1405/edvent)

---

## 🌟 Key Features

- 🚀 Next.js + TailwindCSS for fast and responsive UI
- 🔑 Google Authentication via Auth.js
- 🔥 Axios-based API integration with `edvent-service`

---

## 💡 Screenshots

### 📚 Course Page

![Course Page](https://media-hosting.imagekit.io/fafd0e3cc4334e06/edventcourses.png?Expires=1839665535&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=GK2i65sqfceoTvENwTZoBOH5t2c-uHEhSHVfenmSldlBEhiNqYPSt08xfKroMgxZzzNPiPke~eIco27scDHcU-wzM3y6JiyFfW0d8hWWVEVxzxlRYqcQGbgUS0wa-bUcwuh0hJ7-aRBGNTbbOY3H4zL35RfvsvxDKkNdPaQagkqbk7vu7ygrVxJPYIsPjTcSsXjUdxZUAVJiM~ZnL~ao7aKMzRIu5FKMTHjYdZFMzxUEQ2YaES23diUISgFbj872k4sEPhQAoXjcwrHmdYuGSmyzaPH1A9kNhjL7lPkQYl-oWa01PLQyoVjknNE0YVbKiQmQuCVmbbqubB6KCFV-Vg__)

### 🔑 Google Login

![Google Login](https://media-hosting.imagekit.io/fb15f6382fc3479b/Google.png?Expires=1839665644&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=hG2WUg62Vp9VY6KBv84bBaLFJ5oqcgmP3HNvFx0E~0G5F5IdapUpp5HqXzfv-gVdtsgNjDph0hjxYxcAqDalLVBOf2i0r3SGyNSdR7ZnTNFqCMI4Ti6NQExOBuX9nvrbpSKTfvI5ivlSmMLvRZc8xk2aP3WQ8iILPqhhRwSkGsnrpSKq4abA~UKEF5LCFqndC9jBrs8ute-Mihc7ao5EQb26QSsrQcX0j1mc6dvm4f4w14C6X16rXUsKC7Ek2RIUAvSpnBsAxqb09tPRSK9ju-6TCBkA19J1~T94p6jORAE0uqwkburxf7mWjLsC0IeuIC3qb0R-l-5cNJIlbdJtWg__)

---