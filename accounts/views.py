
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages


def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            if user.role == "Admin":
                return redirect("admin_dashboard")

            elif user.role == "Engineer":
                return redirect("engineer_dashboard")

            else:
                return redirect("user_dashboard")

        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, "accounts/login.html")

def user_logout(request):
    logout(request)
    return redirect("login")