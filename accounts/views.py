from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm # Importando o formulário que criamos

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Loga o usuário automaticamente
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})
