from flask import request, jsonify, Flask


app = Flask(__name__)


@app.route('/')
def hello():
    print(f'request ip address: {request.remote_addr}')
    return jsonify({'ip': request.remote_addr}), 200


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
