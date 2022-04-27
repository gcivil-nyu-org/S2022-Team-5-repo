from django.db import models
from django.db.models import Q
from account.models import UserProfile

# Create your models here.


class ThreadManager(models.Manager):
    def byUser(self, **kwargs):
        user = kwargs.get("user")
        lookup = Q(first_person=user) | Q(second_person=user)
        qs = self.get_queryset().filter(lookup).distinct()

        return qs


class Thread(models.Model):
    first_person = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="thread_first_person",
    )
    second_person = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="thread_second_person",
    )
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ThreadManager()

    class Meta:
        unique_together = ["first_person", "second_person"]


class ChatMessage(models.Model):
    thread = models.ForeignKey(
        Thread,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="chatmessage_thread",
    )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
