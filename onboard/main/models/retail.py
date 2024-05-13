from django.db import models
from .user import UserProfile
from .business import Business


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


# Модель для типа "Ритейл"
class RetailType(models.Model):
    BOOKS = "books"  # Книги
    SPORT = "sport"  # Спорт
    CLOTHES = "clothes"  # Одежда

    RETAIL_CATEGORY_CHOICES = [
        (BOOKS, "Books"),
        (SPORT, "Sport"),
        (CLOTHES, "Clothes"),
    ]

    # Связка пользователя с типом "Ритейл" и категорией товаров
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    business_type = models.ForeignKey(Business, on_delete=models.CASCADE)
    products_category = models.CharField(
        max_length=100, choices=RETAIL_CATEGORY_CHOICES, blank=False
    )

    def __str__(self):
        return self.products_category


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


# Общая модель видов ритейла
class BaseRetailCategory(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    # Дополнительная информация
    sales_area = models.FloatField()
    warehouse_area = models.FloatField()
    opening_hours = models.TimeField()
    number_of_employees = models.IntegerField()


# Книжный ритейл
class BooksRetail(BaseRetailCategory):
    pass


# Ритейл спортивных товаров
class SportRetail(BaseRetailCategory):
    pass


# Ритейл одежды
class ClothesRetail(BaseRetailCategory):
    pass
