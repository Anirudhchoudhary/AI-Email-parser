from django.views.generic import TemplateView
from django.shortcuts import render

from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm


class Home(TemplateView):
    template_name = "base/index.html"

    def get_context_data(self, **kwargs):
        context = {
            "name": "Hello Anirudh"
        }
        return context


class PricingPage(TemplateView):
    template_name = "base/pricing.html"


def about(request):
    return render(request, 'base/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data here
            email = form.cleaned_data['email']
            description = form.cleaned_data['description']
            message = ""
            # Send email (configure your settings.py for email backend)
            send_mail(
                'Contact Form Submission',
                f"Message: {message}\n\nDescription: {description}",
                email,
                ['your_email@example.com'],  # Replace with your email
                fail_silently=False,
            )
            return render(request, 'homepage/contact_success.html')
    else:
        form = ContactForm()

    return render(request, 'base/contact.html', {'form': form})
