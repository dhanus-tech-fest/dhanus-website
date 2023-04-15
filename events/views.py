from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect, render,  get_object_or_404
from django.urls import reverse_lazy

from .models import Event
from .forms import EventForm


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
        prize = request.POST["prize"]
        guidelines = request.POST["guidelines"]
        is_active = request.POST["is_active"]
        konf_hub_url = request.POST["konf_hub_url"]
        Event.objects.create(image=image, title=title, description=description, prize=prize,
                             konf_hub_url=konf_hub_url, is_active=is_active, guidelines=guidelines)
        return redirect('event_list')
    return render(request, 'events/add_event.html')


def edit_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('all_events')
    else:
        form = EventForm(instance=event)
    return render(request, 'edit_event.html', {'form': form, 'event_id': event_id})
