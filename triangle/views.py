from django.shortcuts import get_object_or_404, redirect, render

from .forms import PersonForm, Hypotenuse
from .models import Person


def triangle(request):
    hypotenuse = None
    if "OK" in request.GET:
        my_form = Hypotenuse(request.GET)

        if my_form.is_valid():
            base = my_form.cleaned_data['base']
            altitude = my_form.cleaned_data['altitude']
            hypotenuse = round(((base ** 2 + (altitude ** 2)) ** 0.5), 2)

            my_form = Hypotenuse()
    else:
        my_form = Hypotenuse()

    return render(request, 'triangle/triangle.html', {'form': my_form, 'hypotenuse': hypotenuse})


def create_person(request):
    if request.method == 'POST':
        user_form = PersonForm(request.POST)

        if user_form.is_valid():
            user_form.save()
            return redirect('triangle:persons_all')

    else:
        user_form = PersonForm()

    return render(request, 'triangle/create_person.html', {'form': user_form})


def persons_all(request):
    all_persons = Person.objects.all()
    return render(request, 'triangle/all_persons.html', {'users': all_persons})


def update_person(request, pk):
    obj = get_object_or_404(Person, pk=pk)

    if request.method == 'POST':
        user_form = PersonForm(request.POST, instance=obj)

        if user_form.is_valid():
            obj = user_form.save()
            return redirect('triangle:person')

    else:
        user_form = PersonForm(instance=obj)

    return render(request, 'triangle/update_person.html', {'form': user_form, 'obj': obj})
