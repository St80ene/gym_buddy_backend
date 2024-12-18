from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
from gym_buddy import get_chatbot_response
from utils import find_free_port
import os

app = Flask(__name__)
CORS(app)
load_dotenv()

# API route for receiving messages
@app.route('/chat', methods=['POST'])
def chatBot():
    data = request.json
    user_message = data.get('message')
    
    if not user_message:
        return jsonify({"error": "Message content missing"}), 400
    
    try:
        response = get_chatbot_response(user_message)
        return jsonify({"response": response})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    

if __name__ == "__main__":
    # Read the port from the environment variable, default to 5000 if not set
    assigned_port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=assigned_port)