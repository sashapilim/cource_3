import json
from json import JSONDecodeError


class PostDAO:

    def __init__(self, path: str):
        """ При создании экземпляра DAO нужно указать путь к файлу с данными"""
        self.path = path

    def load_data(self) -> list[dict]:
        """ Загружает данные из файла и возвращает обычный list"""

        with open(self.path, 'r', encoding='utf-8') as file:
            posts_data = json.load(file)

        return posts_data

    def get_posts_all(self) -> list[dict]:
        """ Возвращает список со всеми данными"""
        posts = self.load_data()
        return posts

    def get_post_by_pk(self, pk: int) -> list[dict]:
        posts = self.load_data()
        for post in posts:
            if pk == post["pk"]:
                return post
            if type(pk) != int:
                raise TypeError("pk должен быть числом")

    def get_posts_by_user(self, user_name: str) -> list[dict]:
        """возвращает посты определенного пользователя."""
        if type(user_name) != str:
            raise TypeError("user_name должен иметь тип строковых данных")
        posts = self.load_data()
        post = [post for post in posts if user_name in post["poster_name"]]
        return post

    def search_for_posts(self, query: str) -> list[dict]:
        if type(query) != str:
            raise TypeError("query должен быть строкой")
        posts = self.load_data()
        post = [post for post in posts if query.lower() in post["content"].lower()]
        return post
