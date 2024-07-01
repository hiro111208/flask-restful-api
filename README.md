# Planetary API

## Description

Planetary API is a Flask-based web application that allows users to manage a collection of planets and user accounts. It supports CRUD operations for planet data and provides user authentication via JWT.

## Features

- User registration and login
- CRUD operations for managing planet data
- JWT authentication for protected routes
- Basic parameter handling in routes

## Deployed website

<https://hirofunatsuka.pythonanywhere.com/>

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/planetary-api.git
   cd planetary-api
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the environment variables:**
   Create a `.env` file in the root directory and add the following:

   ```
   FLASK_ENV=development
   SECRET_KEY=your_secret_key
   SQLALCHEMY_DATABASE_URI=your_database_uri
   MAIL_SERVER=your_mail_server
   MAIL_PORT=your_mail_port
   MAIL_USERNAME=your_email
   MAIL_PASSWORD=your_password
   ```

5. **Initialize the database:**
   ```bash
   flask /db_drop
   flask /db_create
   flask /db_seed
   ```

## Usage

1. **Run the application:**

   ```bash
   flask run
   ```

2. **API Endpoints:**
   - **`GET /`**: Returns a simple "Hello, World!" message.
   - **`GET /super_simple`**: Returns a JSON message.
   - **`GET /not_found`**: Returns a 404 JSON message.
   - **`GET /parameters`**: Handles URL parameters `name` and `age`.
   - **`GET /url_variables/<name>/<age>`**: Handles URL path variables `name` and `age`.
   - **`GET /planets`**: Returns a list of all planets.
   - **`POST /register`**: Registers a new user.
   - **`POST /login`**: Authenticates a user and returns a JWT token.
   - **`GET /planet_details/<planet_id>`**: Retrieves details of a specific planet.
   - **`POST /add_planet`**: Adds a new planet (JWT required).
   - **`PUT /update_planet`**: Updates an existing planet (JWT required).
   - **`DELETE /remove_planet/<planet_id>`**: Deletes a planet (JWT required).

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.

## License

This project is licensed under the MIT License.
