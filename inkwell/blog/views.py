from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .forms import PostForm

# Create your views here.


def is_author(user):
    return user.groups.filter(name="Author").exists()


@login_required
# @user_passes_test(lambda u: u.groups.filter(name="Author").exists())
@user_passes_test(
    lambda u: u.groups.filter(name__in=["Author", "Patron"]).exists()
)
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()  # for tags
            messages.success(request, "Your post has been created!")
            return redirect("author_dashboard")
    else:
        form = PostForm()
    return render(request, "author_dashboard/create_post.html", {"form": form})
