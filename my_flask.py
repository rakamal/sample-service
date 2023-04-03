from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/service2", methods=["GET"])
def say_hello():
    print(" Welcome Team B!")
    return " Welcome Team B!"


if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=6000, debug=True)
