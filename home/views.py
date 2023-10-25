from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

# Create your views here.
import os
import openai

openai.api_key = "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"


def chat(request):
    return render(request, "index.html")


def chatAPI(request):
    if request.method=="POST":
        prompt = request.POST["prompt"]
        #response = {"this": "that"}
        response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        print(response)
        return JsonResponse(response)
    return HttpResponse("Bad request")