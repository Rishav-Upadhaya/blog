from django.shortcuts import render, redirect
from .models import Post, CustomUser
from .forms import add_post
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .my_middleware import RequestTimerMiddleware
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .signals import post_updated

class BlogPostListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

    @method_decorator(cache_page(60 * 15, key_prefix='blog_post_list'))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        import time
        currenttime = time.time()
        time.sleep(2)
        print(time.time()-currenttime)
        return Post.objects.all()


class BlogPostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'posts'


class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = add_post
    login_url = '/login'
    template_name = 'add.html'
    
    def get_success_url(self):
        cache.delete('all_posts')
        cache.delete_pattern('*blog_post_list*')
        return reverse_lazy('add') + '?submitted=True'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submitted'] = 'submitted' in self.request.GET
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        cache.delete('all_posts')
        cache.delete_pattern('*blog_post_list*')
        post_updated.send(sender=self.__class__, instance=form.instance)
        return response


def deletePost(request, pk):
    delpost = Post.objects.get(id = pk)
    title = delpost.title  # Store title before deletion
    delpost.delete()
    # Signal handling is automatic through post_delete signal
    posts = Post.objects.all()
    return render(request, "index.html", {'posts' : posts})

def editPost(request, pk):
    posts = Post.objects.get(id = pk)
    if request.method == 'POST':
        form = add_post(request.POST, instance = posts)
        if form.is_valid():
            form.save()
            # Signal that a post was updated
            post_updated.send(sender=editPost, instance=posts)
            return redirect('post', pk = posts.pk)
    else:
        form = add_post(instance=posts)
    return render(request, 'edit.html', {'form':form, 'post':posts})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password1"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'login.html', {
                "message": "Invalid Credentials."
            })
        
    return render(request, "login.html")

def register(request):
    form = CustomUser()
    if request.method == 'POST':
        form = CustomUser(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            login(request, user)
            return render(request, "login.html")
        else:
            print(form.errors)
            return redirect('register')

    return render(request, "register.html", {'form': form})

def logout_view(request):
    logout(request)
    return render(request, "login.html",{
        "message":"Logged Out Successfully."
    })


def get_cached_posts():
    posts = cache.get('all_posts')
    if not posts:
        posts = Post.objects.all()
        cache.set('all_posts', posts, timeout=60*15)  # Cache for 15 minutes
    return posts

# Create your views here.
# def index(request):
#     posts = Post.objects.all()
#     return render(request, "index.html", {'posts' : posts})

# def post(request, pk):
#     posts = Post.objects.get(id = pk)
#     return render(request, "post.html", {'posts' : posts})


# def add(request):
#     submitted = False
#     if request.method == 'POST':
#         form = add_post(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('/add?submitted=True')
#     else:
#         form = add_post
#         if 'submitted' in request.GET:
#             submitted = True
#     return render(request, 'add.html',{'form' : form, 'submitted' : submitted})
