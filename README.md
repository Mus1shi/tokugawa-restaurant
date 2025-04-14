# tokugawa-restaurant
Fullstack gastronomic restaurant platform – Django REST API + React/TypeScript/MUI


# Tokugawa – High-End Japanese Restaurant Web App

**Tokugawa** is a fullstack web application built with **Django (Python)** on the backend and **React + TypeScript** on the frontend. It simulates an elegant, 
high-end Japanese restaurant featuring **online reservations, menu & chef management, client reviews**, and a sleek, responsive design inspired by Japanese aesthetics.

> 💡 This project showcases my fullstack skills, code structure practices, API design, and attention to user experience.

---

## 🌐 Live Demo
 Coming soon on Vercel + Railway  
---

##  Key Features

###  Backend (Django + Django REST Framework)
- API endpoints for Menu, Chefs, Reservations, Comments
- CSRF protection, form validation, and JWT authentication (in progress)
- Modular models: `Menu`, `Chef`, `Category`, `Reservation`, `Comment`
- Admin dashboard customization
- Internationalization ready (EN/FR/JP planned)

###  Frontend (React + TypeScript + Tailwind CSS)
- Fully responsive, premium design
- Interactive & secure reservation form
- Modular components (Cards, Buttons, Navbar, etc.)
- Integrated with Django templates (Phase 1)
- Phase 2: Standalone SPA with React Router
- PWA-ready architecture

---

##  Tech Stack

| Backend         | Frontend                | Tooling / DevOps         |
|------------------|--------------------------|----------------------------|
| Django 5.1       | React 18                 | Git + GitHub              |
| Django REST API  | TypeScript               | WebStorm (JetBrains)      |
| SQLite (dev)     | Tailwind CSS             | Vercel / Railway          |
| Python 3.12      | React Router DOM         | `.env`, Hot Reload        |

---

##  Project Structure

tokugawa-restaurant/ │ ├── backend/ # Django backend app (API & logic) │ 
└── restaurant/ # Models, views, serializers, forms ├── frontend/ # Django HTML templates (Phase 1) ├── tokugawa-app/ # React frontend (SPA - 
Phase 2) ├── static/ # Images, videos, global styles ├── templates/ # Django HTML templates ├── db.sqlite3 # Local dev database └── README.md


---

## Local Setup

### Backend

```bash
git clone https://github.com/<your-username>/tokugawa-restaurant.git
cd tokugawa-restaurant/backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
