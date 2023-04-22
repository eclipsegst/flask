from flask import make_response, jsonify
from app.models import Feed

def feed_list():
    feeds = Feed.query.all()
    print(feeds)
    # return make_response(jsonify({'feeds': jsonify(feeds)}), 200)
    return jsonify(feeds)
