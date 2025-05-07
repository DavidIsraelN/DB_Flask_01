# Flask-Postgres Integration Project
## Overview

This project demonstrates a Flask application integrating with a PostgreSQL database using the `psycopg2` library. The project showcases a clean architecture with a structured repository and service layer. It allows the management of users and their roles while integrating with the Nobel API to fetch additional country information.

Practice in the Advanced Python Course for ExcellenTeam

---

## Project Setup

### Prerequisites

* Python 3.8+
* PostgreSQL
* Docker
* Flask
* psycopg2-binary
* Postman (optional, for API testing)

---

## Database Setup

### Running PostgreSQL with Docker

Use the following command to create and run a PostgreSQL container:

```bash
docker run -d --name my-postgres-edu \
    -e POSTGRES_DB=dbname \
    -e POSTGRES_USER=admin \
    -e POSTGRES_PASSWORD=Aa123456 \
    -p 5433:5432 postgres:latest
```

* `POSTGRES_DB`: Specifies the database name.
* `POSTGRES_USER`: Specifies the username for authentication.
* `POSTGRES_PASSWORD`: Specifies the password for authentication.
* `-p 5432:5432`: Maps port 5432 on the host to port 5432 on the container.

---

## Flask Application Structure

### Directory Layout

```plaintext
project/
├── app/
│   ├── __init__.py
│   ├── user_routes.py
│   ├── user_service.py
│   ├── nobel_service.py
│   ├── user_repository.py
│   ├── nobel_repository.py
│   ├── db_connection.py
├── requirements.txt
├── README.md
└── run.py
```

### Key Components

1. **Database Connection (`db_connection.py`)**

   * Manages database connections using `psycopg2`.
   * Provides reusable functionality for executing queries and transactions.

2. **Repository Layer (`repositories`):**

   * Encapsulates direct interactions with the database.
   * Examples: CRUD operations for `users` and fetching country codes from the Nobel API.

3. **Service Layer (`services`):**

   * Contains business logic.
   * Validates and processes data from repositories before sending to routes.

4. **Routes Layer (`routes`):**

   * Handles API endpoints.
   * Connects service methods to HTTP requests.

---

## API Endpoints Documentation

### 1. **Create User Table**
- **Endpoint:** `POST /users/create_user_table`
- **Description:** Creates the `user` table in the database.
- **Response:**
  - Success: `{"message": "User table created successfully."}`
  - Error: Returns an error message with status code 500.

---

### 2. **Create User Role Table**
- **Endpoint:** `POST /users/create_user_role_table`
- **Description:** Creates the `user_role` table in the database.
- **Response:**
  - Success: `{"message": "User role table created successfully."}`
  - Error: Returns an error message with status code 500.

---

### 3. **Get All Users**
- **Endpoint:** `GET /users`
- **Description:** Retrieves all users from the database.
- **Response:**
  - Success: Returns a list of users.
  - Error: Returns an error message with status code 500.

---

### 4. **Get User with Role by ID**
- **Endpoint:** `GET /users/get_user_with_role/<int:user_id>`
- **Description:** Retrieves a user by their ID, including their role if assigned.
- **Response:**
  - Success: Returns user details along with their role.
  - Error: Returns a 400 or 500 status code with an error message.

---

### 5. **Get Country Code by User ID**
- **Endpoint:** `GET /users/get_country_code`
- **Query Parameter:** `user_id` (Required)
- **Description:** Retrieves the country code for a user based on their country name.
- **Response:**
  - Success: Returns the country code.
  - Error: Returns a 400 or 500 status code with an error message.

---

### 6. **Add New User**
- **Endpoint:** `POST /users/add_user`
- **Description:** Adds a new user to the database.
- **Request Body:**
  ```json
  {
    "first_name": "John",
    "last_name": "Doe",
    "country": "USA",
    "national_id": "123456789",
    "phone_number": "5551234567"
  } 
  ```
- **Response:**

  * Success: Returns the created user object (excluding the ID).
  * Error: Returns a 400 or 500 status code with an error message.

---

### 7. **Add User with Role**

* **Endpoint:** `POST /users/add_user_with_role`
* **Description:** Adds a new user and assigns a role to them.
* **Request Body:**
  ```json
  {
    "user": {
      "first_name": "Jane",
      "last_name": "Smith",
      "country": "Canada",
      "national_id": "987654321",
      "phone_number": "5559876543"
    },
    "role": "student"
  }
  ```
* **Response:**

  * Success: Returns the created user object with their role.
  * Error: Returns a 400 or 500 status code with an error message.

---

## Notable Highlights

1. **Transactional Safety:**

   * Transactions ensure atomicity when creating users and roles.
   * Any failure during the process rolls back the transaction.

2. **External API Integration:**

   * The Nobel API is used to fetch country codes based on the user's country.
   * Caching or optimizing API calls can improve performance.

---

## Running the Application

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/DavidIsraelN/DB_Flask_01.git
   cd DB_Flask_01
   ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv .venv
    source venv/bin/activate   
    # On Windows: ./.venv\Scripts\activate
    ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Start Flask Server:**

   ```bash
   python run.py
   # or - flask run
   ```

5. **Access Endpoints:**
   Use tools like Postman or `curl` to interact with the API.

---

## Database Schema

### `users` Table

| Column        | Type         | Constraints     |
| ------------- | ------------ | --------------- |
| id            | SERIAL       | PRIMARY KEY     |
| first\_name   | VARCHAR(250) | NOT NULL        |
| last\_name    | VARCHAR(250) | NOT NULL        |
| country       | VARCHAR(250) | NOT NULL        |
| national\_id  | VARCHAR(250) | NOT NULL        |
| phone\_number | VARCHAR(250) | NOT NULL        |

### `user_role` Table

| Column     | Type         | Constraints                                          |
| ---------- | ------------ | ---------------------------------------------------- |
| id         | SERIAL       | PRIMARY KEY                                          |
| user\_id   | INTEGER      | FOREIGN KEY REFERENCES `users`(id)                   |
| user\_type | VARCHAR(250) | CHECK(user\_type IN ('student', 'teacher', 'admin')) |

---

## Future Enhancements

1. **Authentication:** Add user authentication and authorization.
2. **Caching:** Optimize country code lookups with caching.
3. **Pagination:** Add pagination for user-related endpoints.

---

## References

* Flask Documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
* Psycopg2 Documentation: [https://www.psycopg.org/docs/](https://www.psycopg.org/docs/)
* Nobel API: [https://api.nobelprize.org/v1/country.json](https://api.nobelprize.org/v1/country.json)
