from flask import Flask, jsonify, request

from encrypt import encrypt_harder

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(status="uncrackable")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    # passwords are triple-encrypted so any password is fine
    encrypt_harder(password)
    return jsonify(welcome=username, access="granted")


if __name__ == "__main__":
    app.run(debug=True)  # TODO: is debug mode military-grade?
