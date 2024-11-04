### GYM Buddy API

A simple chatbot API that uses TF-IDF and cosine similarity to find the best response to user
queries. This project is implemented using Flask and includes features such as response handling,
custom port setup, and a shutdown API for stopping the server.


---
## Table of Contents
1. [Project Structure](#project-structure)
2. [Getting Started](#getting-started)
3. [Environment Variables](#environment-variables)
4. [Running the Application](#running-the-application)
5. [API Endpoints](#api-endpoints)
6. [Testing with Postman](#testing-with-postman)
7. [Documentation](https://documenter.postman.com/preview/11145480-72e90be0-85e6-40d0-89b1-122465119322?environment=&versionTag=latest&apiName=CURRENT&version=latest&documentationLayout=classic-double-column&documentationTheme=light&logo=https%3A%2F%2Fres.cloudinary.com%2Fpostman%2Fimage%2Fupload%2Ft_team_logo%2Fv1%2Fteam%2Fanonymous_team&logoDark=https%3A%2F%2Fres.cloudinary.com%2Fpostman%2Fimage%2Fupload%2Ft_team_logo%2Fv1%2Fteam%2Fanonymous_team&right-sidebar=303030&top-bar=FFFFFF&highlight=FF6C37&right-sidebar-dark=303030&top-bar-dark=212121&highlight-dark=FF6C37)


## Project Structure

Here’s the structure of the project:

```bash
.
├── app.py                   # Main Flask application
├── config.py                # Configuration for environment variables
├── utils.py                 # Utility functions (e.g., free port finder)
├── response_handler.py      # Response processing logic
├── training_data.py         # Sample training data for the chatbot
├── .env                     # Environment file for custom variables
├── README.md                # Project documentation

```
## Getting Started
To set up the project, follow these steps:

Prerequisites
- Python 3.x
- [pip](https://pip.pypa.io/en/stable/) for package management

#### Installation

1. Clone the Repository

  ```bash
  git clone https://github.com/your-username/flask-chatbot-api.git
  cd flask-chatbot-api
  ```
2. Create a Virtual Environment

  ```bash
  python3 -m venv venv
  source venv/bin/activate   # On Windows use `venv\Scripts\activate`
  ```
3. Install Dependencies
  ```bash
  pip install -r requirements.txt
  ```
4. Environment Variables
   
   Create a `.env` file in the project root:
  ```bash
   pip install -r requirements.txt
  ```

## Environment Variables

The project uses environment variables managed by a `.env` file. Set these variables as required:

- `PORT`: Port for running the application (default is 5000).

## Running the Application

1. Start the Flask Server Run the following command to start the server:
   
  ```bash
  python app.py
  ```
2. Accessing the API By default, the server will start at `http://localhost:5000` (or the port specified in your `.env` file).
3. Shutdown the Server To gracefully shut down the server, send a POST request to the `/shutdown` endpoint.

## API Endpoints
1. Chat Endpoint
 - Endpoint: `/chat`
 - method: `POST`
 - Description: Processes a user message and returns the chatbot’s response based on the closest match in the training data.
 - Request Payload:
```json
  {
  "message": "Hello, how are you?"
  }
```

 - Response:
```json
  {
  "response": "I'm here to assist you with any questions."
  }
```
- Error Responses:
  - `400 Bad Request`: If the request payload does not contain a message field.
  - `500 Internal Server Error`: If an unexpected error occurs while processing the request.
 


## Testing with Postman
Setting Up Postman
1. Create a New Collection:
   - Go to Collections in Postman and create a new collection named "Flask Chatbot API".
  
2. Add Requests:
   - Within your collection, add two requests:
      - Chat Request:
         - Method: `POST`
         - URL: `http://localhost:5000/chat`
         - Body: Set to raw JSON and add a sample message:
       
             ```json
             {
           "message": "Hello!"
            }
          ```
      - Expected Response
       ```json
             {
             "response": "I'm here to assist you with any questions."
            }
       ```
       
- Environment Setup in Postman (optional):
  - To simplify requests, you can create an environment variable for the base_url.
  - Go to Environments in Postman and add a new environment with a variable:
  - base_url: `http://localhost:5000`
  - Replace `http://localhost:5000` in your requests with `{{base_url}}/chat` and `{{base_url}}/shutdown`.
       
        
       
### Contact
If you have any questions or suggestions, please feel free to reach out:

- Etiene Essenoh: etienejames5@gmail.com

- GitHub: https://github.com/St80ene
