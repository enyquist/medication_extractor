# third party libraries
from demo.forms import DemoForm
from django.contrib import messages
from django.shortcuts import render

# custom libraries
from medication_extractor.utils import get_medication_mapping


def home(request):
    """Home view"""
    if request.method == "POST":
        form = DemoForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get("text")
            medication_mapping = get_medication_mapping(text)
            messages.success(request, "Medications Extracted!")
            return render(request, "demo/demo.html", {"text": text, "medications": medication_mapping})
    else:
        form = DemoForm()
    return render(request, "demo/home.html", {"form": form})


def demo(request):
    """Demo View"""
    return render(request, "demo/demo.html")
