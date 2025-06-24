from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render


def in_group(group_name):
    return lambda user: user.groups.filter(name=group_name).exists()


@login_required
@user_passes_test(in_group("Reader"))
def reader_dashboard(request):
    return render(request, "reader_dashboard.html")


@login_required
@user_passes_test(in_group("Author"))
def author_dashboard(request):
    return render(request, "author_dashboard.html")


@login_required
@user_passes_test(in_group("Patron"))
def patron_dashboard(request):
    return render(request, "patron_dashboard.html")
