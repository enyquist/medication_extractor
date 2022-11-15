# third party libraries
import django.forms as forms


class DemoForm(forms.Form):
    """Custom form to take in text"""

    text = forms.CharField(widget=forms.Textarea)
