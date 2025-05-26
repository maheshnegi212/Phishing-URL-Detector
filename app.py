from flask import Flask, request, jsonify
from predict import predict_url

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    url = request.json['url']
    result = predict_url(url)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
