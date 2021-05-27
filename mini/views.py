from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm,LoginForm,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post
from django.contrib.auth.models import Group
from .forms import ImageForm
from .models import Image
# Create your views here.
#home
def Home(request):
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    form = ImageForm()
    img = Image.objects.all()
    posts = Post.objects.all()
    return render(request,'home.html',{'posts':posts,'img': img, 'form': form})

"""def ho(request):
    if request.method=="POST":
       form = ImageForm(request.POST,request.FILES)
       if form.is_valid():
          form.save()
    form = ImageForm()
    img = Image.objects.all
    return render(request, 'home.html', {'img': img, 'form': form})"""

#Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        form = ImageForm()
        img = Image.objects.all()
        posts=Post.objects.all()
        user=request.user
        full_name = user.get_full_name()
        gps=user.groups.all()
        return render(request,'dashboard.html',{'posts':posts,
                'full_name':full_name,'groups':gps,'img': img, 'form': form })
    else:
        return HttpResponseRedirect('/login/')









#About
def About(request):
    return render(request,'about.html')

#Contact
def contact(request):
    return render(request,'contact.html')

"""#Dashboard
def dashboard(request):
    if request.user.is_authenticated:
     posts=Post.objects.all()
     user=request.user
     full_name = user.get_full_name()
     gps=user.groups.all()
     return render(request,'dashboard.html',{'posts':posts,
                'full_name':full_name,'groups':gps })
    else:
     return HttpResponseRedirect('/login/')
"""
#logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

#signup
def user_signup(request):
    if request.method == "POST":
      form=SignUpForm(request.POST)
      if form.is_valid():
       messages.success(request,'congratulation you have become an author')
       user=form.save()
       group = Group.objects.get(name="Author")
       user.groups.add(group)
    else:
     form=SignUpForm()
    return render(request,'signup.html',{'form':form})

"""#login
def user_login(request):
    if not request.user.is_authenticated:
      if request.method=="POST":
        form=LoginForm(request=request,data=request.POST)
        if form.is_valid():
          uname=form.cleaned_data['username']
          upass = form.cleaned_data['password']
          user=authenticate(username=uname,password=upass)
          if user is not None:
              login(request,user)
              messages.success(request,'login successfully')
              return HttpResponseRedirect('/dashboard/')
      else:
       form = LoginForm()
      return render(request,'login.html',{'form':form})
    else:
       form = LoginForm()
    return HttpResponseRedirect('/dashboard/')"""

def user_login(request):
    if not request.user.is_authenticated:
      if request.method=="POST":
        form=LoginForm(request=request,data=request.POST)
        if form.is_valid():
          uname=form.cleaned_data['username']
          upass = form.cleaned_data['password']
          user=authenticate(username=uname,password=upass)
          if user is not None:
              login(request,user)
              messages.success(request,'login successfully')
              return HttpResponseRedirect('/dashboard/')
      else:
       form = LoginForm()
      return render(request,'login.html',{'form':form})
    else:
       form = LoginForm()
    return HttpResponseRedirect('/dashboard/')

#Add New POst
def add_post(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form=PostForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title=title,desc=desc)
                pst.save()
                form=PostForm()
        else:
            form=PostForm()
        return render(request,'addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

# Update POst
def update_post(request, id):
    if request.user.is_authenticated:
      if request.method == "POST":
         pi =Post.objects.get(pk=id)
         form =PostForm(request.POST, instance=pi)
         if form.is_valid():
             form.save()
      else:
          pi = Post.objects.get(pk=id)
          form=PostForm(instance=pi)
      return render(request, 'updatepost.html',{'form':form})
    else:
      return HttpResponseRedirect('/login/')

# Delet POst
def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method =="POST":
            pi=Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')

"""
def ho(request):
    if request.method=="POST":
       form = ImageForm(request.POST,request.FILES)
       if form.is_valid():
          form.save()
    form = ImageForm()
    img = Image.objects.all
    return render(request, 'home.html', {'img': img, 'form': form})"""