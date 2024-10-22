from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages
from .forms import CreateUser, LoginUser, UpdateProfile
from .models import UserProfile, CreatePost, Category, Comments
from django.contrib.auth import get_user_model
from admin_dash.models import CustomUser


from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash



# users profile
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your views here.
def home(request):
    posts = CreatePost.objects.filter(publish=True)
    categories = Category.objects.all()
    return render(request, 'home.html', {'posts':posts, 'categories': categories})

def register_user(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            user = form.save()
            print(f'This is the error: {type(user), user}')  # Add this line to check what is returned
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = CreateUser()
    
    return render(request, 'users/register.html', {'form': form})



def login_user(request):
    if request.method == 'POST':
        form = LoginUser(request.POST)
        if form.is_valid():
            # authenticate the user 
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                # login user 
                login(request, user)
                messages.success(request, "You're logged in!")
                return redirect('home')
            else:
                messages.info(request, 'Invalid email or password')
    else:
        form = LoginUser()
    return render(request, 'users/login.html', {'form': form})

def update_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':  
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Password ')
                return redirect('home')
        else:
            form = PasswordChangeForm(request.user)
    else:
        messages.error(request, 'You must be logged in')
        return redirect('home')
    return render(request, 'users/update_pass.html', {'form':form})

User = get_user_model()
# Update user profile
def user_profile(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        form = UpdateProfile(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            login(request, current_user)
            messages.success(request, "Your details are saved successfully!")
            return redirect('user_profile')
    else:
        messages.info(request, 'You must be logged in')
        return redirect('home')
    return render(request, 'users/user_profile.html', {'form': form})


# posts
def create_post(request):
    if request.user.is_staff:
        if request.method == 'POST':
            title = request.POST.get('title')
            image = request.FILES.get('image')
            content = request.POST.get('content')
            category_title = request.POST.get('category')
            publish = request.POST.get('publish') == 'on'
            
            # Retrieve the Category instance based on the title
            category = Category.objects.get(title=category_title)
            
            # Check if an image was uploaded, otherwise use the default image
            if not image:
                image = 'Posts/imgs/default.jpg'
            
            
            user = request.user
            post = CreatePost(user=user, title=title, image=image, content=content, category=category, publish=publish)
            post.save()
            messages.success(request, 'Post created!')
            return redirect('home')
        return render(request, 'posts/create_post.html', {})
    else:
        messages.error(request, "Access Denied!")
        return redirect('home')

def post(request, pk):
    post = CreatePost.objects.get(id=pk)
    
    if request.method == 'POST':
        user = request.user
        if user.is_authenticated:
            text = request.POST.get('text')
            comment = Comments(post=post, user=user, text=text)
            comment.save()
            return redirect('post', pk=post.id)   
        else:
            messages.info(request, 'Kindly log in to leave a comment!') 
            return redirect('login')
    comments = Comments.objects.all()
    return render(request, 'posts/post.html', {'post': post, 'comments': comments})


def manage_posts(request):
    user = request.user
    if user.is_staff:
        authors = CustomUser.objects.filter(is_staff=True)
        
        #filter the posts by authors
        author_id = request.GET.get('author')
        if author_id:
            posts = CreatePost.objects.filter(user_id=author_id)
        else: 
            posts = CreatePost.objects.all()
            
        # delete, publish and archive posts
        if request.method == 'POST':
            action = request.POST.get('action')
            post_id = request.POST.get('post_id')
            post = CreatePost.objects.get(id=post_id)
            if action =='delete':
                post.delete()
                messages.success(request, 'Post deleted succeffully!')
            elif action == 'archive':
                post.publish = False
                post.save()
                messages.success(request, 'Post archived succeffully!')
            elif action == 'publish':
                post.publish = True
                post.save()
                messages.success(request, 'Post published succeffully!')
            return redirect('manage_posts')

    else:
        messages.error(request,'Access denied!')
        return redirect('home')
    return render(request, 'posts/manage_posts.html', {'authors': authors, 'posts': posts})

def edit_post(request, pk):
    
    post = CreatePost.objects.get(id=pk)
    user = request.user
    
    if user.is_staff: 
        if request.method == 'POST':
            title = request.POST.get('title')
            image = request.FILES.get('image')
            content = request.POST.get('content')
            category_title = request.POST.get('category')
            publish = request.POST.get('publish') == 'on'
            
            # Retrieve the Category instance based on the title
            category = Category.objects.get(title=category_title)
            
            # Update post fields
            post.title = title
            post.content = content
            post.category = category
            post.publish = publish
            if image:
                post.image = image
            post.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('manage_posts')
    else: 
        messages.error(request, 'Access denied')
        return redirect('home')
    return render(request, 'posts/edit_post.html', {'post': post})

def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'categories/all_categories.html', { 'categories': categories })

def category_posts(request, pk):
    category = Category.objects.get(id=pk)
    posts = CreatePost.objects.filter(category=category)
    return render(request, 'categories/category_posts.html', {'category': category,'posts': posts})