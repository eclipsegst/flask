from flask import Blueprint, request
from app.services.feed_service import feed_list

feed_route = Blueprint('feed_route', __name__)

@feed_route.route("/api/feed", methods=['GET'])
def get_feed_list():
    return feed_list()
