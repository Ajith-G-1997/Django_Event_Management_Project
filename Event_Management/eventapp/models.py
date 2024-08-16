from django.db import models

# Create your models here.


class Speaker(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    specialize = models.CharField(max_length=100)
    image = models.ImageField(upload_to='speakers/')

    def __str__(self):
        return self.name
    
class Event(models.Model):
    time = models.DateTimeField()
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.subject} by {self.speaker.name} at {self.venue}"
    
class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

   