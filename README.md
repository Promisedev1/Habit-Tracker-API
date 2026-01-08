# 🚀 Habit Tracker API 🎯

A powerful and intuitive RESTful API to help you build amazing habit-tracking applications. Stay motivated, track your progress, and achieve your goals! 💪

## ✨ Features

*   **User Authentication:** Secure user registration and login using JWT (JSON Web Tokens). 🔐
*   **Habit Management:** Full CRUD (Create, Read, Update, Delete) functionality for habits.
*   **Progress Tracking:** Mark habits as complete and monitor your progress.
*   **Scalable Architecture:** Built with Flask and SQLAlchemy for a robust and scalable backend.
*   **Rate Limiting:** Protects the API from brute-force attacks.

## 🛠️ Tech Stack

*   **Backend:** [Flask](https://flask.palletsprojects.com/)
*   **Database:** [SQLAlchemy](https://www.sqlalchemy.org/) (with SQLite as the default database)
*   **Authentication:** [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/)
*   **API Testing:** [Postman](https://www.postman.com/) or any API client.

## 🏁 Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

*   [Python 3.8+](https://www.python.org/downloads/)
*   [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)

### ⚙️ Installation

1.  **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd habit-tracker
    ```

2.  **Create and activate a virtual environment:**
    *   **Windows:**
        ```sh
        python -m venv .venv
        .venv\Scripts\activate
        ```
    *   **macOS/Linux:**
        ```sh
        python3 -m venv .venv
        source .venv/bin/activate
        ```

3.  **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

### ▶️ Running the Application

1.  **Run the development server:**
    ```sh
    python run.py
    ```
2.  The API will be available at `http://127.0.0.1:5000`.

## 📖 API Endpoints

Here's a quick overview of the available endpoints. For detailed information on request/response formats, please refer to the source code.

### Auth
*   `POST /api/v1/register` - Register a new user.
*   `POST /api/v1/login` - Log in a user and receive a JWT.
*   `POST /api/v1/logout` - Log out a user.

### Habits
*   `POST /api/v1/habits` - Create a new habit.
*   `GET /api/v1/habits` - Get all habits for the logged-in user.
*   `GET /api/v1/habits/<int:habit_id>` - Get a specific habit.
*   `PUT /api/v1/habits/<int:habit_id>` - Update a habit.
*   `DELETE /api/v1/habits/<int:habit_id>` - Delete a habit.
*   `POST /api/v1/habits/<int:habit_id>/complete` - Mark a habit as complete.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.