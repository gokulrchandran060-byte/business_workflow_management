# Business Workflow Management System

A Django REST Framework backend application that implements
a controlled business workflow using Django ORM.

This project focuses on enforcing workflow rules and validations
instead of simple CRUD operations.

---

## 🔧 Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Django ORM
- Git

---

## 🧠 Core Concept

Tasks move through a predefined workflow:

CREATED → IN_PROGRESS → DONE

Invalid transitions are blocked at the business logic layer.

---

## ✨ Key Features

- RESTful APIs using Django REST Framework
- Workflow state transitions with validation
- Service layer for business logic
- ORM-based filtering, validation, and updates
- Status-based querying using Django ORM
- Structured logging for workflow actions
- Clean separation of concerns

---

## 🏗️ Architecture Overview

Client  
→ Versioned API URLs (`/api/v1/`)  
→ DRF API Layer (Views & Serializers)  
→ Service Layer (Workflow Rules)  
→ Django ORM  
→ PostgreSQL Database  

---

## 🧩 ORM Usage Highlights

This project makes explicit use of Django ORM features:

- `all()` – list workflow items
- `filter()` – status-based querying
- `exists()` – efficient validation
- `update()` – state updates without full object reload
- `order_by()` – latest-first ordering

---

## 📡 API Endpoints (v1)

| Method | Endpoint | Description |
|------|--------|-------------|
| GET | `/api/v1/tasks/` | List tasks (supports status filter) |
| POST | `/api/v1/tasks/` | Create new task |
| GET | `/api/v1/tasks/<id>/` | Retrieve task |
| DELETE | `/api/v1/tasks/<id>/` | Delete task safely |
| PATCH | `/api/v1/tasks/<id>/status/` | Update task status |

---

## ⚠️ Workflow Rules

- CREATED → IN_PROGRESS ✅
- IN_PROGRESS → DONE ✅
- CREATED → DONE ❌
- DONE → any ❌

Invalid transitions return a clear error response.

---

## 📊 Logging & Error Handling

- INFO logs for successful workflow actions
- WARNING logs for invalid transitions
- Clean HTTP error responses for clients

---

## 🚀 Project Focus

This project focuses on backend fundamentals, ORM usage,
and business workflow enforcement.

Infrastructure-level scaling concepts are understood
but not implemented.

---

## 👤 Author

Gokul R Chandran  
Backend Developer (Django / DRF)
