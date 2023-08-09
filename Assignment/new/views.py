
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from .models import User
from rest_framework.authtoken.models import Token

#view for user registration
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Registered successfully!')
            return redirect('registration')
    else:
        form = RegistrationForm()
    return render(request, 'index.html', {'form': form})

#view for delete user by searching
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, 'User deleted successfully!')
    return redirect('registration')

#view for delete
def search_and_delete_by_name(request):
    if request.method == 'POST':
        search_name = request.POST.get('search_name')
        users = User.objects.filter(username__icontains=search_name)
        return render(request, 'index.html', {'users': users})
    return redirect('registration')

#view for search and update
def search_and_update_by_name(request):
    if request.method == 'POST':
        search_name = request.POST.get('search_name')
        user = get_object_or_404(User, username=search_name)
        if request.method == 'POST':
            form = RegistrationForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'User updated successfully!')
                return redirect('registration')
        else:
            form = RegistrationForm(instance=user)
        return render(request, 'update_user.html', {'form': form})
    return redirect('registration')

#view for generate access token
def generate_access_token(request, user_id):
    user = get_object_or_404(User, id=user_id)
    token, created = Token.objects.get_or_create(user=user)
    messages.success(request, f'Access token generated: {token.key}')
    return redirect('registration')