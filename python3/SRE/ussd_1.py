# Read the variables sent via POST from our API
import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def ussd_handler():
    # Read variables sent via POST
    session_id = request.form.get("sessionId", "")
    service_code = request.form.get("serviceCode", "")
    phone_number = request.form.get("phoneNumber", "")
    text = request.form.get("text", "")

    # Initialize response
    response = ""

    # Menu handling
    if text == "":
        # First request
        response = "CON What would you want to check?\n"
        response += "1. My Account\n"
        response += "2. My phone number\n"
    elif text == "1":
        # First level response
        response = "CON Choose account information you want to view\n"
        response += "1. Account number\n"
    elif text == "2":
        # First level response
        response = "END Your phone number is {}".format(phone_number)
    elif text == "1*1":
        # Second level response
        account_number = "ACC1001"
        response = "END Your account number is {}".format(account_number)

    # Send response back to the API
    return response

if __name__ == "__main__":
    # Run the Flask app
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

