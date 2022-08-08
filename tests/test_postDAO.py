import os

import pytest
# "../data/data.json"
# "data", "data.json"
from coursework2_source.posts.views import PostDAO


class TestPostDao:

    @pytest.fixture
    def post_dao(self):
        post_dao = PostDAO(os.path.join("coursework2_source","data", "data.json"))
        return post_dao

    def test_get_all_types(self, post_dao):
        """ Проверяем, верный ли список кандидатов возвращается """

        posts = post_dao.get_posts_all()
        assert type(posts) == list, "возвращается не список"

    def test_get_by_id(self, post_dao):
        """ Проверяем правильность pk  кандидатов возвращаются при запросе"""
        posts = post_dao.get_posts_all()

        correct_pk = {1, 2, 3, 4, 5, 6, 7, 8}
        pk = set([post["pk"] for post in posts])
        assert pk == correct_pk, "Не совпадает получение pk"

    def test_get_by_pk_none(self, post_dao):
        post = post_dao.get_post_by_pk(89)
        assert post is None, "Нет такого пользолвателя"

    def test_search_is_correct(self, post_dao):
        """Проверка поиска поста"""
        posts = post_dao.search_for_posts("ржавые")
        assert type(posts) == list, "Вернулся не список"

    def test_search_is_correct_not_found(self, post_dao):
        """Проверка что поста такого нет"""
        posts = post_dao.search_for_posts("456745")
        assert posts == [], "Ничего не найдено"
