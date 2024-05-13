from django.shortcuts import render
from django.http import JsonResponse


def main(request):
    return render(request, "main/index.html")


def onboard(request):
    business_type_question = {
        "title": "Тип вашего бизнеса",
        "name": "business_type",
        "options": {
            "сatering": "Общепит",
            "retail": "Ретейл",
            "service": "Услуги на заказ",
        },
    }

    return render(request, "board/default/main.html", business_type_question)


def get_next_question(request):
    print(request.POST.get("selected_value"))
    next_question = {
        "title": "Новый вопрос",
        "name": "new_question",
        "options": {
            "some_option": "Опция 1",
            "some_second_option": "Опция 2",
            "some_third_option": "Опция 3",
        },
    }

    return JsonResponse(next_question)
