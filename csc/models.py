from django.db import models

# Create your models here.
# Ebooks Model


class Ebooks(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    edition = models.CharField(max_length=50)
    download_link = models.URLField()
    image = models.ImageField(upload_to='book_covers',
                              default='default.jpg')

    class Meta:
        verbose_name = 'Ebooks'
        verbose_name_plural = 'Ebooks'

    def __str__(self):
        return self.title


class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    message = models.TextField()

    def __str__(self):
        return self.full_name
