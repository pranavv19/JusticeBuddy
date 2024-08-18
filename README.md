Project Description
JusticeBuddy is a web application designed to provide users with accurate and timely legal advice using the power of artificial intelligence. Leveraging the GPT API, JusticeBuddy processes user queries to generate comprehensive legal guidance based on extensive legal knowledge and datasets. This project aims to make legal advice accessible to everyone by providing a user-friendly platform for legal assistance.

Features
AI-Powered Legal Advice: Utilizes the GPT API to deliver accurate legal guidance.
User-Friendly Interface: Simplified design for easy navigation and query submission.
Secure and Confidential: Ensures user data privacy and secure handling of sensitive information.
Scalable Architecture: Built with Django, allowing for efficient scaling and maintenance.
Project Structure
JusticeBuddy-master/
├── .idea/
├── JusticeBuddy/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __pycache__/
├── home/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── __pycache__/
├── templates/
│   └── index.html
├── db.sqlite3
├── manage.py
├── requirements.txt
└── runtime.txt
Installation
Clone the Repository:

git clone https://github.com/Hridxyz/JusticeBuddy.git
cd JusticeBuddy
Create a Virtual Environment and Activate it:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

pip install -r requirements.txt
Set Up Environment Variables: Create a .env file in the project root and add the following:

DEBUG=False
SECRET_KEY=your-secret-key
GPT_API_KEY=your-gpt-api-key
Apply Migrations:

python manage.py migrate
Run the Development Server:

python manage.py runserver
Usage
Visit http://127.0.0.1:8000 in your web browser.
Submit your legal queries through the interface.
Receive AI-generated legal advice instantly.
Technology Used
Backend: Python, Django
Frontend: HTML, CSS, JavaScript
API: GPT API
Database: SQLite
Skills Utilized
Web Development
API Integration
Legal Data Analysis
Ethical AI Implementation
Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.
