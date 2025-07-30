
# 🛒 E-Commerce Backend Documentation

This backend is a comprehensive and modular e-commerce system built using **Django** and **Django REST Framework**. It provides all essential functionalities required for a modern e-commerce application, including user management, product catalog, shopping cart, order processing, and admin operations. The backend is API-driven, making it easy to integrate with various frontend platforms or third-party services.

---

## 🌐 Live Demo

🔗 [View E-Commerce Backend](https://django-id12.onrender.com/) – Hosted on Render.

Use the demo to explore API behavior and how different components interact in real-time.

---

## 🧱 Project Structure

The project is organized into multiple Django apps, each responsible for a specific domain to ensure clean architecture and maintainability:

- **`core`** – Handles authentication using JWT tokens (login, token refresh, registration)
- **`likes`** – Manages user profiles and user interactions (e.g., liked products)
- **`store`** – The heart of the platform; manages products, collections, carts, and orders
- **`tags`** – Enables flexible product categorization using tags

Each app follows Django's standard practices for models, views, serializers, and permissions.

---

# 🔑 Admin Access

Use the following credentials to log in as an administrator:
| Endpoint | Description |
|----------|----------|
| `/admin` | access to admin panel |


| Username | Password |
|----------|----------|
| `Admin`  | `1234`   |

---

# 📘 API Reference

Below is the categorized API documentation for each domain.

## 🔐 Authentication (JWT-Based)

These endpoints handle user authentication and token management:

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/auth/jwt/create` | Create JWT access and refresh tokens |
| `POST` | `/auth/jwt/refresh` | Generate a new access token using a refresh token |
| `GET`  | `/auth/users` | Retrieve all users (Admin only) |

> ⚠️ All protected endpoints require a valid JWT token in the `Authorization` header:  
> `Authorization: Bearer <your_token>`

---

## 👥 Customer Management

### 📋 Get All Customers
```http
GET /store/customers
```

### 👤 Get Current Authenticated Customer
```http
GET /store/customers/me
```

### 🔎 Customer Details (Admin Only)
```http
GET    /store/customers/<int:id>
PUT    /store/customers/<int:id>
DELETE /store/customers/<int:id>
```

### 🕘 Customer Purchase History
```http
GET    /store/customers/<int:id>/history
PUT    /store/customers/<int:id>/history
DELETE /store/customers/<int:id>/history
```

These endpoints provide complete access to user information and their transaction history for both users and admins.

---

## 🗂️ Collections API

Collections are groupings of products for easier navigation and management.

### 🔄 All Collections
```http
GET  /store/collections
POST /store/collections   # Admin Only
```

### 📁 Single Collection by ID
```http
GET     /store/collections/<int:id>
POST    /store/collections/<int:id>   # Admin Only
PUT     /store/collections/<int:id>   # Admin Only
DELETE  /store/collections/<int:id>   # Admin Only
```

Admins can fully manage product collections, which users can browse publicly.

---

## 🛍️ Product Management

The core of the platform: adding, editing, and browsing products.

### 🔎 All Products
```http
GET  /store/products
POST /store/products   # Admin Only
```

### 🛒 Product Details
```http
GET     /api/items/<int:id>
POST    /api/items/<int:id>
PUT     /api/items/<int:id>
PATCH   /api/items/<int:id>
DELETE  /api/items/<int:id>
```

### 🖼️ Manage Product Images (Admin Only)
```http
GET     /store/products/<int:id>/images
PUT     /store/products/<int:id>/images
DELETE  /store/products/<int:id>/images
```

Products are fully manageable with image upload support and RESTful operations.

---

## 🧺 Shopping Cart

Provides endpoints to manage user carts and simulate real-time e-commerce experiences.

### 🛒 All Carts
```http
GET  /store/carts               # Admin or Authorized users only
POST /store/carts
```

### 🧾 Single Cart
```http
GET     /store/carts/<int:id>
PATCH   /store/carts/<int:id>
PUT     /store/carts/<int:id>
DELETE  /store/carts/<int:id>
```

> Carts are automatically created for users and updated as they shop.

---

## 📦 Order Management

Manages customer orders and purchase records.

### 📄 All Orders
```http
GET /store/orders   # Admin or Authorized users only
```

### 🧾 Order Detail by ID
```http
GET /store/orders/<int:id>
```

Order data is secured and only accessible to admins or the user who placed the order.

---

# 📌 Notes

- Ensure all requests to protected endpoints contain a valid JWT token.
- For API testing, use tools like [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/).
- All responses are in JSON format and follow REST standards.

---

# 🚀 Deployment & Hosting

- Hosted on: [Render](https://render.com/)
- Stack: Django, Django REST Framework, PostgreSQL


---

Made with Django and DRF
---
