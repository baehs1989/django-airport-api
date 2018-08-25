from django import forms
from .models import Document
from .validators import validate_file_extension

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='.dat File Upload:',
        validators=[validate_file_extension]
    )