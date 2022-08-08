import json


class Comments_dao:

    def __init__(self, path: str):
        self.path = path

    def load_json(self) -> list[dict]:
        """агружает данные из JSON и возвращает список словарей"""

        with open(self.path, "r", encoding="utf-8") as file:
            comments = json.load(file)
        return comments

    def get_comments_by_post_id(self, post_id: int) -> list[dict]:
        comments = self.load_json()
        com: list[dict] = [comment for comment in comments if post_id == comment["post_id"]]
        return com
