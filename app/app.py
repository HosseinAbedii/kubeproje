from flask import Flask, jsonify
import socket
import uuid
import time

app = Flask(__name__)

INSTANCE_UUID = str(uuid.uuid4())[:8]
START_TIME = time.strftime('%Y-%m-%d %H:%M:%S')

@app.route('/instance-id')
def get_instance_id():
    return jsonify({
        "instance_id": socket.gethostname(),
        "short_id": INSTANCE_UUID,
        "started_at": START_TIME
    })

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
