# 🛒 E-Commerce Backend API (Django)

A secure and modular eCommerce backend built with Django and Django REST Framework.  
Includes a custom admin panel, JWT authentication, and RESTful APIs for managing users, products, orders, promotions, and more.

---

## 🚀 Live Demo

[![Live Site](https://img.shields.io/badge/Visit%20Live%20App-Render-blue?style=for-the-badge)](https://django-id12.onrender.com)

---

## 📚 Table of Contents

- [✅ Features](#-features)
- [🔐 Authentication](#-authentication)
- [👥 Customers](#-customers)
- [🛍️ Products](#-products)
- [🛒 Cart](#-cart)
- [📦 Orders](#-orders)
- [🛠️ Admin Panel](#-admin-panel-credentials)
- [🔒 Security](#-security-highlights)
- [📦 Tech Stack](#-tech-stack)

---

## ✅ Features

### 🔸 Core Functionality
- User Registration & Login with JWT Authentication
- Role-Based Access Control (RBAC) using Django Groups & Permissions
- Secure API Endpoints with token protection and custom permissions

### 🛍️ E-Commerce Modules
- Product Management (CRUD + images, collections, tags, promotions)
- Order Management (Create, track, update, cancel)
- Collection & Tag Support
- Promotion System

### 🔐 Authentication & Security
- JWT Access & Refresh Tokens
- Admin-only endpoints protected via role-based permissions
- Secured data access by user identity

### 🛠️ Admin Panel
- Custom Django Admin Dashboard
- Manage:
  - Users
  - Products & Product Images
  - Orders
  - Tags, Collections, Promotions

### 🌐 REST API Endpoints
- `/auth/` - Auth operations (JWT)
- `/store/products/` - Product catalog
- `/store/customers/` - Customer details
- `/store/orders/` - Orders & status
- `/store/carts/` - Shopping cart logic
- `/store/promotions/`, `/tags/`, etc.

---

## 🔐 Authentication

### 🔸 Admin Panel Credentials

```http
USERNAME: admin
PASSWORD: 1234
```

### 🔸 Auth Endpoints

| Method | Endpoint                | Description              |
|--------|-------------------------|--------------------------|
| POST   | `/auth/jwt/create/`     | Create access/refresh tokens |
| POST   | `/auth/jwt/refresh/`    | Regenerate access token |
| GET    | `/auth/users/`          | Get all users (Admin only) |

---

## 👥 Customers

### Get All Customers
```http
GET /store/customers/
```

### Get / Update / Delete Customer
```http
GET     /store/customers/<int:id>/
PUT     /store/customers/<int:id>/
DELETE  /store/customers/<int:id>/
```

### View Customer History
```http
GET /store/customers/<int:id>/history/
```

| Header        | Value         |
|---------------|---------------|
| Authorization | Bearer JWT_TOKEN |

---

## 🛍️ Products

### Get All Products
```http
GET /store/products/
```

### Get / Update / Delete Product
```http
GET     /store/products/<int:id>/
PUT     /store/products/<int:id>/
DELETE  /store/products/<int:id>/
```

### Create Product (Admin)
```http
POST /store/products/
```

### Product Images
```http
GET     /store/products/<int:id>/images/
POST    /store/products/<int:id>/images/
PUT     /store/products/<int:id>/images/<int:image_id>/
DELETE  /store/products/<int:id>/images/<int:image_id>/
```

---

## 🛒 Cart

### Create Cart
```http
POST /store/carts/
```

### Modify Cart
```http
PUT     /store/carts/<int:id>/
DELETE  /store/carts/<int:id>/
```

### Cart Items
```http
GET     /store/carts/<int:id>/items/
POST    /store/carts/<int:id>/items/
```

### Modify Cart Item
```http
GET     /store/carts/<int:id>/items/<int:item_id>/
PUT     /store/carts/<int:id>/items/<int:item_id>/
DELETE  /store/carts/<int:id>/items/<int:item_id>/
```

---


---

## 🗂️ Collections

### Get All Collections
```http
GET /store/collections/
```

### Get, Update, or Delete a Collection
```http
GET     /store/collections/<int:pk>/
PUT     /store/collections/<int:pk>/
DELETE  /store/collections/<int:pk>/
```

### Create a New Collection (Admin)
```http
POST /store/collections/
```


## 📦 Orders

### Get All Orders (Admin only)
```http
GET /store/orders/
```

### Order Details
```http
GET     /store/orders/<int:id>/
PUT     /store/orders/<int:id>/
DELETE  /store/orders/<int:id>/
```

| Header        | Value         |
|---------------|---------------|
| Authorization | Bearer JWT_TOKEN |

---

## 🔒 Security Highlights

- JWT-secured endpoints using `djangorestframework-simplejwt`
- Role-based permission model (Admins vs Authenticated Users)
- Custom permissions for resource ownership
- Admin panel access restricted

---

## 📦 Tech Stack

- Django
- Django REST Framework
- djangorestframework-simplejwt (JWT)
- PostgreSQL / SQLite
- Docker (optional for deployment)
- Render for hosting

---

> Built with Django & DRF.
