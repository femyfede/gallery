from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm

def gallery(request):
    images = Image.objects.all()
    return render(request, 'gallery/gallery.html', {'images': images})

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = ImageForm()
    return render(request, 'gallery/upload.html', {'form': form})
