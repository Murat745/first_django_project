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


def person(request):
    form = PersonForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            obj = Person.objects.create(**form.cleaned_data)
            return redirect('triangle:update_person', obj.id)
    elif request.method == 'GET':
        context = {
            "form": form
        }
        return render(request, 'triangle/create_person.html', context)


def update_person(request, pk):
    user = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=user)
        if form.is_valid():
            obj = form.save()
            return redirect('triangle:update_person', obj.id)
    elif request.method == 'GET':
        form = PersonForm(instance=user)
    return render(request, 'triangle/person.html', {"form": form, 'obj': user})
