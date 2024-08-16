from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('single_speaker/',views.single_speaker,name='single-speaker'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('pricing/',views.pricing,name='pricing'),
    path('gallery/',views.gallery,name='gallery'),
    path('sponsors/',views.sponsors,name='sponsors'),
    path('book-event/<int:event_id>/', views.book_event, name='book_event'),
    path('booking-success/', views.booking_success, name='booking_success'),
    path('event_list/',views.event_list,name='event_list'),
    path('event/<int:pk>/',views.event_detail, name='event_detail'),
    path('booking_list/',views.booking_list, name='booking_list'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)