# Integrated Communication Framework

This project implements an integrated communication framework with email and chat services using Python and aiohttp.

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/integrated-communication.git
   cd integrated-communication
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add the following variables:
   ```
   EMAIL_SERVER=localhost
   EMAIL_PORT=1025
   EMAIL_USERNAME=your_username
   EMAIL_PASSWORD=your_password
   CHAT_SERVER=localhost
   CHAT_PORT=5222
   DATABASE_URI=sqlite:///integrated_communication.db
   SECRET_KEY=your_secret_key
   WEBSOCKET_HOST=localhost
   WEBSOCKET_PORT=8080
   ```

## Running the Application

1. Start the application:
   ```
   python integrated_communication/app.py
   ```

2. Open a web browser and navigate to `http://localhost:8080`.

3. Log in using one of the predefined user credentials (check `config/settings.py` for user details).

login credentials you can use:

For User 1:

Username: user1
"email": "user1@example.com",
"password": "password1",
"mobile": "+1234567890"

For User 2:

Username: user2
"email": "user2@example.com",
"password": "password2",
"mobile": "+0987654321"

## Features

- User authentication
- Email service (send and receive emails)
- Chat service (send and receive messages)
- Real-time updates using WebSockets
- Responsive design for desktop and mobile devices

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.