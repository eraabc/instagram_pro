from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import CommentForm
from webapp.models import PostModel


class AddCommentView(LoginRequiredMixin,CreateView):
    form_class = CommentForm

    def form_valid(self, form):
        post = get_object_or_404(PostModel, pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return  reverse('webapp:detail_post', kwargs={'pk': self.kwargs['pk']})