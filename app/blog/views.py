from django.shortcuts import render
from django.views import generic

from .models import *

# Create your views here.

class BlogView(generic.TemplateView):
    template_name = 'blog/blog.html'
    
    
class BlogPostAdd(generic.CreateView):
    template_name = 'blog/post.html'
    success_url = '/'
    form_class = Post
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    