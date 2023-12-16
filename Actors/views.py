from multiprocessing import connection

from django.shortcuts import render
from django.shortcuts import render, redirect
from .form import ActorsForm
from django.http import HttpResponse
from django.views import View
from django.db import connection
from django.views.generic import View

# Create your views here.
def login(request):
    return render(request, 'sign-in.html')
class ActorsView(View):
    template_name = 'celebs.html'
    def get(self, request):
        form = ActorsForm()
        return render(request, 'celebs.html', {'form': form})

    def post(self, request):
        form = ActorsForm(request.POST)
        if form.is_valid():

            actor_id = request.POST.get('actor_id')
            firstname = request.POST.get('FirstName')
            lastname = request.POST.get('LastName')
            age = request.POST.get('Age')
            birthday = request.POST.get('BirthDate')
            birthplace = request.POST.get('BirthPlace')
            height = request.POST.get('Height')
            description = request.POST.get('Description')
            status = request.POST.get('Status')

            args = [actor_id, firstname, lastname, age, birthday, birthplace, height, description, status]
            cursor = connection.cursor()
            cursor.callproc('InsertActor', args)
            result = cursor.fetchall()
            return HttpResponse("INSERT SUCCESSFULLY")
        return render(request, 'celebs.html', {'form': form})