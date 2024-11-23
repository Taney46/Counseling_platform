# models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_counselor = models.BooleanField(default=False)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    availability = models.JSONField(default=dict)

    def __str__(self):
        return self.user.username


# Signal to create or save profile when a new user is created
@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        # Create the profile when the user is created
        Profile.objects.create(user=instance)
    else:
        # Save the profile on user update
        instance.profile.save()

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    counselor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="counseling_sessions")
    date = models.DateTimeField()
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=[('upcoming', 'Upcoming'), ('completed', 'Completed')], default='upcoming')

    def __str__(self):
        return f"Session with {self.counselor.username} on {self.date}"

class Resource(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class Counselor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
