from django.shortcuts import render
from .forms import LoginForm,RegistrationForm,UserProfileForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login

# Create your views here.

def user_login(request):

    if request.method == "POST":
        print(request.POST)
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            print(cd)
            user = authenticate(username=cd['username'],password=cd['password'])

            if user:
                login(request,user)
                return HttpResponse("Wellcome You. You have been authenticated successfully")
            else:
                return HttpResponse("Sorry. Your username of password is not right.")
        else:
            return HttpResponse("Invalid login")


    if request.method == "GET":
        print(request.GET)
        login_form = LoginForm()
        return render(request, "account/login.html", {"form":login_form})



# def register(request):
#     if request.method == "POST" :
#         user_form = RegistrationForm(request.POST)
#         if user_form.is_valid() :
#             new_user = user_form.save(commit=False)
#             new_user.set_password(user_form.cleaned_data['password'])
#             new_user.save()
#             return  HttpResponse("successfully")
#         else:
#             return HttpResponse("sorry,you can not register.")
#     else:
#         user_form = RegistrationForm()
#         return render(request,"account/registration.html",{"form":user_form})

def register(request):
    if request.method == "POST" :
        user_form = RegistrationForm(request.POST)
        userprofile = UserProfileForm(request.POST)
        if user_form.is_valid() * userprofile.is_valid() :
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile.save(commit=False)
            new_profile.user = new_user
            new_profile.save()

            return  HttpResponse("successfully")
        else:
            return HttpResponse("sorry,you can not register.")
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request,"account/registration.html",{"form":user_form,"profile":userprofile_form})