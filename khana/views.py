from django.shortcuts import render

def index(request):
    return render(request, "khana/home.html")
    
def item(request):
    return render(request, "khana/item.html", {'content' : []})

def dash(request):
    return render(request, "khana/dashboard.html", {'content' : []})
    
def vendor(request):
    return render(request, "khana/vendor.html", {'content' : []})
