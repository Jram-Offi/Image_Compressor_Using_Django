from django.db import models

class Image(models.Model):
    original_image = models.ImageField(upload_to='originals/')
    compressed_image = models.ImageField(upload_to='compressed/', blank=True, null=True)
    compression_quality = models.PositiveIntegerField(default=50)  # Range: 1-100
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id}"
