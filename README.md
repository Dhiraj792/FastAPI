# FastAPI Learning Journey 🚀

This repository documents my journey of learning **FastAPI**, a modern, fast (high-performance) web framework for building APIs with Python.

---

# What is FastAPI?

**FastAPI** is a Python framework used to build APIs quickly and efficiently.

### Key Features:

* ⚡ High performance (comparable to Node.js & Go)
* 🧠 Automatic validation using Python type hints
* 📄 Auto-generated API documentation (Swagger UI)
* 🔒 Built-in support for data validation
* 🚀 Easy to learn and use

---

# Why I Started Learning FastAPI

* To build **backend APIs**
* To connect **Machine Learning models with web applications**
* To create **real-world projects**
* To improve my **development skills for placements**

---

# What I Learned So Far

* Installing FastAPI
* Creating a basic API
* Running a FastAPI server
* Understanding routes (GET, POST)

---

# Installation

```bash
pip install fastapi uvicorn
```

---

# First FastAPI App

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}
```

---

# Running the Server

```bash
uvicorn main:app --reload
```

* Open browser: http://127.0.0.1:8000
* Swagger Docs: http://127.0.0.1:8000/docs

---

# Project Structure (Basic)

```
project/
│── main.py
│── README.md
```

---

# Learning Goals

* Build REST APIs
* Connect FastAPI with databases
* Deploy APIs
* Integrate with Machine Learning models
* Create real-world backend projects

---

# Future Topics

* Path & Query Parameters
* Request Body (POST)
* Pydantic Models
* Database Integration (SQLAlchemy)
* Authentication (JWT)
* Deployment (Render / AWS)

---

# Learning Outcome

After starting FastAPI, I aim to:

* Build scalable APIs
* Deploy backend applications
* Integrate ML models into APIs
* Work on real-world projects

---

⭐ This repository will be updated as I continue learning FastAPI step by step.
