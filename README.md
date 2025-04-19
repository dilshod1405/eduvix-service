# 🛠️ Edvent Service — Backend for Edvent Online Learning Platform

This repository contains the backend services for the [Edvent](https://github.com/dilshod1405/edvent) online learning platform.  
The platform offers professional courses in **Architecture, Civil Engineering, IT, and Finance**.

---

## 🚀 Features

- 🔒 User Authentication
- 🎓 Course Management
- 💳 Payment Integration
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
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://user:password@db:5432/edvent_db
```

3. **Build and run using Docker:**

```bash
docker-compose up --build
```

4. **Run migrations & create a superuser:**

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

5. **Access your app locally:**

- API Base URL: `http://localhost:8000/api/`
- Admin Panel: `http://localhost:8000/admin/`

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
http://localhost:8000/api/docs/
```

---

## 💡 Deployment

- Make sure you’ve properly configured `nginx/` and `certbot/` for production.
- Use Docker Compose on your production server as well:

```bash
docker-compose -f docker-compose.prod.yml up -d --build
```

---

## 🤝 Contributing

Contributions are welcome!  
Fork the repo, create a feature branch, push your changes and submit a Pull Request.

---

## 📬 Contact

- 📧 Email: [dilshod.normurodov1392@gmail.com](mailto:dilshod.normurodov1392@gmail.com)
- 💬 Telegram: [@dilshod1405](https://t.me/dilshod1405)

---

## 📄 License

MIT License — feel free to use, distribute, and modify.

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

✅ Now your frontend and backend both are documented clearly! Let me know if you want me to also prepare a `docker-compose.yml` explanation or deployment guide!

