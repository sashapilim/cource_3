from flask import Blueprint, render_template, request

from .dao.comments_dao import Comments_dao
from .dao.posts_dao import PostDAO
from project.config import DATA_PATH_POSTS, data_path_comments

post_blueprint = Blueprint("post_blueprint", __name__, template_folder="templates")

post_dao = PostDAO(DATA_PATH_POSTS)
comments_dao = Comments_dao(data_path_comments)


@post_blueprint.route("/")
def page_post_all():
    post: list[dict] = post_dao.get_posts_all()
    return render_template("index.html", posts=post)


@post_blueprint.route("/posts/<int:pk>")
def odinary_post_page(pk):
    post: list[dict] = post_dao.get_post_by_pk(pk)
    comments: list[dict] = comments_dao.get_comments_by_post_id(pk)
    lenght: int = len(comments)
    return render_template("post.html", post=post, comments=comments, leng=lenght)


@post_blueprint.route("/search/")
def search_post():
    requests: str = request.args.get("s")
    posts: list[dict] = post_dao.search_for_posts(requests)
    len_posts: int = len(posts)
    if requests == "":
        posts: list = []
    return render_template("search.html", posts=posts, requests=requests, len_posts=len_posts)


@post_blueprint.route("/users/<username>")
def page_user(username):
    post: list[dict] = post_dao.get_posts_by_user(username)
    return render_template("user-feed.html", posts=post, user_name=username)
