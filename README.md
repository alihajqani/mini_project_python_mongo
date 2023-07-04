# Project Name

Project Name is a Python application that interacts with a MongoDB database to perform operations on a "users" collection.

## Installation

1. Create a virtual environment to isolate the project dependencies:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
- For Windows:
  ```
  venv\Scripts\activate
  ```
- For Unix or Linux:
  ```
  source venv/bin/activate
  ```

3. Install the required packages by running the following command in the project's root directory:
  ```
  pip install -r requirements.txt
  ```

4. Install MongoDB:
- Follow the official MongoDB documentation to install MongoDB on your system: [MongoDB Installation Guide](https://docs.mongodb.com/manual/installation/)

5. Create a database named "shop" in MongoDB.

6. Create a collection named "users" within the "shop" database.

## Usage

1. Make sure your virtual environment is activated.

2. Run the Python application with the following command:
  ```
  uvicorn main:app --reload
  ```

3. Open your web browser and navigate to `http://localhost:8000` to access the application.
