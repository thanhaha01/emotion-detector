from flask import Flask, request, jsonify
from emotion_detector import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def detect():
    text = request.args.get("textToAnalyze")
    if not text:
        return jsonify({"error": "Missing text input"}), 400

    result = emotion_detector(text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
