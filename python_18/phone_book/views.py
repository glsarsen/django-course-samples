from django.shortcuts import render, redirect
from django.contrib.postgres.search import SearchVector
from .forms import AddContact
from .models import PhoneBook


# Create your views here.
def index(request):
    return render(request, "phone_book/index.html")

def add_phone(request):
    form = AddContact(request.POST)
    if request.method == "POST" and form.is_valid():
        contact = PhoneBook(name=form.cleaned_data['name'],
                            lastname=form.cleaned_data['lastname'],
                            email=form.cleaned_data['email'],
                            phone=form.cleaned_data['phone'],
                            about=form.cleaned_data['about'],
                            )
        contact.save()
        return redirect("index")
    return render(request, "phone_book/add_phone.html", {'form':form})

def view_contacts(request):
    data = PhoneBook.objects.all()
    return render(request, "phone_book/show_contacts.html", {'data': data})

# def contact(request, id):
#     contact = PhoneBook.objects.get(id=id)
#     data = {
#         'name': contact.name,
#         'lastname': contact.lastname,
#         # 'email':
#     }

def search_contacts(request):
    if request.method == "POST":
        data = PhoneBook.objects.filter(name__icontains=request.POST["search"])
        data2 = PhoneBook.objects.filter(lastname__icontains=request.POST["search"])
        data = data.union(data2)
        # data = PhoneBook.objects.annotate(search=SearchVector("name", "lastname"),).filter(search=request.POST["name_search"])
        # assert False
        return render(request, "phone_book/show_contacts.html", {"data": data})
    return render(request, "phone_book/search.html")




# from django.db.models import Value as V
# from django.db.models.functions import Concat

# text = "John Doe"
# Profile.objects.annotate(full_name=Concat('name', V(' '), 'surname')).filter(full_name__icontains=text)