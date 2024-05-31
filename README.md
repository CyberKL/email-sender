# Selenium and Django Assignment

## Project Overview
This project automates the submission of a Google Form using Selenium, captures a screenshot of the confirmation page, and sends an email with the screenshot attached using Django.

## Approach
- **Selenium Script**: Used Selenium to fill out and submit the Google Form and capture a screenshot.
- **Django**: Set up a Django project to send an email with the screenshot as an attachment.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/CyberKL/email-sender.git
   cd email-sender 
2. Install dependecies and setup env varaiables:
    ```bash
    pip install -r requirements.txt
    export EMAIL_ADDRESS=your-email@example.com
    export APP_PASS=your-app-password
3. Apply migrations and start the Django server:
    python manage.py migrate
    python manage.py runserver

## Sending the email
Visit "http://localhost:8000/send-email/" to start the email sending proccess.
You can change the email data in email_sender_app/views
