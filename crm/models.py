from django.db import models
from django.utils import timezone

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    join_date = models.DateField(default=timezone.now)
    membership_type = models.CharField(
        max_length=50,
        choices=[('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Yearly', 'Yearly')]
    )

    def __str__(self):
        return self.name


class FeePayment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="fees")
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateField(default=timezone.now)
    next_due_date = models.DateField()

    def __str__(self):
        return f"{self.member.name} - {self.amount}"
