from django.contrib.auth.models import User
from django.db import models


admin_models = [
    "UserProfile",
    "Business",
    "CateringType",
    "RetailType",
    "ServiceType",
    "CoffeeHouse",
    "Restaurant",
    "BurgerJoint",
    "BooksRetail",
    "SportRetail",
    "ClothesRetail",
    "DisignService",
    "ITService",
    "MusicService",
]


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


# Модель пользовательских данных
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.name


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


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
