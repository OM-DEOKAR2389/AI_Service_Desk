
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required
from accounts.models import User



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

@login_required(login_url='login')
@role_required(['Admin'])
def add_user(request):

    if request.method == "POST":

        form = UserForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.set_password(form.cleaned_data['password'])

            user.save()

            messages.success(request, "User created successfully.")

            return redirect('user_list')

    else:

        form = UserForm()
    return render(request, 'dashboard/add_user.html', {'form': form})

@login_required(login_url='login')
@role_required(['Admin'])
def edit_user(request, id):

    user = get_object_or_404(User, id=id)

    if request.method == "POST":

        form = UserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            messages.success(request, "User updated successfully.")
            return redirect('user_list')

    else:
        form = UserForm(instance=user)

    return render(
        request,
        'dashboard/edit_user.html',
        {'form': form}
    )


@login_required(login_url='login')
@role_required(['Admin'])
def delete_user(request, id):

    user = get_object_or_404(User, id=id)

    if request.user == user:
        messages.error(request, "You cannot delete your own account.")
        return redirect('user_list')

    user.delete()

    messages.success(request, "User deleted successfully.")

    return redirect('user_list')

