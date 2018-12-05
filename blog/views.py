import subprocess
from django.shortcuts import render
from .models import Post
from .models import ConfigInfo
from .forms import  PostForm
from .forms import  ConfigInfoForm
from django.shortcuts import redirect



# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

#def post_detail(request):
 #   post = Post.objects.all()
  #  return render(request, 'blog/post_detail.html', {'post': post})

def post_L(request):
    post = Post.objects.all()
    return render(request, 'blog/post_L.html', {'post': post})

def post_list_two(request):
    return render(request, 'blog/post_list_two.html',{})

def post_list_four(request):
    from .models import dhcp
    from .forms import dhcpForm
    dhcp.objects.all().delete()
    if request.method=="POST":
        dhcp=dhcpForm(request.POST)
        if dhcp.is_valid():
            dhcpForm=dhcp.save(commit=False)
            dhcpForm.save()
            subprocess.Popen(["python3", "/home/pi/Docker/NewP/NewProject/wifi_dhcp.py","-m"])
    else:
        dhcp=dhcpForm()
    return render(request, 'blog/post_edit_two.html',{'dhcp':dhcp})


def post_list_three(request):
    from .models import ConfigInfo
    ConfigInfo.objects.all().delete()
    if request.method =="POST":
       form =ConfigInfoForm(request.POST)
       if form.is_valid():
           ConfigInfo=form.save(commit=False)
           ConfigInfo.save()
           subprocess.Popen(["python3", "/home/pi/Docker/NewP/NewProject/tech_scripts_wifi.py","-m"])
    else:
        form=ConfigInfoForm()
    return render(request, 'blog/post_edit_wifi.html', {'form':form})


def post_new(request):
    Post.objects.all().delete()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
           # return redirect('post_detail')
            subprocess.Popen(["python3","/home/pi/Docker/NewP/NewProject/tech_scripts_eth.py","-m"])
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_new_dhcp():
    subprocess.Popen(["python3","/home/pi/Docker/NewP/NewProject/tech_scripts_dhcp_eth.py","-m"])





