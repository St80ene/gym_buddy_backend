import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from training_data import training_data

# Separate questions and responses from training data
questions = [item[0] for item in training_data]
responses = [item[1] for item in training_data]

# TF-IDF Vectorizer setup
vectorizer = TfidfVectorizer().fit(questions)

def get_chatbot_response(user_message):
    # transform questions and responses to vectors for processing
    user_message_vectors = vectorizer.transform([user_message])
    question_vectors = vectorizer.transform(questions)
    
    # Calculate cosine similarities between user message and questions
    similarities = cosine_similarity(user_message_vectors, question_vectors).flatten()
    
    # Find the index of the best match based on similarity scores
    best_match_index = np.argmax(similarities)
    best_match_score = similarities[best_match_index]
    
    # Set a threshold to ensure the match is strong enough
    threshold = 0.2
    if best_match_score >= threshold:
        return responses[best_match_index]
    else:
        return "I'm sorry, I didn't quite understand that. Could you please rephrase?"
