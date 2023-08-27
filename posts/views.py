from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'index.html')

# blog.html 페이지를 부르는 blog 함수
def blog(request):
    postlist = Post.objects.all()
    for list in postlist :
        print(list)
        print(list.pk)

    return render(request, 'blog.html', {'postlist':postlist})

def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'posting.html', {'post':post})