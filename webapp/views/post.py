from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

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


class UpdatePostView(PermissionRequiredMixin,UpdateView):
    template_name = 'post/update_post.html'
    permission_required = 'webapp.change_post'
    form_class = PostForm
    model = PostModel

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse('webapp:index')


class DeletePostView(PermissionRequiredMixin,DeleteView):
    template_name = 'post/delete_post.html'
    model = PostModel
    success_url = reverse_lazy('webapp:index')

    permission_required = 'webapp.delete_post'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author


class DetailPostView(DetailView):
    template_name = 'post/detail_post.html'
    model = PostModel
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['comments'] = self.object.comments.order_by('-created_at')
        return result