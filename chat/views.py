from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from chat.forms import *
from chat.models import *


def registrationPage(request):
    if request.user.is_authenticated:
        return HttpResponse("HELLO")
    else :
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                print(12)
                return redirect(loginPage);
        context = {
            'form': form
        }
        return render(request, "forms/registration.html", context)

# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else :
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                print("12312")
                return redirect(mainPage)
            else :
                messages.info(request,'Username is not found')
        context = {

        }
        return render(request, 'forms/login.html', context)

@login_required(login_url='login')
def mainPage(request):
    friends = Friends.objects.all().filter(id1=request.user)

    context = {"friends":friends}
    return render(request, "pages/main.html", context)


@login_required(login_url='login')
def allUsersPage(request):
    users = User.objects.all()
    context = {
        'users' : users
    }
    return render(request, 'pages/allusers.html', context)

def logoutPage(request):
    logout(request)
    return redirect(loginPage)


@login_required(login_url='login')
def addFriend(request, pk):
    receiveUser = User.objects.get(id =pk)
    friendship = Friends(id1 = request.user, id2 = receiveUser)
    friendship.save()
    friendship2 = Friends(id1 = receiveUser, id2 = request.user)
    friendship2.save()
    return redirect(mainPage)


@login_required(login_url='login')
def requestFriend(request, pk):
    receiveUser = User.objects.get(id=pk)
    ch = FriendRequest.objects.all().filter(sender = request.user, receiver =receiveUser)
    if ch.count()>1:
        return redirect(allUsersPage)
    sendReq = FriendRequest(sender = request.user, receiver = receiveUser)
    sendReq.save()
    return redirect(allUsersPage)

@login_required(login_url='login')
def listRequestFriend(request):
    reqs = FriendRequest.objects.all().filter(receiver = request.user)
    context  = {
        'reqs' : reqs
    }
    return render(request,'pages/requestpage.html',context)


@login_required(login_url='login')
def listFriends(request):
    friends = Friends.objects.all().filter(id1 = request.user)
    context = {
        'friends' : friends
    }
    return render(request, 'pages/friends.html', context)


@login_required(login_url='login')
def chatPage(request, pk):
    form = MessageForm()
    receiveUser = User.objects.get(id=pk)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid()==True:
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = receiveUser
            message.save()
            messages = Messages.objects.all().filter(receiver=request.user, sender=receiveUser)
            context = {
                'form': form,
                'messages': messages
            }
            return render(request, 'pages/chatpage.html', context)
    messages = Messages.objects.all().filter(receiver = request.user, sender = receiveUser)
    context  = {
        'form': form,
        'messages' : messages
    }
    return render(request,'pages/chatpage.html',context)
