from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .models import Event

@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

@login_required(login_url="/login")
def add_event(request):
    if request.method == 'POST':
        image = request.FILES['image']
        title = request.POST['title']
        description = request.POST['description']
        Event.objects.create(image=image, title=title, description=description)
        return redirect('event_list')
    return render(request, 'events/add_event.html')
