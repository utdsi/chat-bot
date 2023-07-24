from flask import Flask, request, jsonify
from flask_cors import CORS

import openai




app = Flask(__name__)
CORS(app)
openai.api_key = "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"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data['content']

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message},
        ]
    )
    gpt3_response = response['choices'][0]['message']['content']

    return jsonify({'message': gpt3_response}), 200

if __name__ == "__main__":
    app.run(debug=True)