from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request, article_num, author="None"):
    return HttpResponse(f"Article #{article_num} author name: {author}")


def params(request):
    result = []
    for key, value in request.GET.items():
        result.append(f"Request parameter: {key}, {value}")
    print("\n".join(result))
    return HttpResponse(f"Receivede params: <br>{'<br>'.join(result)}")