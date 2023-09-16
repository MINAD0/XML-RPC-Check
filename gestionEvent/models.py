from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    USER_TYPE_CHOICES = (
        ('client', 'Client'),
        ('superUser', 'SuperUser'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='client')
    image = models.ImageField(upload_to="", blank=True)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Fournisseurs(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=255)
    services_offered = models.TextField()

    def __str__(self):
        return self.name
    

class Event(models.Model):
    event_type = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    catering_options = models.ForeignKey(Fournisseurs, on_delete=models.CASCADE) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="", blank=True)



    def __str__(self):
        return self.event_type

class Reservation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # ForeignKey to Event model
    user = models.ForeignKey(User, on_delete=models.CASCADE)    # ForeignKey to User model
    reservation_date = models.DateTimeField()  # Date and time when the reservation was made

    # You can add more fields related to the reservation here, such as the number of seats, special requests, etc.

    def __str__(self):
        return f"Reservation for {self.user.username} at {self.event.event_type}"
    

class Facture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    # You can add more fields like invoice date, due date, etc.

    def __str__(self):
        return f"Invoice for {self.user}"

