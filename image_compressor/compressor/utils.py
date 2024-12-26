from PIL import Image as PilImage
from io import BytesIO
from django.core.files.base import ContentFile

def compress_image(image, quality=30, max_width=800, max_height=800):
    # Open the image
    img = PilImage.open(image)

    # Convert RGBA to RGB if the image has an alpha channel (transparency)
    if img.mode == 'RGBA':
        img = img.convert('RGB')

    # Resize image while keeping the aspect ratio
    img.thumbnail((max_width, max_height))

    # Compress the image with the specified quality
    img_io = BytesIO()
    img.save(img_io, format='PNG', quality=quality, optimize=True, progressive=True)
    img_io.seek(0)

    # Return as a Django ContentFile
    return ContentFile(img_io.read(), name=image.name)
