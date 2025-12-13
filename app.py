from flask import Flask, render_template, request, jsonify
from Login import Login
from constants import FILE_NAME

app = Flask(__name__)
login_system = Login()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    user = login_system.create_account(username, email, password)
    if user:
        return jsonify({"success": True, "message": f"Account for {username} created!"})
    else:
        return jsonify({"success": False, "message": "Username already exists!"})

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    try:
        # login prints output; we want to capture success/failure
        try:
            login_system.login(username, password)
            return jsonify({"success": True, "message": "Login successful!"})
        except Exception:
            return jsonify({"success": False, "message": "Username/password incorrect!"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
