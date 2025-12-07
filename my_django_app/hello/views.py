from django.shortcuts import render

# Create your views here.

# views.py

from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError

def custom_login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Reset the failed login attempt counter
            request.session['failed_attempts'] = 0
            return redirect('/inadmin/')  # Redirect to the true admin page or dashboard
        else:
            # Increment failed login attempts
            request.session['failed_attempts'] = request.session.get('failed_attempts', 0) + 1
            if request.session['failed_attempts'] >= 3:
                # Redirect to honeypot URL after 3 failed attempts
                return redirect('/admin/')  # Redirect to the honeypot admin page

            # Return an error message for a failed login attempt
            return render(request, 'login.html', {'error': 'Invalid login credentials'})  # Adjust as needed

    # Render the login page if not a POST request
    return render(request, 'login.html')  # Replace with your login template
