from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/service1", methods=["GET"])
def say_hello():
    print(" Welcome Team A!")
    return " Welcome Team A!"


if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=5000, debug=True)
