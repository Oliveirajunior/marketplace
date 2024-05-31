from django.contrib.auth.models import User
from django.db import models
from django_resized import ResizedImageField


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(
        Category, related_name="items", on_delete=models.CASCADE
    )  # relacionamento de item com categoria
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = ResizedImageField(
        size=[500, 300], upload_to="item_images", blank=True, null=True
    )
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, related_name="items", on_delete=models.CASCADE
    )  # relacionamento de item com usuario
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
