from django.db import models
from .user import UserProfile
from .business import Business


# Модель для типа "Услуги на заказ"
class ServiceType(models.Model):
    DESIGN = "design"  # Дизайн
    IT = "it"  # Айти
    MUSIC = "music"  # Музыка

    SERVICE_TYPE_CHOICES = [
        (DESIGN, "Design"),
        (IT, "It"),
        (MUSIC, "Music"),
    ]

    # Пользователь, тип "Услуги на заказ", тип услуг
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    business_type = models.ForeignKey(Business, on_delete=models.CASCADE)
    service_type = models.CharField(
        max_length=100, choices=SERVICE_TYPE_CHOICES, blank=False
    )

    # Дополнительная информация
    has_office = models.BooleanField(blank=False)
    office_area = models.FloatField()

    def __str__(self):
        return self.service_type


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


# Общая модель видов услуг на заказ
class BaseServiceCategory(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    service_category = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    has_office = models.BooleanField()
    office_area = models.FloatField()

    # Дополнительная информация
    opening_hours = models.TimeField()
    number_of_employees = models.IntegerField()


# Услуги в дизайне
class DisignService(BaseServiceCategory):
    pass


# Услуги в айти
class ITService(BaseServiceCategory):
    pass


# Услуги в музыке
class MusicService(BaseServiceCategory):
    pass
