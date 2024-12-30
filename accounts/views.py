from django.shortcuts import render, redirect
from django.contrib.auth import login
from freelancers.models import Freelancer
from clients.models import Client
from .forms import CustomUserSignupForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserSignupForm(request.POST)
        if form.is_valid():
            # Create the user
            user = form.save(commit=False)
            role = form.cleaned_data['role']
            user.save()

            # Assign role-specific logic
            if role == 'freelancer':
                Freelancer.objects.create(owner=user)
            elif role == 'client':
                company = form.cleaned_data['company']
                Client.objects.create(user=user, company=company)

            # Log the user in and redirect
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired redirect URL
    else:
        form = CustomUserSignupForm()

    return render(request, 'accounts/signup.html', {'form': form})
