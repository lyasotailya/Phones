from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    slug = models.SlugField(unique=True, max_length=255)
    price = models.PositiveIntegerField()
    image = models.ImageField(verbose_name='Фото', upload_to='photos/%Y/%m/%d/')
    release_date = models.CharField(max_length=255, null=False)
    lte_exists = models.BooleanField(blank=True)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
