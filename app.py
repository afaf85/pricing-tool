from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Flask-Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv("EMAIL_USER")
app.config['MAIL_PASSWORD'] = os.getenv("EMAIL_PASS")
app.config['MAIL_DEFAULT_SENDER'] = os.getenv("EMAIL_USER")

mail = Mail(app)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')  # Render index.html for the homepage

# Email Route
@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    try:
        msg = Message(
            subject="New Contact Form Submission",
            recipients=["acosta.franky@gmail.com"],
            body=f"Name: {data['name']}\nEmail: {data['email']}\nMessage: {data['message']}"
        )
        mail.send(msg)
        return jsonify({"status": "success", "message": "Email sent successfully!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
