from django.db import models
from django.contrib.auth.models import User
import uuid

class Note(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_notes')
    shared_with = models.ManyToManyField(User, related_name='shared_notes')
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='modified_notes')

    def __str__(self):
        return self.title
