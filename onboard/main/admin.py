from django.contrib import admin
from .models.board import Question, Answer

admin_models = [Question, Answer]

admin.site.register(admin_models)
