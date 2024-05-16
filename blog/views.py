from django.shortcuts import render
# added by me
from django.http import HttpResponse
# importing the models
from .models import Post
# to switch to class based view
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
# similar to login required but for classes, and will just redirect you to the login page;
# posts to can only be updated by the user who created it
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def home(request):
    # adding the html template
    # can be added either way
    # context = {
    #     'posts': posts
    # }
    # return render(request, 'blog/home.html', context)
    # no need to specify to look inside templates folder as it already knows that is why it is blog/
    # return render(request, 'blog/home.html', {'posts': posts})
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    # defining the model
    model = Post
    # both variables should be named like that
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    # this can be anything as long as it is matching in the html
    context_object_name = 'posts'
    # this is to show the newest (just adding '-')
    ordering = ['-date_posted']

# this is for when clicking on a post to see the details
class PostDetailView(DetailView):
    model = Post
    # this is if we want to rename it if we DONT just go to the html and replace with object
    # context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # this is for creating a new post
    # this creates the form
    fields = ['title', 'content']

    # this is to get the user id of the user who is currently logged in adn add it to the form
    # it also the name of the template will be post_form instead of create/update
    def form_valid(self, form):
        # assigning the currently logged in user to a variable author which matches the form key
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)   

    # to test if the user updating the post is the user that created the post
    #  needed when we use User Passes Test Mixin
    def test_func(self):
        # this means: bring me information about the post that I am trying to update
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # this is a requirement for delete when the post is deleted where the user should be redirected
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About my Blog'})