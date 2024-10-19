from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from .models import CustomUser


# Create your views here.
@login_required
def dash(request):
    user = request.user
    if user.is_active and user.is_staff:
        return render(request, 'dash.html', {})
    else:
        pass

@login_required
def reg_author(request):
    user = request.user
    if user.is_superuser:
        if request.method == 'POST':
            form = CustomCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success('Author registered Successfully!')
                return redirect('dash')
        else: 
            form = CustomCreationForm()
    else:
        messages.error(request, "Not allowed")
        return redirect('home')
    return render(request, 'users/reg_author.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out!')
    return redirect('home')


@login_required
def manage_authors(request):
    user = request.user
    if user.is_superuser:
        authors = CustomUser.objects.filter(is_staff=True)
        # delete author
        if request.POST:
            num = request.POST['num']
            deleted_author = CustomUser.objects.filter(id=num)
            deleted_author.delete()
            messages.success(request, 'Deleted Succeffully!')
            return redirect('manage_authors')
    return render(request, 'users/manage_authors.html', {'authors': authors})

