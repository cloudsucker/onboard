from django.contrib import admin
from .models import *

admin_models = [
    UserProfile,
    Business,
    CateringType,
    RetailType,
    ServiceType,
    CoffeeHouse,
    Restaurant,
    BurgerJoint,
    BooksRetail,
    SportRetail,
    ClothesRetail,
    DisignService,
    ITService,
    MusicService,
]

admin.site.register(admin_models)
