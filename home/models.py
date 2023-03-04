from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories" 
    def __str__(self) -> str:
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Topic"
        verbose_name_plural = "Topics"

    def __str__(self) -> str:
        return self.name

class Command(models.Model):
    code = models.CharField(max_length=100, verbose_name="Codigo")
    description = models.CharField(max_length=100)
    link = models.CharField(max_length=100, default="")
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        pass
    def __str__(self) -> str:
        return f"Linea de codigo: {self.code}"

# class Linux(Command):
#     class Meta:
#         verbose_name = "Linux"
#         verbose_name_plural = "Linux Commands"


