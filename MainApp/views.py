from django.shortcuts import render
from django.http import HttpResponse

def main_page(request):
    text="Sample text"
    return HttpResponse(text, request)