from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):
    """Represents a blog post authored by a user, with support for
    categories, tags, and publication status."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    tags = models.ManyToManyField("Tag", blank=True, related_name="posts")
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Category(models.Model):
    """Defines a category that a blog post can belong to,
    used for content organization and filtering."""

    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Tag(models.Model):
    """A keyword or label assigned to one or more posts,
    allowing flexible content discovery."""

    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
