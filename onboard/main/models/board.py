from django.db import models
from .user import UserProfile


# Модель вопроса
class Question(models.Model):
    CHOICE = "choice"
    TEXT = "text"
    FLOAT = "float"

    QUESTION_TYPES = [
        (CHOICE, "Choice"),
        (TEXT, "Text"),
        (FLOAT, "Float"),
    ]

    title = models.TextField(max_length=100, null=False, blank=False)
    name = models.TextField(max_length=40, null=False, blank=False)
    order = models.IntegerField(null=False, blank=False)
    question_type = models.CharField(max_length=100, choices=QUESTION_TYPES)
    options = models.JSONField(null=True, blank=True)
    depends_on = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )
    depends_key = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        # return (
        #     f"{str(self.order)}. " + self.title + f"{f' ({str(self.depends_on.order) + ". " + str(self.depends_on.title)} - {self.depends_key if self.depends_key else 'ANY'})' if self.depends_on
        #     else ""}"
        # )
    
        return (
            f"{f'[{str(self.depends_on.order) + ". " + str(self.depends_on.title)}: "{self.depends_key if self.depends_key else 'ANY'}"] ' if self.depends_on else ""}" + f"{str(self.order)}. " + self.title
        )
    
    class Meta:
        ordering = ['order']


# Модель ответа пользователя
class Answer(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    value = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.value
