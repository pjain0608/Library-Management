from django.shortcuts import render,redirect
from .models import Books

# Create your views here.
def index(request):
    # if query:
    #     data1 = Task.objects.filter(title__icontains=query)  
    # else:
    #     data1 = Task.objects.all()  # Get all tasks if no query
    
    query = request.GET.get('search', '')
    if query:
        data = Books.objects.filter(name__icontains=query)
    else:
        data = Books.objects.all()

    context = {
        'data' : data
    }
    return render(request,'index.html', context)

def display(request,pk):
    data1 = Books.objects.get(id = pk)
    if request.method == 'POST':
        data1.delete()
        return redirect('index')
    context = {
        'data1' : data1
    }
    return render(request,'display.html',context)

def edit(request,ab):
    edit = True
    data2 = Books.objects.get(id = ab)
    if request.method == 'POST':
        name = request.POST.get('name')
        author = request.POST.get('author')
        price = request.POST.get('price')
        genre = request.POST.get('genre')
        quantity = request.POST.get('quantity')
        rating = request.POST.get('rating')
        print(name,author,price,genre,quantity,rating)
        data2.name = name
        data2.author = author
        data2.price = price
        data2.genre = genre
        data2.quantity = quantity
        data2.rating = rating
        data2.save()
        return redirect("index")
        # print(name,author,price,genre,quantity,rating)

    context = {
        'data2' : data2,
        'edit':edit
    }
    return render(request,'edit.html',context)

def create(request):
    edit = False
    if request.method == 'POST':
        name = request.POST.get('name')
        author = request.POST.get('author')
        price = request.POST.get('price')
        genre = request.POST.get('genre')
        quantity = request.POST.get('quantity')
        rating = request.POST.get('rating')
        # print(name,author,price,genre,quantity,rating)
        a = Books.objects.create(name = name, author=author,price=price,genre=genre,quantity=quantity,rating=rating)
        return redirect("index")
    return render(request,'add.html',{'edit':edit})