from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('category/',course_category),
    path('question/<id>',questions)
]