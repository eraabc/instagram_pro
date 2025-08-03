from urllib.parse import urlencode

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model
from django.db.models import Q
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from webapp.forms import SearchForm
from .forms import CustomAuthenticationForm, MyUserCreationForm, MyUserChangeForm

User = get_user_model()

def custom_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('webapp:index')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})

class RegisterView(CreateView):
    template_name = 'registration.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())


    def get_success_url(self):
        next = self.request.GET.get('next')
        if not next:
            next = self.request.POST.get('next')
        if not next:
            next = reverse('webapp:index')
        return next


class ProfileView(DetailView):
    model = User
    template_name = 'profile/user_profile.html'
    context_object_name = 'user_obj'


    def get_context_data(self, **kwargs):
        posts = self.object.posts.order_by('-id')
        kwargs['posts'] = posts
        return super().get_context_data(**kwargs)


class ProfileListView(ListView):
    model = User
    template_name = 'profile/profile_list.html'
    context_object_name = 'users_obj'

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
            queryset = User.objects.filter(
                Q(email__icontains=self.search_value) | Q(
                    username__icontains=self.search_value) | Q(
                    first_name__icontains=self.search_value))
        return queryset

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['search_form'] = self.form
        if self.search_value:
            result['query'] = urlencode({'search': self.search_value})
            result['search'] = self.search_value
        return result


class ProfileUpdateView(PermissionRequiredMixin,UpdateView):
    model = get_user_model()
    form_class = MyUserChangeForm
    template_name = 'profile/update_profile.html'
    context_object_name = 'user_obj'

    def has_permission(self):
        return  self.get_object() == self.request.user

    def get_success_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.object.pk})
