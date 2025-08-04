from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DeleteView

from webapp.forms import CommentForm
from webapp.models import PostModel, Comment


class AddCommentView(LoginRequiredMixin,CreateView):
    form_class = CommentForm

    def form_valid(self, form):
        post = get_object_or_404(PostModel, pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return  reverse('webapp:detail_post', kwargs={'pk': self.kwargs['pk']})


class DeleteCommentView(PermissionRequiredMixin,DeleteView):
    model = Comment
    permission_required = 'webapp.delete_comment'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:detail_post', kwargs={'pk': self.object.post.pk})