import pytest

from coursework2_source.posts.views import post_dao


class TestPostDao:

    @pytest.fixture
    def post_dao(self):
        return post_dao

    def test_get_all_types(self, post_dao):
        """ Проверяем, верный ли список кандидатов возвращается """
        posts = post_dao.get_all()
        assert type(posts) == list, "возвращается не список"