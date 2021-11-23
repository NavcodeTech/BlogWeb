from urllib.parse import quote_plus
from django.shortcuts import render,redirect,get_object_or_404
from .form import *
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
# Create your views here.

def logout_user(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('/')

def home(request):
    context = {'blogs' : BlogModel.objects.all()}
    return render(request, 'home.html' , context)

def login(request):
    return render(request, 'login.html')

def blog_detail(request,slug):
    context = {}
    try:
        blog_objx= BlogModel.objects.filter(slug = slug).first()
        share_string= quote_plus(blog_objx.title)
        context['blog_objx'] = blog_objx
        print(blog_objx)
        print(context)
    except Exception as e:
        print(e)
    return render(request, 'blog_detail.html', context)

def register(request):
    return render(request, 'register.html')

def add_blog(request):
    context = {'form' : BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']

            BlogModel.objects.create(
                user = user, title = title,
                content = content, image = image,
            )
            return redirect('add_blog')

    except Exception as e:
        print(e)

    return render(request, 'add_blog.html', context)

def see_blog(request):
    context={}
    try:
        blog_objs = BlogModel.objects.filter(user = request.user)
        context['blog_objs'] = blog_objs
        print("seeblog",context)
    except Exception as e:
        print(e)
    return render(request, 'see_blog.html', context)

def blog_delete(request,id):
    try:
        blog_obj = BlogModel.objects.get(id=id)

        if blog_obj.user == request.user:
            blog_obj.delete()


    except Exception as e:
        print(e)
    return redirect('/see_blog/')


def blog_update(request, slug):
    context={}
    try:
        blog_obj = BlogModel.objects.get(slug= slug)
        initial_detail = {'content': blog_obj.content}
        form = BlogForm(initial=initial_detail)
        if blog_obj.user != request.user:
            return redirect('/')

        initial_detail = {'content': blog_obj.content}
        form = BlogForm(initial=initial_detail)
        if request.method == 'POST':
            form = BlogForm(request.POST)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']

            BlogModel.objects.create(
                user=user, title=title,
                content=content, image=image
            )
        context['blog_obj'] = blog_obj
        context['form'] = form

    except Exception as e:
        print(e)
    return render(request, 'blog_update.html', context)

def verify(request,token):
    try:
        profile_obj = Profile.objects.filter(token=token).first()

        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
        return redirect('/login/')

    except Exception as e:
        print(e)

    return redirect('/')

def liked_blog(request,user):
    liked = BlogModel.objects.get(title = request.POST.get('blog_title'))
    lik=request.user
    print(lik)
    print(request.user)
    liked.likes.add(request.user)
    return HttpResponseRedirect(reverse('home'))

def liked(request):
    fav = {}
    try:
        blog_fav = BlogModel.objects.filter(likes=request.user)
        fav['blog_fav'] = blog_fav
        print("seeblog", fav)
    except Exception as e:
        print(e)
    return render(request, 'liked.html',fav)

