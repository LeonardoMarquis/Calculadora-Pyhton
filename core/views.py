from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def user_terms(request):
    return render(request, 'user_terms.html')