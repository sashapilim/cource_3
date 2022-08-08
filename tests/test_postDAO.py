import os

import pytest

from project.posts.views import PostDAO


class TestPostDao:

    @pytest.fixture
    def post_dao(self):
        post_dao = PostDAO(os.path.join("project", "data", "data.json"))
        return post_dao

    def test_get_all_types(self, post_dao):
        """ Проверяем, верный ли список кандидатов возвращается """
        posts = post_dao.get_posts_all()
        assert type(posts) == list, "возвращается не список"
