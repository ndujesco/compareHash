from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify(message="This is the home page. Just put it because why not?😊")


@app.post("/hash-password")
def hash_the_password():
    print(request.json)
    hashed_and_salted_password = generate_password_hash(
        request.json["password"],
        method='pbkdf2:sha256',
        salt_length=1)

    print(hashed_and_salted_password)
    return jsonify(hashedPassword=hashed_and_salted_password)


@app.post("/check-password")
def check_the_password():
    print(request.json["hashedPassword"])
    password = request.json["password"]
    hashed_password = request.json["hashedPassword"]

    matches = check_password_hash(hashed_password, password)
    print(matches)
    return jsonify(matches=matches)


if __name__ == '__main__':
    app.run(debug=True)
