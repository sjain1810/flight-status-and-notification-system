## Flight Status and Notifications System

This project provides real-time flight status updates and notifications to passengers.
It displays current flight status, sends notifications for changes, and integrates with airport systems using mock data.

## Features

1. Real-time Updates: Displays current flight status, including delays, cancellations, and gate changes.
2. Push Notifications: Sends notifications for flight status changes via SMS, email, or app notifications.
3. Integration with Airport Systems: Pulls data from airport databases for accurate information (using mock data in this implementation).

## Tech. Stack

1. Frontend - HTML, CSS , JavaScript and React.js
2. Backend - Python (Flask), PostgreSQL (Structured data) , MongoDB (Unstructured data), Message : Kafka (Notifications)

## Setup and Installation

1. Prerequisites

- Python (>= 3.9)
- Node.js
- PostgreSQL
- MongoDB

2. Backend Setup

   1. Clone the repository:
      git clone <repository-url>

   2. Create a virtual environment:
      python -m venv venv

   3. Install dependencies:
      pip install Flask Flask-Cors Flask-SQLAlchemy psycopg2-binary pymongo SQLAlchemy requests python-dotenv kafka-python pika pytest pytest-flask

   4. Set up PostgreSQL

   5. Set up MongoDB

   6. Run the backend server

3. Frontend Setup

   1. Navigate to the frontend directory:
      cd flight-status-frontend
   2. Install dependencies (if using a package manager like npm):
   3. Run the frontend development server:

## Usage

    1. Access the Application:

        Open your browser and go to http://localhost:3000 to access the frontend.
        The backend API is accessible at http://localhost:5000/api.

    2. View Flight Status:

        The home page displays a table of flights with their current status, gate number, and other details.

    3. Subscribe to Notifications:

        Users can subscribe to notifications by providing their email or phone number.

## Testing

    1. Backend

        Run tests for the Flask API using pytest or any preferred testing framework.
        Ensure that all endpoints and data flows work correctly.

    2. Frontend

    Use tools like Jest and React Testing Library for testing frontend components.

## Deployment

    1. Backend

        Deploy the Flask backend on platforms like Heroku, AWS, or DigitalOcean.
        Set up PostgreSQL and MongoDB databases on the cloud.

    2. Frontend

    Deploy the frontend on Netlify, Vercel, or GitHub Pages.

    3. Environment Variables

    Database Credentials: Store PostgreSQL and MongoDB credentials securely.
    API Keys: If using third-party services for notifications, store API keys securely.
