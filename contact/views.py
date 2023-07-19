from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import ContactForm

# Create your views here.

def index(request):
    form_class = ContactForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            html =  render_to_string('contact/email/contact.html',{
                'name':name,
                'email':email,
                'content':content
            })

            send_mail('This contect from Subject', 'This is the message','vsk05032000@gmail.com',['veerababuv878@gmail.com'],html_message=html)


            return redirect('index') 
        


        else:
            form = ContactForm()

    return render(request, 'contact/index.html',{'form':form})
