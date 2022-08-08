import os
from flask import Flask

from coursework2_source import main
from coursework2_source.main import app

import pytest


key_data = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count",
            "pk"}


class Test_api:



    def test_index(self):
        result = app.test_client().get("/api", follow_redirects=True)

        assert result.status_code == 200, "Неправильный статус "

    def test_post_page(self,):
        result = app.test_client().get("/api/posts", follow_redirects=True)
        assert result.status_code==200,"Неправильный статус "

    def test_page_post_pk(self):
        result = app.test_client().get("/api/posts/1", follow_redirects=True)
        assert result.status_code==200
        assert type(result.json)==dict,"несоответствующий тип данных"

    def test_page_found_name(self):
        result = app.test_client().get("/api/posts/Sasha", follow_redirects=True)
        assert result.status_code==404

    def test_page_user(self):
        result = app.test_client().get("/api/posts/Leo", follow_redirects=True)
        assert result.status_code==200
        assert type(result.json)==list,"несоответствующий тип данных"