from django.shortcuts import render

from tests.forms import PersonForm

# Create your views here.
def create_person(request):
    form = PersonForm(request.POST)
    context = {'form': form}
    return render(request, 'create-person.html', context)