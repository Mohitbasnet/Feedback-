
# Feedback Web Application

This Django project aims to create a web application for collecting user feedback and reviews. It utilizes Django's built-in functionalities along with custom views, models, and templates to provide a seamless user experience.

## Installation

1. Clone the repository to your local machine:
     - git clone <repository_url>

2. Create a virtual environment and activate it:

    - pip install virtualenv
    - virtualenv envname
    - envname\scripts\activate # For Windows
    - source envname/bin/activate # For macOS/Linux

3. Navigate to the project directory:

    - cd feedback_project

4. Install project dependencies:

    - pip install -r requirements.txt

5. Apply database migrations:

    - python manage.py migrate

6. Run the development server:

   - python manage.py runserver

7. Access the application via your web browser at [http://localhost:8000/](http://localhost:8000/).

## Features

- Submit and view user profiles
- Submit and view reviews
- Session management for marking favorite reviews


## Tech Stack

- Django
- SQLite

## Project Overview

- Basic Django code
- Database Design and Models
- Management of Static Files

## Contributing

Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
