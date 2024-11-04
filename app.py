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

# API route for shutting down the server
@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server = request.environ.get('werkzeug.server.shutdown')
    if shutdown_server is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    shutdown_server()
    return jsonify({"message": "Server shutting down..."})

# Main execution block
if __name__ == "__main__":
    assigned_port = int(os.getenv('PORT', 5000))
    
    try:
        print('App running...')
        app.run(debug=True, port=assigned_port)
    except OSError:
        free_port = find_free_port()
        print(f"Assigned port {assigned_port} is in use. Switching to port {free_port}")
        app.run(debug=True, port=free_port)
