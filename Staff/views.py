from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

# Create your views here.
from django.views import View

class AdminHome(View):
    @method_decorator(login_required(login_url="Authentication:sign-in"))
    def get(self, request):
        return render(request, 'admin.html')

    def post(self,request):
        if request.method == "POST":
            pass

def signOut(request):
    logout(request)
    return redirect('Authentication:sign-in')