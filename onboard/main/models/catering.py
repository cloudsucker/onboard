from django.db import models
from .user import UserProfile
from .business import Business


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


# Модель типа "Общепит"
class CateringType(models.Model):
    BAR = "bar"  # Бар
    COFFEE_HOUSE = "coffee house"  # Кофейня
    RESTAURANT = "restaurant"  # Ресторан
    BURGER_JOINT = "burger joint"  # Бургерная

    CATERING_TYPE_CHOICES = [
        (BAR, "Catering"),
        (COFFEE_HOUSE, "Coffee house"),
        (RESTAURANT, "Restaurant"),
        (BURGER_JOINT, "Burger joint"),
    ]

    # Связка пользователя с типом "Общепит" и типом общепита
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    business_type = models.ForeignKey(Business, on_delete=models.CASCADE)
    catering_type = models.CharField(
        max_length=100, choices=CATERING_TYPE_CHOICES, blank=False
    )

    def __str__(self):
        return self.catering_type


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


# Общая модель видов общепита
class BaseCateringType(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    # Кухонное помещение
    has_kitchen = models.BooleanField(blank=False, default=True)
    kitchen_area = models.FloatField()

    # Дополнительная информация
    hall_area = models.FloatField()
    seating_capacity = models.IntegerField()
    has_delivery = models.BooleanField()
    opening_hours = models.TimeField()
    number_of_employees = models.IntegerField()


# Кофейня
class CoffeeHouse(BaseCateringType):
    pass


# Ресторан
class Restaurant(BaseCateringType):
    pass


# Бургерная
class BurgerJoint(BaseCateringType):
    pass
