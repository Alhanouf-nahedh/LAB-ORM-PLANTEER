from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from Planteer.forms import ContactForm


# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('main:contact_messages_view') 
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})

def contact_messages_view(request):
    messages = Contact.objects.all()
    return render(request, 'main/contact_messages.html', {'messages': messages})