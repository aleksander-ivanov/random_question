from django.shortcuts import render
from django.http import JsonResponse
import random
import time

# TODO: Get questions from DB
questions = [
    "What is your favorite color?",
    "What is your favorite food?",
    "What is your favorite movie?",
    "What is your favorite book?",
    "What is your favorite hobby?",
]


def index(request):
    return render(request, 'main/index.html', {'questions': questions})


def test(request):
    return render(request, 'main/test.html', {'questions': questions})


def test2(request):
    return render(request, 'main/test2.html', {'questions': questions})


def get_random_question(request):
    # Simulate the delay of the carousel rotation
    time.sleep(1)

    # Get a random question from the list
    question = random.choice(questions)

    # Return the question as a JSON response
    return JsonResponse({'question': question})
