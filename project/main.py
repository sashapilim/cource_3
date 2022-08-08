from flask import Flask

from project.api.views import bluepint_api
from project.posts.views import post_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(post_blueprint)
app.register_blueprint(bluepint_api)


@app.errorhandler(404)
def page_error_404(error):
    return f"Такой страницы нет {error}", 404


@app.errorhandler(500)
def page_error_500(error):
    return f"На сервере ошибка - {error}", 500

# response = app.test_client().get('/api/posts')
# print(response.status_code)
if __name__ == "__main__":
    app.run(debug=True)