from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model
from django.db.models import Q
from .forms import CustomAuthenticationForm

User = get_user_model()

def custom_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            users = User.objects.filter(Q(username=username_or_email) | Q(email=username_or_email))
            if users.exists():
                user = users.first()
                if user.check_password(password):
                    login(request, user)
                    return redirect('webapp:index')
            form.add_error(None, 'Неверный логин, email или пароль.')

    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})