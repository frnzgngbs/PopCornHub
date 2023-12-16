from django.shortcuts import render
from django.shortcuts import render, redirect
from .form import UserForm
from django.http import HttpResponse
from django.views import View

def login(request):
    return render(request, 'login.html')

class register_form(View):
    template = 'registration.html'

    def get(self, request):
        form = UserForm()
        return render(request, self.template, {'form':form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, self.template, {'form':form})
