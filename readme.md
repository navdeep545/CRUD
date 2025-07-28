# FastAPI CRUD

This is a CRUD (Create, Read, Update, Delete) application built using FastAPI, SQLAlchemy, and PostgreSQL.

## Tech Stack

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **SQLAlchemy**: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **PostgreSQL**: A powerful, open-source object-relational database system.
- **Pydantic**: Data validation and settings management using Python type annotations.

## Setup Instructions

Follow these steps to set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd fastapi-basic-crud
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   - Ensure PostgreSQL is installed and running.
   - Update the `SQLALCHEMY_DATABASE_URL` in `db.py` with your PostgreSQL credentials.

5. **Create database tables**:
   ```bash
   python temp.py
   ```

6. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```

7. **Access the API**:
   - Open your browser and navigate to `http://127.0.0.1:8000/docs` to explore the API documentation.

## Notes

- Make sure PostgreSQL is properly configured and accessible.
- Use the `.gitignore` file to exclude unnecessary files from version control.



