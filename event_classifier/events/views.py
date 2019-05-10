from django.shortcuts import render, redirect
from .models import Event

# Create your views here.

def event_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, "events/event_list.html", {'events':events})

def event_detail(request,slug):
    #return HttpResponse(slug)
    event = Event.objects.get(slug=slug)
    return render(request, 'events/event_detail.html', {'event':event})
