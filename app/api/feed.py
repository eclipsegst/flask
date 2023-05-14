from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.services.feed_service import feed_list

bp = Blueprint('feed_route', __name__)

@bp.route("/api/feed", methods=['GET'])
def get_feed_list():
    return feed_list()

@bp.route('/api/feed/protected', methods=['GET'])
@jwt_required()
def get_feed():
    # Fetch the feed data for the current user from the database
    # The actual implementation will depend on how your feed data is structured.
    # For now, let's just return a dummy feed.
    feed_data = [
        {"id": 1, "content": "Hello, world!", "posted_by": "test_user"},
        {"id": 2, "content": "Another post", "posted_by": "another_user"}
    ]
    return jsonify(feed_data)
