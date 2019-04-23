from .email import send_welcome_email
from django.shortcuts import render,redirect
from django.http  import HttpResponse, Http404,HttpResponseRedirect
from .models import Image,Staff,Registor,NewsLetterRecipients
from .forms import RegistorForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'index.html')
def mission(request):
    return render(request,'mission.html')
def promoter(request):
    return render(request,'promoters.html')
def campuse(request):
    return render(request,'campuses.html')
def image(request):
    
    images = Image.get_all_images()
    return render(request, 'image.html', { 'images':images})
def staff(request):
    
    staffs= Staff.get_all_staff()
    
    return render(request, 'staff.html',{"staffs":staffs})
def registration(request):
    current_user = request.user
    if request.method == 'POST':
        form = RegistorForm(request.POST,request.FILES)
        if form.is_valid():
            register = form.save(commit=False)
            register.user = current_user
            # recipient = NewsLetterRecipients(name = name,email =email)
            # recipient.save()
            register.save()
            send_welcome_email(register.first_name,register.email)
            HttpResponseRedirect('registration')
        return redirect("home")
    else:
        form = RegistorForm()
    return render(request, 'registration/registration_form.html', {"form":form})
def email(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('email')
            #.................
    return render(request, 'email/hautemail.html', {"letterForm":form})
