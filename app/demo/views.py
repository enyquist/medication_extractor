# third party libraries
from demo.forms import DemoForm
from django.contrib import messages
from django.shortcuts import render

# custom libraries
import medication_extractor.utils as utils


def home(request):
    """Home view"""
    if request.method == "POST":
        form = DemoForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get("text")
            medication_mapping = utils.get_medication_mapping(text)
            messages.success(request, "Extracting Medications...")
            return render(request, "demo/demo.html", {"text": text, "medications": medication_mapping})
    else:
        form = DemoForm()
    return render(request, "demo/home.html", {"form": form})


def demo(request):
    """Demo View"""
    return render(request, "demo/demo.html")
