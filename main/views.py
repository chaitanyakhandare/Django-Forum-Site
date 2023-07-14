
# pass for all: qwer@1234
# "Menlo, Monaco, 'Courier New', monospace, 'cascadia code'"

from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm, PostForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, permission_required
from .models import Post



# Create your views here.

@login_required(login_url="/login") # very easy method!
def home(request):
    posts = reversed(Post.objects.all())    #this we get all posts, and we'll pass this in the context in return
    # posts = Post.objects.all() # remove "reversed" method to get posts from oldest-to-newest 

    # Deleting post
    if request.method == "POST":
        post_id = request.POST.get('post-id')
        user_id = request.POST.get('user-id')
        print(f"PoSt ID  = = = {post_id}")
        print(f"UseR ID  = = = {user_id}")

        if post_id: # for delete user, if we get post_id passed from POST request
            post = Post.objects.filter(id=post_id).first()
            print("SOmething Special= " + str(post))
            if post and (post.author == request.user or request.user.has_perms("main.delete_post")):
                post.delete()

        elif user_id: # for banning user, means: only removing from "default" & "mod" group. And we've also wrote some code in apps.py to add new user in "default" group automatically.
            user = User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    groupDefault = Group.objects.get(name="default")
                    groupDefault.user_set.remove(user)
                except:
                    pass
                try:
                    groupMod = Group.objects.get(name="mod")
                    groupMod.user_set.remove(user)
                except:
                    pass


    return render(request, "main/home.html", {"posts" : posts})



def signup(request):
    if request.method == "POST":
        # it will capture all the data of that fields
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')

    else:
        # it says, if request is not POST, then create the empty form & render it in signup.html
        form = RegisterForm()

    return render(request, "registration/signup.html", {"form": form})



@login_required(login_url="/login") # very easy method!
@permission_required("main.add_post", login_url="/login", raise_exception=True)
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/home')
    else:
        form = PostForm()

    return render(request, "main/create_post.html", {"form": form})

               
