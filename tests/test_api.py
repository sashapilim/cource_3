import os
from flask import Flask

from coursework2_source import main
from coursework2_source.main import app

import pytest


key_data = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count",
            "pk"}


class Test_api:

    @pytest.fixture
    def app_instance(self):
        app = main.app
        test_client = app.test_client()
        return test_client

    def test_index(self,app_instance):
        result = app_instance.get("/api", follow_redirects=True)

        assert result.status_code == 200, "Неправильный статус "

    def test_post_page(self,app_instance):
        result = app_instance.get("/api/posts", follow_redirects=True)
        assert result.status_code==200,"Неправильный статус "


