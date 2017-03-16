from django.shortcuts import render

from .models import Thing

def test(request):
    things = Thing.objects.all()
    return render(request, 'test.html', {'things':things})