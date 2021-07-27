from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json


def course_category(request):
    courses = Category.objects.all()
    category=[]
    for course in courses:
        Question_category={}
        Question_category['id']=course.id
        Question_category['category'] = course.category
        category.append(Question_category)
    return JsonResponse(category,safe=False)


def questions(request, id):
    all_questions = Question.objects.filter(category=id)[:10]
    results = []

    for raw_question in all_questions:

        question = {}
        question['id'] = raw_question.id
        question['category'] = raw_question.category.category
        question['question'] = raw_question.question
        question['correct_answer'] = raw_question.correct_answer
        options = []
        options.append(raw_question.option_one)
        options.append(raw_question.option_two)
        if raw_question.option_three != '':
            options.append(raw_question.option_three)

        if raw_question.option_four != '':
            options.append(raw_question.option_four)

        question['options'] = options
        results.append(question)



    return JsonResponse(results, safe=False)
