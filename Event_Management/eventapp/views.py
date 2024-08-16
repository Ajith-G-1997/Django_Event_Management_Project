from django.shortcuts import render,get_object_or_404,redirect
from .forms import BookingForm
from .models import Event,Booking

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def single_speaker(request):
    return render(request,'single_speaker.html')
def testimonial(request):
    return render(request,'testimonial.html')
def pricing(request):
    return render(request,'pricing.html')
def gallery(request):
    return render(request,'gallery.html')
def sponsors(request):
    return render(request,'sponsors.html')

def book_event(request, event_id):
    event = Event.objects.get(id=event_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.event = event
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm(initial={'event': event, 'speaker': event.speaker})

    return render(request, 'book_event.html', {'form': form, 'event': event})

def booking_success(request):
    return render(request, 'booking_success.html')


def event_list(request):
    events = Event.objects.all()
    return render(request, 'schedule.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event_detail.html', {'event': event})

def booking_list(request):
    events = Booking.objects.all()
    return render(request, 'booking_list.html', {'events': events})