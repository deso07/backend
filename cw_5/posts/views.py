from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Post, Thread
from .forms import PostForm

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts_list.html', {'posts': posts})

def login_view(request):
    if request.method == 'POST':
        # Получаем данные из POST-запроса
        username = request.POST.get('username')  # Используйте .get() вместо []
        password = request.POST.get('password')  # Используйте .get() вместо []

        # Проверяем, что данные были отправлены
        if not username or not password:
            return render(request, 'posts/login.html', {'error': 'Please provide both username and password'})

        # Аутентификация пользователя
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Замените 'home' на нужный URL
        else:
            return render(request, 'posts/login.html', {'error': 'Invalid credentials'})
    
    # Если метод GET, просто отображаем форму
    return render(request, 'posts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts_list.html', {'posts': posts})

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'posts/my_posts.html', {'posts': posts})

@login_required
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/post_detail.html', {'post': post})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts')  # Замените 'posts' на нужный URL
    else:
        form = PostForm()
    return render(request, 'posts/post_create.html', {'form': form})

@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user == post.author or request.user.is_superuser:
        post.delete()
    return redirect('posts_list')