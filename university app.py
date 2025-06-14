from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, auth, firestore

# Initialize Flask App
app = Flask(__name__)

# Firebase Setup
cred = credentials.Certificate("firebase_credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# User Authentication
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    user = auth.create_user(email=data["email"], password=data["password"])
    return jsonify({"message": "User registered", "uid": user.uid})

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = auth.get_user_by_email(data["email"])
    return jsonify({"message": "Login successful", "uid": user.uid})

# Attendance Tracking
@app.route("/mark_attendance", methods=["POST"])
def mark_attendance():
    data = request.json
    db.collection("attendance").add({
        "student_id": data["student_id"],
        "course_id": data["course_id"],
        "timestamp": firestore.SERVER_TIMESTAMP
    })
    return jsonify({"message": "Attendance marked"})

@app.route("/get_attendance", methods=["GET"])
def get_attendance():
    course_id = request.args.get("course_id")
    records = db.collection("attendance").where("course_id", "==", course_id).stream()
    attendance_list = [{"student_id": rec.get("student_id"), "timestamp": rec.get("timestamp")} for rec in records]
    return jsonify(attendance_list)

# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)

