from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models.board import Question
import json


def main(request):
    return render(request, "main/index.html")


def onboard(request):
    """
    Подгружает первый по очерёдности вопрос при переходе
    на страницу опроса.
    """

    first_question = Question.objects.order_by("order").first()

    if first_question:
        question_data = {
            "title": first_question.title,
            "name": first_question.name,
            "options": first_question.options,
        }

        return render(request, "board/default/main.html", question_data)

    return HttpResponse("Вопросы не найдены")


def update_questions(request):
    data = json.loads(request.body)

    question_name = data.get("name")
    user_answer = data.get("value")

    print("Имя вопроса:", question_name)
    print("Ответ:", user_answer)

    next_questions = []

    # Ищем связанные вопросы
    matching_questions = Question.objects.filter(
        name=user_answer, depends_on__name=question_name
    )

    for matching_question in matching_questions:
        print("Связка: ", matching_question)
        question_data = {
            "title": matching_question.title,
            "name": matching_question.name,
            "options": matching_question.options,
        }
        next_questions.append(question_data)

    # Если найдены следующие вопросы, возвращаем их данные
    if next_questions:
        return render(request, "board/dynamic/selection.html", next_questions[0])

    # Если связанных вопросов нет, ищем следующие по порядку вопросы
    current_question = Question.objects.get(name=question_name)
    next_order_questions = Question.objects.filter(order__gt=current_question.order)

    for next_question in next_order_questions:
        question_data = {
            "title": next_question.title,
            "name": next_question.name,
            "options": next_question.options,
        }
        next_questions.append(question_data)

    # Если найдены следующие по порядку вопросы, возвращаем их данные
    if next_questions:
        print("По порядку: " + str(next_questions))
        return render(request, "board/dynamic/selection.html", next_questions[0])

    # Если вопросы кончились, возвращаем кнопку отправки формы
    print("Нет вопросов")
    return render(request, "board/dynamic/submit_button.html")
