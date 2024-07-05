from flask import Flask

def create_app():
    # __name__: 檔案名稱
    app = Flask(__name__)
    # SECRET_KEY 的作用?
    app.config["SECRET_KEY"] = "salkdjkalsjdlakq310948uc89"

    from .views import views
    from .auth import auth


    # url_prefix: 就是這些路徑的前綴
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(views, url_prefix="/")

    return app


