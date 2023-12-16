from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View

from Authentication.form import SignUpForm


class SignUpView(View):
    template_name = "registration.html"

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Authentication:sign-in')

        return render(request, self.template_name, {"form": form})


class LoginForm(View):
    template_name = "sign-in.html"
    def get(self, request):
        if request.user.is_staff:
            return redirect('Authentication:sign-in')
        return render(request, self.template_name)

    def post(self, request):
        if request.method == "POST":
            uname = request.POST.get("username")
            passw = request.POST.get("password")

            auth = {
                "username": uname,
                "password": passw
            }

            user = authenticate(request, username=uname, password=passw)

            print("ASDADADADSADS")

            if user is not None:
                print(user.is_staff)
                if user.is_staff:
                    login(request, user)
                    request.session['auth'] = auth
                    return redirect('admin-home')
                else:
                    login(request, user)
                    request.session['auth'] = auth
                    return redirect('Authentication:register')

        return redirect('Authentication:sign-in')


