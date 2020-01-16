from django.conf.global_settings import LOGIN_REDIRECT_URL
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import blogs, comments

# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        pswd = request.POST['pass']
        user = auth.authenticate(username=username, password=pswd)
        if user is not None:
            auth.login(request, user)
            return redirect(blog)
        else:
            return redirect(login)
    return render(request, "Creds/login.html")

def signup(request):
    if request.method == "POST":
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass']
        cpassword = request.POST['cpass']

        if password == cpassword:
            if User.objects.filter(username=username).exists() and User.objects.filter(email=email).exists():
                return HttpResponse("user exists")
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname,
                                                username=username, email=email, password=password)
                return redirect(login)

        else:
            HttpResponse("password doesn't match")


    return render(request, "Creds/signup.html")

def logout(request):
    auth.logout(request)
    return redirect(login)

@login_required(login_url='/blog/login')
def blog(request):
    blog = blogs.objects.all()
    blogsdata = {"blogs": blog}
    return render(request, "Blog/bloghome.html", blogsdata)

@login_required(login_url='/blog/login')
def detailview(request,id):
    bid = blogs.objects.get(id=id)
    cmnt = comments.objects.filter(post=bid)
    u = User.objects.get(username=request.user.username)
    if request.method =='POST':
        cmt = request.POST['comment']
        print(bid," ",u," ",cmt)
        co = comments(comment_content=cmt, owner_username=u, post=bid)
        co.save()

    context = {"blog": bid, "cmnts": cmnt}
    return render(request, "Blog/detailview.html", context)
@login_required(login_url='/blog/login')
def addblog(request):
    if request.method =="POST":
        un = User.objects.get(username=request.user.username)
        title = request.POST['title']
        blo = request.POST['blog']
        print(title," space", blo)
        b = blogs(post_title=title, post_content=blo, owner_email=un)
        b.save()

        return redirect(blog)


    return render(request, "Blog/addblog.html")
@login_required(login_url='/blog/login')
def editview(request,id):
    blogid = blogs.objects.get(id=id)
    context = {"blog":blogid}
    un = User.objects.get(username=request.user.username)
    if request.method =="POST":
        pid = request.POST['id']
        utitle = request.POST['utitle']
        ublog = request.POST['ublog']
        print(pid," ",utitle," space ", ublog)
        u = blogs(id=pid, post_title=utitle, post_content=ublog, owner_email=un)
        u.save()
        return redirect(blog)
    else:
        return render(request, "Blog/updateblog.html", context)


    return render(request, "Blog/updateblog.html", context)
@login_required(login_url='/blog/login')
def delete(request,id):
    b = blogs.objects.get(id=id)
    b.delete()
    return redirect(blog)

def deletecom(request, id):
    cm = comments.objects.get(id=id)
    cm.delete()
    return redirect(blog)

