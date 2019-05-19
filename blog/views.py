from django.shortcuts import render
from .forms import contactForm
from django.contrib.auth import authenticate, login



def contact(request):
    error = False
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():

            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                error = True

    else:
        form = contactForm()

    return render(request, 'form.html', locals())

