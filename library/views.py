from django.contrib import messages
from django.shortcuts import render

from library.forms import BookRequestForm


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def book_request(request):
    return render(request, "book_request.html")


def books(request):
    return render(request, "books.html")


def book_request_view(request):
    if request.method == 'POST':
        form = BookRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'درخواست شما با موفقیت ثبت شد!')
            return render(request, 'book_request.html', {"counter": 1})
        else:
            return render(request, 'book_request.html', {'form': form})
    else:
        form = BookRequestForm()
    return render(request, 'book_request.html', {'form': form})
