from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """The topic that the user is studying."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        """Returns a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Information, studied by user"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string representation of the model."""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text

    class Meta:
        verbose_name_plural = 'entries'
