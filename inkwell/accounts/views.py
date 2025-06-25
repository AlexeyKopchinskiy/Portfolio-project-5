from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import Group
from django.contrib.auth import logout
from .forms import ReaderSignUpForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


# Create your views here.


def in_group(group_name):
    return lambda user: user.groups.filter(name=group_name).exists()


def custom_logout(request):
    logout(request)
    return redirect("start")  # or whatever view you prefer


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


class RoleBasedLoginView(LoginView):
    def get_success_url(self):
        user = self.request.user
        if user.groups.filter(name="Author").exists():
            return reverse_lazy("author_dashboard")
        elif user.groups.filter(name="Patron").exists():
            return reverse_lazy("patron_dashboard")
        else:
            return reverse_lazy("reader_dashboard")
