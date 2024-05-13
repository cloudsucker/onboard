from django.db import models
from .user import UserProfile


# Модель типа бизнеса
class Business(models.Model):
    CATERING = "catering"  # Общепит
    RETAIL = "retail"  # Ритейл
    SERVICE = "service"  # Услуги на заказ

    BUSINESS_TYPE_CHOICES = [
        (CATERING, "Catering"),
        (RETAIL, "Retail"),
        (SERVICE, "Service"),
    ]

    # Связываем пользователя с типом его бизнеса
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    business_type = models.CharField(
        max_length=100, choices=BUSINESS_TYPE_CHOICES, blank=False
    )

    def __str__(self):
        return self.business_type
