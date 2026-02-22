from django.db import models
from components.models import Component

class PCBuild(models.Model):
    class ForSaleChoices(models.TextChoices):
        AVAILABLE = 'AVAILABLE','AVAILABLE'
        NOT_AVAILABLE = 'NOT_AVAILABLE','NOT_AVAILABLE'
        ASK = 'ASK','ASK'
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    components = models.ManyToManyField(
        Component,
        related_name="pc_builds")
    created_at = models.DateTimeField(auto_now_add=True)
    for_sale = models.CharField(max_length=100,
        choices=ForSaleChoices.choices,
        default=ForSaleChoices.AVAILABLE)
    def __str__(self):
        return f"{self.name} - {self.for_sale}"