from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Photo
from .forms import PhotoForm


def index(request):
    """List photos and handle upload."""
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("drive:index"))
    else:
        form = PhotoForm()

    photos = Photo.objects.order_by("-uploaded_at")
    return render(request, "drive/index.html", {"photos": photos, "form": form})


def delete_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == "POST":
        # delete the file from storage
        photo.image.delete(save=False)
        photo.delete()
        return redirect(reverse("drive:index"))
    return render(request, "drive/confirm_delete.html", {"photo": photo})
