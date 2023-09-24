from django.shortcuts import render, HttpResponse
from django.utils import timezone


# Create your views here.
def index(request):
    return HttpResponse("Hello world! <br><a href='dow'>Day of week</a>")


def day_of_the_week(request):
    now = timezone.now().weekday()
    days = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    return HttpResponse(f" Today is {days[now]}")


