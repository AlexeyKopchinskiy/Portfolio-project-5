from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from .forms import ReaderSignUpForm
from django.shortcuts import render

# Create your views here.


def in_group(group_name):
    return lambda user: user.groups.filter(name=group_name).exists()


@login_required
@user_passes_test(in_group("Reader"))
def reader_dashboard(request):
    return render(request, "reader_dashboard/dashboard.html")


@login_required
@user_passes_test(in_group("Author"))
def author_dashboard(request):
    return render(request, "author_dashboard/dashboard.html")


@login_required
@user_passes_test(in_group("Patron"))
def patron_dashboard(request):
    return render(request, "patron_dashboard/dashboard.html")


def register_reader(request):
    if request.method == "POST":
        form = ReaderSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Add to "Reader" group
            reader_group = Group.objects.get(name="Reader")
            user.groups.add(reader_group)
            login(request, user)
            return redirect("reader_dashboard")
    else:
        form = ReaderSignUpForm()
    return render(request, "registration/register.html", {"form": form})
