from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def contact(request: HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

       


        # Prepare the email content
        email_message = f'''
        You have received a new message:

        Name: {name}
        Email: {email}
        Phone Number: {number}
        Subject: {subject}
        Message: {message}
        '''

        # Send the email
        try:
            send_mail(
                subject,
                email_message,
                settings.EMAIL_HOST_USER,  
                ['aiondatta1234@gmail.com'],  
                fail_silently=True,
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('#home')  
        except Exception as e:
            
            print(f"Error sending email: {e}")
            
            

    return render(request, 'index.html', {})