# Ollama Flask Streaming API

This project is a Flask-based API that allows users to interact with the Ollama chat model. It provides endpoints for generating chat completions and testing responses.

## Features

- Chat completions via the `/chat/completions` endpoint.
- Console output for testing responses via the `/chat/test` endpoint.
- CORS support for cross-origin requests.

## Requirements

- Python 3.6 or higher
- Flask
- Flask-CORS
- Ollama

## Installation

### Important! Follow the link
1. Ollama installation: https://hub.docker.com/r/ollama/ollama
    Then run:
    ```docker exec -it ollama ollama run deepseek-r1:1.5b```

2. Clone the repository:
   ```bash
   git clone https://github.com/Poopa2108/ollama-flask-streaming
   cd ollama-flask-streaming
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```

2. The API will be available at `http://127.0.0.1:5000`.

## API Endpoints

### 1. Chat Completions

- **Endpoint:** `/chat/completions`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "messages": "Your message here"
  }
  ```
- **Response:**
  - Returns a stream of chat responses.

### 2. Test Response

- **Endpoint:** `/chat/test`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "messages": "Your message here"
  }
  ```
- **Response:**
  - Returns 'Ok' and prints the response to the console along with the execution time.

## License

This project is licensed under the MIT License.
