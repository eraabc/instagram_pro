from urllib.parse import urlencode

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView

from webapp.forms import PostForm, SearchForm
from webapp.models import PostModel


class IndexView(ListView):
    model = PostModel
    template_name = 'post/index.html'

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']

    def get_queryset(self):
        queryset = super().get_queryset().all()

        if self.search_value:
            queryset = PostModel.objects.filter(
                Q(author__email__icontains=self.search_value) | Q(author__username__icontains=self.search_value) | Q(
                    author__first_name__icontains=self.search_value))
        return queryset

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['search_form'] = self.form
        if self.search_value:
            result['query'] = urlencode({'search': self.search_value})
            result['search'] = self.search_value
        return result


class CreatePostView(LoginRequiredMixin,CreateView):
    form_class = PostForm
    template_name = 'post/create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:index')