from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse
from django.views.generic import CreateView, ListView

from webapp.forms import PostForm, SearchForm
from webapp.models import PostModel


class IndexView(ListView):
    model = PostModel
    template_name = 'post/index.html'
    ordering = ['-id']
    context_object_name = 'posts'


class CreatePostView(LoginRequiredMixin,CreateView):
    form_class = PostForm
    template_name = 'post/create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:index')