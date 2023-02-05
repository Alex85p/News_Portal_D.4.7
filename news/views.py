
from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news_list.html'
    context_object_name = 'posts'

class PostDetail(DetailView):

    model = Post
    template_name = 'post.html'
    context_object_name = 'post'