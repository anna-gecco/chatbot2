from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import chatbot_response

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    answer = chatbot_response(user_input)
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)