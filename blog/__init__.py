from flask import Flask

def create_app():
    # __name__: 檔案名稱
    app = Flask(__name__)
    # SECRET_KEY 的作用?
    app.config["SECRET_KEY"] = "salkdjkalsjdlakq310948uc89"


    return app


