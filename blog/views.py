import subprocess
from django.shortcuts import render
from .models import Post
from .forms import  PostForm
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


def post_new(request):
    Post.objects.all().delete()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
           # return redirect('post_detail')
            subprocess.Popen(["python3","/home/pi/Docker/NewP/NewProject/tech_scripts.py","-m"])
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_new_dhcp(request):
    subprocess.Popen(["python3","/home/pi/Docker/NewP/NewProject/tech_scripts_dhcp.py","-m"])





