from django.shortcuts import render

# Create your views here.
def index(request, aftertext=""):
    return render(request, 'company/index.html')

def news(request, aftertext=""):
    # print(aftertext)
    return render(request, 'company/news.html')

def management(request, aftertext=""):
    return render(request, 'company/management.html')

def about(request, aftertext=""):
    return render(request, 'company/about.html')

def contacts(request, aftertext=""):
    return render(request, 'company/contacts.html')

def branches(request, name=""):
    if name == "london":
        return render(request, "company/branches/london.html")
    elif name == "paris":
        return render(request, "company/branches/paris.html")
    else:
        return render(request, "company/branches.html")


        
