from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model
from django.db.models import Q
from django.urls import reverse
from django.views.generic import CreateView

from .forms import CustomAuthenticationForm, MyUserCreationForm

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