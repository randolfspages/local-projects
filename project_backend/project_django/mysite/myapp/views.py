from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .forms import BookForm
from django.shortcuts import redirect


# Create your views here.

def home(request):
    book_list = Book.objects.all()
    return render(request, 'myapp/home.html', {'book_list': book_list})

def details(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'myapp/details.html', {'book': book})

def add_book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        author = request.POST.get('author')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        
        book = Book(title=name, author=author, description=description, price=price, book_image=image)
        book.save()
        return redirect('/')
    return render(request, 'myapp/add_book.html')

def update(request, book_id):
    book = Book.objects.get(id=book_id)
    form = BookForm(request.POST or None, request.FILES, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'myapp/update.html',{'form':form, 'book':book})


def delete(request, book_id):
    if request.method == 'POST':
        book = Book.objects.get(id=book_id)
        book.delete()
        return redirect('/')
    return render(request, 'myapp/delete.html')


    