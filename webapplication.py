from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Your code here to fetch or generate the data
    data = {'name': 'John', 'age': 30, 'city': 'New York'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)