import os

from django.shortcuts import render
#from HelloWorld.HelloWorld.settings import STATICFILES_DIRS
from HelloWorld.settings import STATICFILES_DIRS, BASE_DIR
import PaddleGAN.r as r
#from PaddleGAN.r import run
#import paddleGAN
import sys,os

#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#print(BASE_DIR)
#sys.path.append(BASE_DIR)
#import sys

#sys.path.insert(0,os.path.join(BASE_DIR,"G:/python/PP/PaddleGAN/PaddleGAN/ppgan/apps"))

import PaddleGAN.ppgan.apps as p

def ai(request):
    return render(request, "ai.html")
def upload(request):
  if request.method == "GET":
    #return render(request,"ai",locals())
    return render(request, "ai.html")
  if request.method == "POST":
    error = ""
    fp = request.FILES.get("file")
    # fp 获取到的上传文件对象
    if fp:
      path = os.path.join(STATICFILES_DIRS[0],'image/' + 'test.jpg')  # 上传文件本地保存路径， image是static文件夹下专门存放图片的文件夹
      # fp.name #文件名
      #yield = fp.chunks() # 流式获取文件内容
      # fp.read() # 直接读取文件内容
      if fp.multiple_chunks():  # 判断上传文件大于2.5MB的大文件
        # 为真
        file_yield = fp.chunks()  # 迭代写入文件
        with open(path,'wb') as f:
          for buf in file_yield:   # for情况执行无误才执行 else
            f.write(buf)
          else:
            print("大文件上传完毕")
      else:
        with open(path,'wb') as f:
          f.write(fp.read())
        print("小文件上传完毕")


        #models.ImgPath.objects.create(path=('image/' + fp.name))   # image是static文件夹下专门存放图片的文件夹

    else:
      error = "文件上传为空"
      #return render(request,"ai",locals())
      return render(request, "ai.html")
    #return redirect("ai/") # 重定向到首页
    #return render(request, "ai", locals())
    return render(request, "ai.html")
def runs(request):
  #deoldify = p.DeOldifyPredictor()
  #deoldify.run("/static/image/test.jpg")  # 原图片所在路径
  r.run()
  return render(request, "see.html")
def see(request):
  return render(request, "see.html")