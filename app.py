
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def recommend_shot(bowler, pitch, length, situation):
    # Rule-based AI logic
    if bowler == "Fast" and length == "Short":
        return {
            "shot": "Pull Shot",
            "risk": "Medium",
            "reason": "Short balls from fast bowlers are ideal for pull shots.",
            "alternative": "Hook Shot"
        }

    if bowler == "Fast" and length == "Good":
        return {
            "shot": "Cover Drive",
            "risk": "Low",
            "reason": "Good length ball allows proper timing on dry pitches.",
            "alternative": "Straight Drive"
        }

    if bowler == "Spin" and pitch == "Dusty":
        return {
            "shot": "Sweep Shot",
            "risk": "Low",
            "reason": "Dusty pitches assist spin, making sweep effective.",
            "alternative": "Reverse Sweep"
        }

    if bowler == "Spin" and situation == "Death Overs":
        return {
            "shot": "Lofted Shot",
            "risk": "High",
            "reason": "Aggressive play needed in death overs against spin.",
            "alternative": "Inside-Out Shot"
        }

    return {
        "shot": "Defensive Shot",
        "risk": "Low",
        "reason": "Safe option based on given conditions.",
        "alternative": "Leave the Ball"
    }

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    result = recommend_shot(
        data["bowler"],
        data["pitch"],
        data["length"],
        data["situation"]
    )
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
