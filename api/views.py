from flask import Blueprint, jsonify
import logging

from coursework2_source.loggings import logger_api
from coursework2_source.posts.views import post_dao

bluepint_api = Blueprint("bluepint_api", __name__)


@bluepint_api.route("/api")
def index():
    return "Hello"


@bluepint_api.route("/api/posts")
def get_all_post():
    all_posts:list[dict] = post_dao.get_posts_all()
    logger_api.warning("Запрошены все посты")
    return jsonify(all_posts)


@bluepint_api.route("/api/posts/<int:postid>")
def get_post_id(postid):
    post:list[dict] = post_dao.get_post_by_pk(postid)
    logger_api.warning(f"Запрошен пост {postid}")
    return jsonify(post)
