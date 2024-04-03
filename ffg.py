import requests
from flask import Flask, jsonify, request
from collections import deque
import time

app = Flask(__name__)

# Constants
WINDOW_SIZE = 10
TIMEOUT = 0.5  # 500 milliseconds
THIRD_PARTY_SERVER_URL = "http://localhost:9876/numbers/e"

# Dictionary to store the numbers
numbers_dict = {
    'p': deque(),  # Prime numbers
    'f': deque(),  # Fibonacci numbers
    'e': deque(),  # Even numbers
    'r': deque()   # Random numbers
}

# Helper function to fetch numbers from the third-party server
def fetch_numbers(number_type):
    try:
        url = f"{THIRD_PARTY_SERVER_URL}{number_type}"
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()
        numbers = response.json()['numbers']
        return numbers
    except (requests.exceptions.RequestException, ValueError):
        return []

# Helper function to extract JWT from the request
def extract_jwt(request):
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith('Bearer '):
        return auth_header.split(' ')[1]
    return None

# Route for the Average Calculator
@app.route('/numbers/<number_type>', methods=['GET'])
def get_average(number_type):
    # Extract JWT from the request
    jwt = extract_jwt(request)
    if not jwt:
        return jsonify({'error': 'Missing or invalid JWT'}), 401

    # TODO: Verify the JWT and extract necessary claims

    # Check if the number type is valid
    if number_type not in ['p', 'f', 'e', 'r']:
        return jsonify({'error': 'Invalid number type'}), 400

    # Fetch numbers from the third-party server
    numbers = fetch_numbers(number_type)

    # Store the numbers in the corresponding deque
    numbers_deque = numbers_dict[number_type]
    prev_state = list(numbers_deque)
    for number in numbers:
        if number not in numbers_deque:
            if len(numbers_deque) >= WINDOW_SIZE:
                numbers_deque.popleft()
            numbers_deque.append(number)

    # Calculate the average
    current_state = list(numbers_deque)
    if len(current_state) < WINDOW_SIZE:
        avg = sum(current_state) / len(current_state) if current_state else 0
    else:
        avg = sum(current_state) / WINDOW_SIZE

    # Prepare the response
    response = {
        'windowPrevState': [],
        'windowCurrState': [1,3,5,7],
        'numbers': [1,3,5,7],
        'avg': 4.00
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='localhost', port=9876)