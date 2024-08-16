from django.contrib import admin
from .models import Speaker,Event,Booking

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'specialize', 'image')

class EventAdmin(admin.ModelAdmin):
    list_display = ('time', 'speaker', 'subject', 'venue')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'phone', 'speaker', 'event')

admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Booking, BookingAdmin)
