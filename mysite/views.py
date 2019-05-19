from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.shortcuts import redirect


def deconnexion(request):
    logout(request)
    return redirect(reverse('contact'))



