# Integrated Communication Framework

## Overview

The Integrated Communication Framework is a comprehensive solution that combines email and chat functionalities into a single, cohesive platform. This project aims to streamline communication by providing a unified interface for managing both email and instant messaging.

## Features

- **User Authentication**: Secure login system to manage user access.
- **Email Service**: 
  - Send and receive emails
  - View inbox
  - Mark emails as read
  - Delete emails
- **Chat Service**:
  - Real-time messaging between users
  - View chat history
  - Mark messages as read
  - Delete messages
- **WebSocket Integration**: Real-time updates for both email and chat services.
- **Database Integration**: Persistent storage of emails and chat messages using SQLite.
- **SMTP Server**: Custom SMTP server for handling email operations.
- **Docker Support**: Containerized deployment for easy setup and scalability.

## Technology Stack

- **Backend**: Python 3.9+
- **Web Framework**: aiohttp
- **Database**: SQLite (with aiosqlite for async operations)
- **Frontend**: HTML, CSS, JavaScript
- **Real-time Communications**: WebSockets
- **Email Handling**: aiosmtpd, smtplib
- **Session Management**: aiohttp_session
- **Environment Management**: python-dotenv
- **Docker**: Containerization for deployment

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/arsalanrex/integrated-communication-framework.git
   cd integrated-communication-framework
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the environment variables:
   - Copy the `.env.example` file to `.env`
   - Fill in the necessary configuration details in the `.env` file
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

### Locally

- To run the application locally, use the following command:

1. Initialize the database:
   ```
   python init_db.py
   ```

2. Start the SMTP server:
   ```
   python smtp_server.py
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open a web browser and navigate to `http://localhost:8080` (or the port specified in your configuration).

### Docker

- To run the application using Docker, build the image and run the container:

  ```
  docker-compose build
  docker-compose up
  
  > log in to localhost:8080
  ```

## Project Structure

```
integrated-communication-framework/
│
├── app.py                 # Main application file
├── init_db.py             # Database initialization script
├── smtp_server.py         # Custom SMTP server
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables (create this from .env.example)
├── README.md              # Project documentation
├── users.py               # User management
├── users.json             # User list
│
├── config/
│   └── settings.py        # Application settings and configurations
│
├── email_service/
│   ├── email_manager.py   # Email handling logic
│   └── email_storage.py   # Email database operations
│
├── chat_service/
│   ├── chat_manager.py    # Chat handling logic
│   └── chat_storage.py    # Chat database operations
│
├── static/
│   └── style.css          # CSS styles for the frontend
│
└── templates/
    └── index.html         # Main HTML template for the application
```

## Usage

1. **Login**: Use the provided login form to authenticate with your username and password.

2. **Email**:
   - To send an email, fill in the recipient, subject, and body fields in the email tab, then click "Send Email".
   - View your inbox in the email tab.
   - Click on individual emails to mark them as read or delete them.

3. **Chat**:
   - To start a chat, enter the recipient's username and your message in the chat tab, then click "Send Message".
   - View your chat history in the chat tab.
   - Messages are updated in real-time using WebSockets.

## Development

- To add new features or modify existing ones, locate the relevant files in the project structure.
- For frontend changes, modify the `templates/index.html` and `static/style.css` files.
- For backend changes, update the relevant Python files in the `email_service/`, `chat_service/`, or root directory.
- Always update the `requirements.txt` file if you add new dependencies:
  ```
  pip freeze > requirements.txt
  ```

## Testing

- To run tests (if implemented), use the following command:
  ```
  python -m unittest discover tests
  ```

## Contributing

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/arsalanrex/Integrated-Communication-Framework/blob/main/LICENCE) file for details.

The MIT License is a permissive license that is short and to the point. It lets people do almost anything they want with your project, like making and distributing closed source versions, as long as they include the original copyright and license notice.

## Contact

For any queries or support, please contact [Arsalan] at [arsalan.rex@gmail.com].