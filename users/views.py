from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #gets the post data
        if form.is_valid():
            form.save() #saves the user
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hesabınız oluşturuldu. Giriş yapabilirsiniz. {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form}) #from a variable form and the value of the form from up there



@login_required
def profile(request):
    if request.method == 'POST':
        u_form =UserUpdateForm(request.POST, instance = request.user) 
        p_form =ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile) #instances suanki kullanıcının bilgilerini form boslugnda gösterir.
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save() #saves the changes if forms are valid
            messages.success(request, f'Hesabın güncellendi.')
            return redirect('profile')
    else:
        u_form =UserUpdateForm(instance = request.user) 
        p_form =ProfileUpdateForm(instance = request.user.profile) #instances suanki kullanıcının bilgilerini form boslugnda gösterir.

    context =  { 
        'u_form': u_form,
        'p_form': p_form

    }                             #passing into template
    return render(request, 'users/profile.html', context)