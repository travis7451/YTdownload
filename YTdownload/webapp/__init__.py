from flask import Flask
from .home import home



def create_web_app():
  # 創造一個flask的物件 叫做app
  app = Flask(__name__)
  
  

  #註冊藍圖
  app.register_blueprint(home,url_prefix="/")

  
  
  return app
