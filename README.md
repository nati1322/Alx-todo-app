# Todo API

This is a simple RESTful API for managing a todo list, built using Django and Django REST Framework. It allows authenticated users to create, retrieve, update, and delete their own todo items.

## Endpoints

The API provides the following endpoints:

* **User Registration (`/api/users/register/`) - POST**

* **Purpose:** Allows new users to create an account.
* **URL:** `/api/users/register/`
* **Method:** `POST`
* **Request Body (JSON - Example):**
    ```json
    {
        "username": "newuser1",
        "password": "securepassword",
        "email": "newuser1@email.com"

    }
    ```


* **User Login (`/api/users/login/`) - POST**

* **Purpose:** Allows existing users to log in and obtain an authentication token or session.
* **URL:** `/api/users/login/`
* **Method:** `POST`
* **Request Body (JSON - Example using username/password):**
    ```json
    {
        "username": "newuser1",
        "password": "securepassword",
        "email": "newuser1@email.com"

    }
    ```
* **Headers:** `Content-Type: application/json`
* **Response (Success - Status Code: 200 OK):**
    * **Session-based authentication:** The session ID is typically set in a cookie in the response headers.
    * **Token-based authentication (e.g., JWT):** The response body will contain the authentication token:
        ```json
        {
            "token": "your_access_token_here"
        }
        ```


* **`/api/todos/` (GET)**: List all todo items belonging to the authenticated user.
* **`/api/todos/` (POST)**: Create a new todo item for the authenticated user.
    * **Request Body (JSON):**
        ```json
        {
            "title": "Buy groceries",
            "description": "Milk, eggs, bread",
            "completed": false
        }
        ```
    * **Required Fields:** `title`
    * **Optional Fields:** `description`, `completed` (defaults to `false`)
* **`/api/todos/{id}/` (GET)**: Retrieve a specific todo item by its ID.
* **`/api/todos/{id}/` (PUT)**: Update a specific todo item by its ID.
    * **Request Body (JSON):** You can update any of the fields (`title`, `description`, `is_completed`).
        ```json
        {
            "title": "Walk the dog",
            "completed": true
        }
        ```
* **`/api/todos/{id}/` (DELETE)**: Delete a specific todo item by its ID.
* **`/api/todos/{id}/complete/` (PUT)**: Mark a specific todo item as complete. No request body is typically needed.
* **`/api/todos/{id}/incomplete/` (PUT)**: Mark a specific todo item as incomplete. No request body is typically needed.


