from django.db import models
from django.utils import timezone

# Create your models here.

class Expense(models.Model):
    description = models.TextField()
    amount = models.DecimalField(
        max_digits=9,
        decimal_places=2
    )
    created_date = models.DateTimeField(
        default=timezone.now
    )
    expense_date = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return self.description