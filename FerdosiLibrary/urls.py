"""
URL configuration for FerdosiLibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from library.views import *
from attendance.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("books/", BooksListView.as_view(), name="books"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("book_request/", BookRequestView.as_view(), name="book_request"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path('search-books/', BookSearchAjaxView.as_view(), name='search-books'),
    path('attendance/', mark_attendance, name='mark_attendance'),
]


