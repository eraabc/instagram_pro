from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import PostForm


# Create your views here.
def index(request):
    return render(request,'index.html')


class CreatePostView(LoginRequiredMixin,CreateView):
    form_class = PostForm
    template_name = 'post/create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:index')