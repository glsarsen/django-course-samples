from django.shortcuts import render

from .forms import UserForm

# Create your views here.
def index(request):
    if request.method == "POST":
        data = {
            "name": request.POST["username"],
            "password": request.POST["password"],
        }
        return render(request, "form_site/index.html", data)
    return render(request, "form_site/index.html")

def form_page(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data["username"])
        else:
            return render(request, "form_site/form_page.html", {"form": UserForm(), "message": "form is invalid"})
        
    form = UserForm()
    return render(request, "form_site/form_page.html", {"form": form})