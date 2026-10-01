from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(status="uncrackable")


if __name__ == "__main__":
    app.run(debug=True)  # TODO: is debug mode military-grade?
