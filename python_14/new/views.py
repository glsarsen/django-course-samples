from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    context = {
        'name': 'Test user',
        'email': 'Test@email.com',
        'phone': '+39990123456',
        'data': [
            'aaa',
            'aasdfasdfsad',
            'sfdafwer',
            'qweagdsfafd',
            'asdasfdasfd',
        ]
    }
    if request.method == "POST":
        # print(request.path)
        return redirect('thank_you_page')
    
    request.headers
    
    for key, value in request.COOKIES.items():
        print(f"{key} : {value}")

    if request.POST:
        # print("Empty GET")
        # print(request.GET)
        context = {
            'name': request.POST['new_name'],
            'email': request.POST['new_email'],
            'phone': request.POST['new_phone'],
        }
    return render(request, "index.html", context)


def second_page(request):
    return HttpResponse("<h1>Thank you for registering<h1>")