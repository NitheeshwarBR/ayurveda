#pip install flask , flask_cors
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import subprocess
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains on all routes

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/query', methods=['POST'])
def query():
    data = request.get_json()
    user_input = data.get('input')
    
    curl_command = [
        'curl', '-X', 'POST', '-H', 'Content-Type: application/json',
        '-d', json.dumps({"input": user_input}), 'https://llamastudio.dev/api/cly7lu6sl0006lh086drd215h'
    ]
    
    result = subprocess.run(curl_command, capture_output=True, text=True)
    response = result.stdout
    
    # Polite response handling
    if "I cannot provide an answer" in response:
        response = "I'm sorry, but I don't have information on that topic at the moment. Please try asking about another topic."

    return jsonify({'response': response})

@app.route('/api/feedback', methods=['POST'])
def feedback():
    feedback_data = request.get_json()
    print("Feedback received:", feedback_data)  # Add logging to check what's being received
    return jsonify({'status': 'Feedback received', 'data': feedback_data})

if __name__ == '__main__':
    app.run(debug=True)
