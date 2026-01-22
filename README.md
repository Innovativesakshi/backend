# HRMS Lite - Backend

## 📌 Overview
The **HRMS Lite Backend** is a robust and scalable REST API built with **FastAPI** and **MongoDB**. It serves as the core logic layer for the HRMS Lite system, handling employee management, attendance tracking, and authentication.

## 🚀 Tech Stack
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/) - High-performance web framework for building APIs.
- **Database:** [MongoDB](https://www.mongodb.com/) (Async with [Motor](https://motor.readthedocs.io/)).
- **Validation:** [Pydantic](https://docs.pydantic.dev/).
- **Server:** [Uvicorn](https://www.uvicorn.org/) - ASGI web server implementation.

## ⚙️ Prerequisites
Before you begin, ensure you have met the following requirements:
- **Python 3.8+** installed.
- **MongoDB** installed and running locally (or a cloud instance URI).

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Innovativesakshi/backend.git
cd backend
```

### 2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configuration
Create a `.env` file in the root directory by copying the example file:
```bash
cp .env.example .env
```
Open `.env` and configure your MongoDB connection string and other secrets.

## ▶️ Running the Application

Start the development server with auto-reload enabled:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

## 📚 API Documentation
FastAPI provides automatic interactive API documentation:
- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)
