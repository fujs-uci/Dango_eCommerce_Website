from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    context = locals()
    template = 'profiles/home.html'
    return render(request, template, context)


def about(request):
    context = locals()
    template = 'profiles/about.html'
    return render(request, template, context)


@login_required
def user_profile(request):
    user = request.user
    context = {'user': user, }
    template = 'profiles/profile.html'
    return render(request, template, context)
