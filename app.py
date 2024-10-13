import os
import socket
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from gensim.models import Word2Vec
from training_data import training_data

stemmer = PorterStemmer()

# Preprocessing function for text
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    return tokens

# Process training data (ensure training_data is a list of tuples (question, response))
processed_training_data = [(preprocess_text(question), preprocess_text(response)) for question, response in training_data]

# Train Word2Vec model using only the questions from the processed training data
model = Word2Vec([question for question, response in processed_training_data], min_count=1, window=5)

# Chatbot response function
def get_chatbot_response(user_message):
    # Preprocess the user input message
    preprocessed_message = preprocess_text(user_message)
    
    # Get most similar words based on the input
    try:
        similar_words = model.wv.most_similar(positive=[preprocessed_message], topn=1)
        print('similar_words', similar_words)
        
        # Get the index of the most similar word
        most_similar_word = similar_words[0][0]
        
        # Find the matching question in the training_data and return the response
        for question, response in training_data:
            if most_similar_word in preprocess_text(question):
                return response
        
        # If no match is found, return a default response
        return "Sorry, I couldn't find a suitable response."
    
    except KeyError:
        return "Sorry, I couldn't understand that."
      
      
# Flask app setup
app = Flask(__name__)
CORS(app)
load_dotenv()

# Helper function to find a free port if the default one is in use
def find_free_port():
    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_socket.bind(('0.0.0.0', 0))  # Bind to any IP and an available port
    port = new_socket.getsockname()[1]
    new_socket.close()
    return port

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
