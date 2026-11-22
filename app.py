import os

from flask import Flask, jsonify, render_template_string
from redis import Redis
from redis.exceptions import RedisError

app = Flask(__name__)

# Redis connection configuration
redis_client = Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    db=int(os.getenv("REDIS_DB", "0")),
    decode_responses=True,
    socket_connect_timeout=2,
    socket_timeout=2,
    health_check_interval=30
)

# Visitor counter webpage
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visitor Counter | Cloud Computing</title>
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #111827, #1e3a5f);
            font-family: Arial, sans-serif;
            color: white;
        }

        .container {
            width: 90%;
            max-width: 520px;
            padding: 45px 25px;
            text-align: center;
            background: #ffffff12;
            border: 1px solid #ffffff30;
            border-radius: 20px;
        }

        .tag {
            color: #93c5fd;
            font-size: 12px;
            letter-spacing: 2px;
        }

        h1 {
            font-size: 34px;
            margin-bottom: 10px;
        }

        .description {
            color: #cbd5e1;
            line-height: 1.6;
        }

        .counter {
            font-size: 75px;
            font-weight: bold;
            color: #60a5fa;
            margin: 25px 0;
        }

        button {
            padding: 13px 25px;
            border: none;
            border-radius: 8px;
            background: #3b82f6;
            color: white;
            font-size: 15px;
            cursor: pointer;
        }

        button:hover {
            background: #2563eb;
        }

        .footer {
            margin-top: 25px;
            font-size: 12px;
            color: #94a3b8;
        }
    </style>
</head>
<body>
    <div class="container">
        <p class="tag">FLASK + REDIS | CLOUD COMPUTING</p>

        <h1>Visitor Counter</h1>

        <p class="description">
            Welcome! Every page visit is recorded in Redis.
        </p>

        <div class="counter">{{ visitor_count }}</div>

        <p>Total Visitors</p>

        <button onclick="location.reload()">
            Count My Visit
        </button>

        <div class="footer">
            Powered by Flask, Redis and Docker
        </div>
    </div>
</body>
</html>
"""


@app.route("/")
def home():
    try:
        visitor_count = redis_client.incr("visitor_count")

        return render_template_string(
            HTML_PAGE,
            visitor_count=visitor_count
        )

    except RedisError:
        app.logger.exception("Redis visitor counter operation failed")
        return jsonify({
            "error": "Visitor counter is temporarily unavailable"
        }), 503


@app.route("/health")
def health():
    try:
        redis_client.ping()
        return jsonify({
            "status": "ready",
            "redis": "connected"
        }), 200

    except RedisError:
        return jsonify({
            "status": "not_ready",
            "redis": "unavailable"
        }), 503


@app.route("/live")
def live():
    return jsonify({
        "status": "alive"
    }), 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "5000")),
        debug=False
    )
