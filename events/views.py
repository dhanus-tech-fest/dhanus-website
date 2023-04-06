from django.shortcuts import render, redirect
from .models import Event

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        image = request.FILES['image']
        title = request.POST['title']
        description = request.POST['description']
        Event.objects.create(image=image, title=title, description=description)
        return redirect('event_list')
    return render(request, 'events/add_event.html')
