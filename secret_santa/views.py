from django.shortcuts import render

from secret_santa.models import Person

# Create your views here.
def home(request):
    if request.POST:
        person = Person(
            budget=request.POST['budget'],
            name=request.POST['name'],
            like=request.POST['likes'],
            dislike=request.POST['dislikes'],
            address=request.POST['address'],
            email=request.POST['email'],
        )

        person.save()

    return render(request, 'secret_santa/home.html')
