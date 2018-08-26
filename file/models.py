from django.db import models
import os
from django.dispatch import receiver

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

@receiver(models.signals.post_delete, sender=Document)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    # if instance.docfile:
    #     if os.path.isfile(instance.docfile.path):
    #         os.remove(instance.docfile.path)
    instance.docfile.delete(save=False)