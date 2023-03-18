from django.shortcuts import render

# Create your views here.

from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post
from django.shortcuts import render, get_object_or_404
@login_required
def create_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('index')
    return render(request, 'blog/create_post.html', {'form': form})

def search(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(title__icontains=query)
    return render(request, 'blog/search.html', {'posts': posts, 'query': query})