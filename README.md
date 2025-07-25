
# E-Commerce Application Backend

# Features

### Core Functionality

-- User Registration & Login with JWT Authentication

-- Role-Based Access Control using Django Groups & Permissions

-- Secure API Endpoints with custom permissions and token protection

### E-commerce Modules

-- Product Management (CRUD for products, linked to collections, tags, promotions)

-- Order Management (create, view, update, cancel orders)

-- Collection Support (product groupings)

-- Tag System (categorize products with tags)

-- Promotion System (attach discounts/promotions to products or collections)

### Authentication & Security
-- JWT-based Access & Refresh Tokens

-- Role-based permissions (Admin vs Regular User)

-- Secured endpoints (only authorized users can access protected routes)

### Admin Panel
-- Custom Admin Interface for:

-- Managing Users, Products, Orders

-- Managing Tags, Collections, Promotions

-- Simplified and styled admin dashboard

### API Endpoints
RESTful APIs for:

-- Users

-- Products

-- Orders

-- Promotions

-- Tags

-- Collections


## 🚀[Click here to checkout the live Application](https://django-id12.onrender.com)

# API Reference

### Admin Panel Credential

```http
  USERNAME : admin
  PASSWORD : 1234
```

## Auth 
#### Create Token

```http
  POST /auth/jwt/create
```
#### Regenerate Token
```http
  POST /auth/jwt/refresh
```
#### Get all users
```http
  POST /auth/users
```

## Customers
#### Get all Customers

```http
  GET /store/customers/
```
#### Customer Detail

```http
  GET       /store/customers/<int:id>
  PUT       /store/customers/<int:id>
  DELETE    /store/customers/<int:id>
  GET       /store/customers/<int:id>/history
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `string` | **Required**. Id of item to fetch |

| Header | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `JWT Token` | `string` | **Required**. Authentication |



## Product
#### Get all Products

```http
  GET /store/products/
```

#### Get a Product
```http
  GET /store/products/<int:id>
```
#### Post/Put/Delete a Product
```http
  GET       /store/products/<int:id>
  POST      /store/products/<int:id>
  PUT       /store/products/<int:id>
  DELETE    /store/products/<int:id>
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `string` | **Required**. Id of item to fetch |

| Header | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `JWT Token` | `string` | **Required**. Authentication |


#### Get Product images

```http
  GET /store/products/<int:id>/images
```
#### Post/Put/Delete Product images

```http
  GET       /store/products/<int:id>/images/<int:id>
  POST      /store/products/<int:id>/images/<int:id>
  PUT       /store/products/<int:id>/images/<int:id>
  DELETE    /store/products/<int:id>/images/<int:id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |



## Cart
#### Create Cart

```http
  POST      /store/carts
```
#### Modify Cart

```http
  PUT         /store/carts/<int:id>
  DELETE      /store/carts/<int:id>

```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of cart to fetch |

#### Cart Items
```http
  GET    /store/carts/<int:id>/items
  POST    /store/carts/<int:id>/items
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of cart to fetch |

#### Modify Cart item 

```http
  GET         /store/carts/<int:id>/items/<int:item_id>
  PUT         /store/carts/<int:id>/items/<int:item_id>
  DELETE      /store/carts/<int:id>/items/<int:item_id>
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of cart to fetch |
| `item_id`      | `string` | **Required**. Id of item to fetch |


## Orders

#### Get all Orders
```http
  GET         /store/orders
```
| Header | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `JWT Token` | `string` | **Required**. Admin only |

#### Order Detail

```http
  GET            /store/orders/<int:id>
  PUT            /store/orders/<int:id>
  DELETE         /store/orders/<int:id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of order to fetch |


| Header | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `JWT Token` | `string` | **Required**. Authentication required|

