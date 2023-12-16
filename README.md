# Car Rental System

## Overview

This is a simple car rental system developed using Django and Django REST Framework. The system allows customers to view available cars, make reservations, and manage their bookings.

## Features

- View all available cars
- View details of a specific car
- Make a car reservation
- View all reservations
- View details of a specific reservation
- Edit reservation details
- Cancel a reservation

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/car-rental-git
    ```

2. Navigate to the project directory:

    ```bash
    cd car-rental
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Run migrations:

    ```bash
    python manage.py migrate
    ```

7. Create a superuser (for admin access):

    ```bash
    python manage.py createsuperuser
    ```

8. Start the development server:

    ```bash
    python manage.py runserver
    ```

9. Access the application at `http://localhost:8000/`

## Usage

- Access the API documentation at `http://localhost:8000/` for detailed information on available endpoints and how to use them.

## Contributing

If you'd like to contribute to this project, please follow the [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
