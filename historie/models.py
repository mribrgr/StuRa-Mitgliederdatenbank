from django.db import models

class Historie(models.Model):
    CREATE = 'C'
    UPDATE = 'U'
    DELETE = 'D'
    ACTION_CHOICES = [
        (CREATE, 'Erstellen'),
        (UPDATE, 'Bearbeiten'),
        (DELETE, 'Löschen'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True, null=False)
    user = models.CharField(max_length=50, null=False)
    action = models.CharField(max_length=1, choices=ACTION_CHOICES, null=False)
