from flask import Flask, jsonify
app = Flask(__name__)

messages = [
    {
        'id': 1,
        'message': u'Hello World',
    },
    {
        'id': 2,
        'message': u'Hello Docker',
    },
]

@app.route('/api/v1/messages', methods=['GET'])
def get_tasks():
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
