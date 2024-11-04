from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from gensim.parsing.preprocessing import preprocess_string

from gensim.models import Word2Vec
from training_data import training_data

stemmer = PorterStemmer()

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens

processed_training_data = [preprocess_text(item) for item in training_data]
model = Word2Vec(processed_training_data, min_count=1, window=5)

def get_chatbot_response(user_message):
    
    preprocessed_message = preprocess_text(user_message)
    
    similar_words = model.wv.most_similar(positive=[preprocessed_message], topn=1)
    
    print('similar_words', similar_words)
    if not similar_words:
        return "Sorry, I'm unable to answer this question"
    
    # Assuming questions are first element in each trainind data pair
    response_index = 0
    response = training_data[similar_words[0][0][response_index]]
    
    return response