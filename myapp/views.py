from .models import Blog
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .forms import ContactForm
from django.views.generic.detail import DetailView

# Create your views here.
class Home(TemplateView):
    template_name = 'myapp/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_data'] = Blog.objects.all()
        return context

class Form(CreateView):
    form_class = ContactForm
    template_name = 'myapp/contact.html'
    success_url = '/form/'

class FullBlog(DetailView):
    model = Blog
    template_name = 'myapp/fullblog.html'