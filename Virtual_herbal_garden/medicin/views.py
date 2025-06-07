from django.conf import settings
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Herb,Add_herb
from django.core.paginator import Paginator
from django.core.mail import send_mail
from .forms import HerbForm,ContactForm,Remedy
from django.urls import reverse
import smtplib
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'medicin/index.html', {'current_page': 'index'})

"""def herbs(request):
    herbs = Herb.objects.all()  # Fetch all herbs from the database
    return render(request, 'medicin/herbs.html', {'herbs': herbs})"""

"""def herbs(request):
    query = request.GET.get('query', '')  
    if query:
        herb_list = Herb.objects.filter(name__icontains=query)  
    else:
        herb_list = Herb.objects.all()  

    paginator = Paginator(herb_list, 3)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'medicin/herbs.html', {'page_obj': page_obj, 'query': query})"""

def herbs(request):
    query = request.GET.get('query', '')  
    herb_ids = request.GET.get('herbs', '')  # Get herb IDs from query string

    if herb_ids:
        herb_list = Herb.objects.filter(id__in=herb_ids.split(','))  # Filter herbs by ID
    elif query:
        herb_list = Herb.objects.filter(name__icontains=query)  
    else:
        herb_list = Herb.objects.all()  

    paginator = Paginator(herb_list, 3)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'medicin/herbs.html', {
    'page_obj': page_obj,
    'query': query,
    'current_page': 'herbs'
})

def about(request):
    return render(request, 'medicin/about.html', {'current_page': 'about'})


def add_herbs(request):
    form = HerbForm()
    
    if request.method == "POST":
        form = HerbForm(request.POST, request.FILES)
        if form.is_valid():
            herb = form.save()  # Save the submitted herb

            # ✅ Define subject & message inside the valid form block
            subject = "New Herb Submission for Approval"
            message = f"A new herb has been submitted:\n\n" \
                      f"Name: {herb.name}\n" \
                      f"Description: {herb.description}\n\n" \
                      f"Please review and approve it in the admin panel."

            admin_email = "bhavanabhat327@gmail.com"
            
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [admin_email])
            except Exception as e:
                print(f"Email sending failed: {e}")  # Log the error

            return redirect("herbs")  # ✅ Redirect after successful submission
        else:
            print("Form is invalid:", form.errors)  # ✅ Debugging

    return render(request, "medicin/add_herbs.html", {"form": form})

    

def contacts(request):
    return render(request, 'medicin/contacts.html', {'current_page': 'contacts'})


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to the database
            return redirect('contacts')  # Redirect to the same page (or a success page)
    else:
        form = ContactForm()
    
    return render(request, "contacts.html", {"form": form, "current_page": "contacts"})



from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Remedy

def find_remidy(request):
    if request.method == "POST":
        disease = request.POST.get("disease")
        print(f"Received disease input: {disease}")  # Debugging

        if disease:
            # Debug: Print all available remedies
            print("All available remedies:", list(Remedy.objects.values_list('disease', flat=True)))

            remedy = Remedy.objects.filter(disease__icontains=disease).first()
            
            if remedy:
                herb_ids = list(remedy.herbs.values_list('id', flat=True))  # Extract herb IDs
                if herb_ids:
                    redirect_url = reverse('herbs') + f"?herbs={','.join(map(str, herb_ids))}"
                    print(f"Redirecting to: {redirect_url}")  # Debugging
                    return redirect(redirect_url)
                else:
                    messages.error(request, "We do not have remedies for this disease.")
            else:
                messages.error(request, "We do not have remedies for this disease.")  # Display popup
        else:
            messages.error(request, "Please enter a valid disease name.")  # Display popup

    return render(request, "medicin/find_remidy.html", {'current_page': 'find_remidy'})


"""
def find_remidy(request):
    if request.method == "POST":
        disease = request.POST.get('disease')  # Get disease input
        print(f"Received disease input: {disease}")  # Debugging

        # Debug: Print all available remedies in the database
        print("All available remedies:", list(Remedy.objects.values_list('disease', flat=True)))

        try:
            remedy = Remedy.objects.get(disease__icontains=disease)  # Find remedy
            
            # ✅ FIX: Properly extract herb IDs from Many-to-Many relationship
            herb_ids = list(remedy.herbs.values_list('id', flat=True))  

            if herb_ids:
                redirect_url = reverse('herbs') + f"?herbs={','.join(map(str, herb_ids))}"
                print(f"Redirecting to: {redirect_url}")  # Debugging
                return redirect(redirect_url)
            else:
                #print("No herbs found for the disease.")  Debugging
                messages.error(request, "We don't have remedies for this disease.")

        except Remedy.DoesNotExist:
            print("No remedy found for the disease.")  # Debugging
            return render(request, 'medicin/find_remidy.html', {'error': "No remedies found for this condition."})

    return render(request, 'medicin/find_remidy.html')
    


def find_remidy(request):
    if request.method == "POST":
        disease = request.POST.get("disease")
        if disease:
            remedy = Remedy.objects.filter(disease__icontains=disease).first()
            if remedy:
                return render(request, "medicin/find_remidy.html", {"remedy": remedy})
            else:
                messages.error(request, "We don't have remedies for this disease.")
        else:
            messages.error(request, "Please enter a valid disease name.")
    return render(request, "medicin/find_remidy.html")"""
