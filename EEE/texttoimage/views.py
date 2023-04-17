from django.shortcuts import render
from django.http import HttpResponse
import openai

# Create your views here.
def index(request):
    openai.api_key = "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"
    response = openai.Image.create(
        prompt="a person on horse",
        n=2,
        size="1024x1024"
    )

    image_url = response['data'][0]['url']
    print(image_url)
    # image_url = "dummy"

    return render(request, 'index.html', {'image_url': image_url})
