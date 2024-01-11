from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.
from .models import *
def test(request):
    return HttpResponse('<h1>hello world</h1>')

def success(request):
    peoples = [
        {'name': 'John', 'age': 16},
        {'name': 'def', 'age': 17},
        {'name': 'candy', 'age': 117},
        {'name': 'biden', 'age': 2},
        {'name': 'putin', 'age': 10},

    ]
    return render(request, "home/index.html", context= {'page': 'Success',"peoples": peoples}, )

def about(request):
    peoples = [
        {'name': 'Prateek', 'about': 'developer'},
        {'name': 'Rajak', 'about': 'engineer'},
        {'name': 'Satyam', 'about': 'designer'},
        {'name': 'Test', 'about': 'tester'},
        {'name': 'putin', 'about': 'president'},

    ]
    return render(request, "home/about.html", context= {'page': 'About',"peoples": peoples})

def contact(request):
    peoples = [
        {'name': 'sobika', 'contact': 6651515},
        {'name': 'yuvan', 'contact': 51615},
        {'name': 'vintoh', 'contact': 15315},
        {'name': 'geenesh', 'contact': 51330},
        {'name': 'putin', 'contact': 944169},

    ]
    return render(request, "home/contact.html", context= {'page': 'Contact', "peoples": peoples})

def RegistrationForm(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        age = data.get('age')
        profile = request.FILES.get('profile')
        print(data)
        User.objects.create(
             name = name,
             email = email,
             phone = phone,
             age = age,
             profile = profile,
             )  
        return redirect('/about/')
    data=User.objects.all()
    context={'users': data}
    return render(request, "home/form.html", context)    

def Delete(request, id):
    querySet= User.objects.get(id=id)
    querySet.delete()
    return HttpResponse("<div>done</div>")

