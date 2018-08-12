from django.db import models
import os

class Document(models.Model):
    # docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    docfile = models.FileField(upload_to='files/')
    created_at = models.DateTimeField(auto_now_add=True, editable=True)
    updated_at = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return str(self.docfile)

    def filename(self):
        return os.path.basename(self.docfile.name)

    class Meta:
        ordering = ['-created_at']
