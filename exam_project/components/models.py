from django.db import models

class Category(models.Model):
    class CategoryChoices(models.TextChoices):
        CPU = "CPU"
        GPU = "GPU"
        PSU = "PSU"
        RAM = "RAM"
        SSD = "SSD"
        HDD = "HDD"
        MOTHERBOARD = "MOTHERBOARD"
        COOLER = "COOLER"
        CASE = "CASE"
    name = models.CharField(max_length=100, choices=CategoryChoices.choices, default=CategoryChoices.CPU)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name

class Tag(models.Model):
    class TagsChoices(models.TextChoices):
        GAMING = "GAMING","GAMING"
        BUDGET = "BUDGET", "BUDGET"
        WORKSTATION = "WORKSTATION", "WORKSTATION"
        OFFICE = "OFFICE", "OFFICE"
    name = models.CharField(max_length=100, choices=TagsChoices.choices, default=TagsChoices.WORKSTATION)
    def __str__(self):
        return self.name

class Component(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="components_category")
    tags = models.ManyToManyField(Tag, related_name="components_tags")
    price = models.DecimalField(decimal_places=2, max_digits=10)
    brand = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.URLField(null=True, default='')
    def __str__(self):
        return f"{self.brand} - {self.category}"

