from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
from .utils import compress_image

def upload_image(request):
    if request.method == 'POST':
        uploaded_image = request.FILES['image']
        quality = int(request.POST.get('quality', 50))  # Default to 50 if not provided
        img_instance = Image(original_image=uploaded_image, compression_quality=quality)
        img_instance.save()

        # Compress the image with the specified quality
        compressed = compress_image(img_instance.original_image, quality)
        img_instance.compressed_image.save(compressed.name, compressed)
        img_instance.save()

        return render(request, 'compressor/result.html', {'image': img_instance})
    return render(request, 'compressor/upload.html')

def download_image(request, image_id):
    img_instance = Image.objects.get(id=image_id)
    file_path = img_instance.compressed_image.path
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type="image/png")
        response['Content-Disposition'] = f'attachment; filename="{img_instance.compressed_image.name.split("/")[-1]}"'
        return response
