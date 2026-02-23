from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "project": "MediDrone UAV Delivery System",
        "status": "Server Running"
    })

if __name__ == "__main__":
    app.run(debug=True)