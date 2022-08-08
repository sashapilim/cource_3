from flask import Blueprint, jsonify, abort
import logging

from coursework2_source.loggings import logger_api
from coursework2_source.posts.views import post_dao

bluepint_api = Blueprint("bluepint_api", __name__)


@bluepint_api.route("/api/")
def index():
    return "Hello"


@bluepint_api.route("/api/posts/")
def get_all_post():
    all_posts: list[dict] = post_dao.get_posts_all()
    logger_api.warning("Запрошены все посты")
    return jsonify(all_posts), 200


@bluepint_api.route("/api/posts/<int:postid>")
def get_post_id(postid):
    post: list[dict] = post_dao.get_post_by_pk(postid)
    if post is None:
        logger_api.warning(f"Обращение к несуществующему посту {postid}")
        abort(404)
    logger_api.warning(f"Запрошен пост {postid}")
    return jsonify(post), 200


@bluepint_api.errorhandler(404)
def api_error_404(error):
    return jsonify({"error": str(error)}), 404
