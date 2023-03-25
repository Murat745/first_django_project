from django.shortcuts import render

from .forms import Hypotenuse


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
