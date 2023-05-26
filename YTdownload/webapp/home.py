from flask import Blueprint , render_template ,request , send_file
from pytube import YouTube



home = Blueprint("home", __name__)
# 用取出來的網址 創一個新的YouTube的物件


#[]是一個list的型態，list就是裡面可以存放資料
@home.route("/",methods=["GET","POST"])
def download_youtube_video():
  #放問的時候是GET(200是成功的意思)
  #送出來的時候是POST
  if request.method == "POST":
    #把用戶在前端這個網頁輸入的網址取出來
    video_url = request.form.get("downloadUrl")
    
    #用去出來的網址創一個溪的youtube的建物
    youtube_video_object = YouTube(video_url, use_oauth=True)
    
    
    
    #下載影片到伺服器
    get_video = youtube_video_object.streams.get_highest_resolution()
    
    #讓用戶端下載，選擇存放路徑
    return send_file(get_video.download(), as_attachment=True)
    #如果不適POST那他就是->GET
  else:
    
    return render_template("home.html")