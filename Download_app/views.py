from django.shortcuts import redirect, render
from pytube import YouTube
from django.contrib import messages
import os
from instascrape import Post,Reel
import os
import time
# Create your views here.

mainurl=""
def home(request):
    return render(request,'home.html')

def youdou(request):
    global mainurl
    if request.method=='POST':
        url=request.POST['url']
        if url.startswith('https://youtu.be/') is True:
            crt_url=url[17:]
            mainurl="https://youtu.be/"+crt_url
            srcs="https://www.youtube.com/embed/"+crt_url+"?rel=0"
            return render(request,'youdou.html',{'srcs':srcs})
        elif url.startswith('https://www.youtube.com/') is True:
            crt_url=url[32:]
            mainurl="https://youtu.be/"+crt_url
            srcs="https://www.youtube.com/embed/"+crt_url+"?rel=0"
            return render(request,'youdou.html',{'srcs':srcs})
        elif url.startswith('https://www.youtube.com/shorts/') is True or url.startswith('https://youtube.com/shorts/') is True:
            mainurl=url
            return render(request,'youdou.html',{'check':'val'})
        else:
            messages.error(request,"Please Provide Valide URL!!")
            return render(request,'youdou.html',{'type':'error','t1':'success','t2':'error'})
    return render(request,'youdou.html')

def youfun(request):
    global mainurl
    if request.method=='POST':
        quality=request.POST['droplis']
        Folder_name=os.path.expanduser("~")+"\Downloads"
        print(quality)
        print(mainurl)
        yt = YouTube(mainurl)
        if (quality == str(0)):
            select = yt.streams.get_by_itag(22)
            select.download(Folder_name)
            messages.success(request,f'Download is Started...\nVideo saved in {Folder_name}')
            return render(request,'youdou.html',{'type':'success','t1':'success','t2':'error'})
        elif (quality == str(1)):
            select = yt.streams.get_by_itag(18)
            select.download(Folder_name)
            messages.success(request,'Download is Started...')
            messages.success(request,f'Download is Started...\nVideo saved in {Folder_name}')
            return render(request,'youdou.html',{'type':'success','t1':'success','t2':'error'})
        elif (quality == str(2)):
            select = yt.streams.get_by_itag(17)
            select.download(Folder_name)
            messages.success(request,'Download is Started...')
            messages.success(request,f'Download is Started...\nVideo saved in {Folder_name}')
            return render(request,'youdou.html',{'type':'success','t1':'success','t2':'error'})
        elif (quality == str(3)):
            select = yt.streams.get_by_itag(251)
            select.download(Folder_name)
            messages.success(request,'Download is Started...')
            messages.success(request,f'Download is Started...\nVideo saved in {Folder_name}')
            return render(request,'youdou.html',{'type':'success','t1':'success','t2':'error'})
        else:
            messages.error(request,'Select the Quality of the video!!')
            return render(request,'youdou.html',{'type':'error','t1':'success','t2':'error'})
    return render(request,'youdou.html')


def instadou(request):
    val='yes'
    return render(request,'instadou.html',{'start':val})

def insvdofun(request):
    if request.method=='POST':
        url=request.POST['vdourl']
        if url.startswith('https://www.instagram.com/') is True:
            SESSIONID="52155423085%3AR7aszvhNCJ5aRr%3A28"#52155423085%3AR7aszvhNCJ5aRr%3A28
            headers={
                "Users-Agent":"Mozilla/5.0 (Windows NT 10.0; WIN64; x64) AppleWebKit/537.36(KHTML,link Gecko) Chrome/79.9.3945.75 Safari/537.36 Edg/79.0.309.43",
                "cookie":f'sessionID = {SESSIONID}'
            }
            Folder_name=os.path.expanduser("~")+"\Downloads"
            google_reel=Reel(url)
            google_reel.scrape(headers=headers)
            google_reel.download(fp=Folder_name+f"/reel{int(time.time())}.mp4")
            messages.success(request,f'Download is Started...\n Video saved in {Folder_name}')
            val='yes'
            return render(request,'instadou.html',{'start':val,'type':'success','t1':'success','t2':'error'})
        else:
            val='yes'
            messages.error(request,'Please Provide Correct URL!!!')
            return render(request,'instadou.html',{'vdo':val,'type':'error','t1':'success','t2':'error'})
    else:
        val='yes'
        return render(request,'instadou.html',{'vdo':val})

def inspicfun(request):
    if request.method=='POST':
        url=request.POST['picurl']
        if url.startswith('https://www.instagram.com/') is True:
                SESSIONID="52155423085%3AR7aszvhNCJ5aRr%3A28"#"45311690968%3AkTfqFW2eM9nva1%3A18"
                headers={
                    "Users-Agent":"Mozilla/5.0 (Windows NT 10.0; WIN64; x64) AppleWebKit/537.36(KHTML,link Gecko) Chrome/79.9.3945.75 Safari/537.36 Edg/79.0.309.43",
                    "cookie":f'sessionID = {SESSIONID}'
                }
                Folder_name=os.path.expanduser("~")+"\Downloads"
                pos=Post(url)
                pos.scrape(headers=headers)
                pos.download(fp=Folder_name+f"/post{int(time.time())}.png")
                messages.success(request,f'Download is Started...\n Image saved in {Folder_name}')
                val='yes'
                return render(request,'instadou.html',{'start':val,'type':'success','t1':'success','t2':'error'})
        else:
            val='yes'
            messages.error(request,'Please Provide Correct URL!!!')
            return render(request,'instadou.html',{'pic':val,'type':'error','t1':'success','t2':'error'})
    else:
        val='yes'
        return render(request,'instadou.html',{'pic':val})