from django.db import models
import uuid


class Project(models.Model):
    # Max length is required for this field
    title = models.CharField(max_length=200)
    description = models.TextField(
        null=True, blank=True)
    # Null means it can be empty, Blank is for Django to know
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(
        auto_now_add=True)  # automatically create this
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    # by default django makes an id integer value with auto increment.

    def __str__(self):
        return self.title
