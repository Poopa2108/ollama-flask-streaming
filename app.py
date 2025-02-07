from flask import Flask, request, jsonify, Response, stream_with_context
from flask_cors import CORS  # Import CORS
from ollama import chat
import threading
import time  # Import the time module

app = Flask(__name__)
CORS(app)  # Enable CORS for the app

### Output to API
@app.route('/chat/completions', methods=['POST'])
def chat_api():
    user_message = request.json.get('messages')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    def generate_response():
        stream = chat(
            model='deepseek-r1:1.5b',
            messages=[{'role': 'user', 'content': user_message}],
            stream=True,
        )

        for chunk in stream:
            yield chunk['message']['content']

    return Response(stream_with_context(generate_response()), mimetype='text/plain')

### Output to console
@app.route('/chat/test', methods=['POST'])
def test_generate_response():
    user_message = request.json.get('messages')
    
    start_time = time.time()  # Record the start time

    def print_response():
        stream = chat(
            model='deepseek-r1:1.5b',
            messages=[{'role': 'user', 'content': user_message}],
            stream=True,
        )

        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)

    # Run the print_response function in a separate thread
    threading.Thread(target=print_response).start()
    
    # Wait for the response to finish before calculating the execution time
    threading.Thread(target=lambda: print(f"Execution time: {time.time() - start_time:.2f} seconds")).start()
    
    return 'Ok'

if __name__ == '__main__':
    app.run(debug=True)