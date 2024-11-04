import os
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import socket
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
warnings.filterwarnings('ignore')

from training_data import training_data
   
# Flask app setup
app = Flask(__name__)
CORS(app)
load_dotenv()

# Convert training data into separate questions and responses lists
questions = [item[0] for item in training_data]
responses = [item[1] for item in training_data]

# TF-IDF Vectorizer setup for matching user inputs to predefined questions
vectorizer = TfidfVectorizer().fit(questions)

# Helper function to find a free port if the default one is in use
def find_free_port():
    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_socket.bind(('0.0.0.0', 0))  # Bind to any IP and an available port
    port = new_socket.getsockname()[1]
    new_socket.close()
    return port

def get_chatbot_response(user_message):
    user_message_vectors = vectorizer.transform([user_message])
    question_vectors = vectorizer.transform(questions)
    
    # calculate cosine similarities between user message and questions
    similarities = cosine_similarity(user_message_vectors, question_vectors).flatten()
    
    # Find the index of the best match bbased on similarity scores
    best_match_index = np.argmax(similarities)
    best_match_score = similarities[best_match_index]
    
    # Set a threshold to ensure the match is strorng enough
    threshold = 0.2
    if best_match_score >= threshold:
        return responses[best_match_index]
    else:
        return "I'm sorry, I didn't quite understand that. Could you pleas rephrase?"
    

# API route for receiving messages
@app.route('/chat', methods=['POST'])
def chatBot():
    data = request.json
    user_message = data.get('message')
    
    if not user_message:
        return jsonify({"error": "Message content missing"}), 400
    
    try:
        response = get_chatbot_response(user_message)
        print('response', response)
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
        print('app running')
        app.run(debug=True, port=assigned_port)
    except OSError:
        free_port = find_free_port()
        print(f"Assigned port {assigned_port} is in use. Switching to port {free_port}")
        app.run(debug=True, port=free_port)
