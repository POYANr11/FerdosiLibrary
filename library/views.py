from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Book
from .forms import BookRequestForm


class HomeView(TemplateView):
    template_name = "home.html"


class AboutView(TemplateView):
    template_name = "about.html"


class BooksListView(ListView):
    model = Book
    template_name = "books.html"
    context_object_name = "books"


class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"
    context_object_name = "book"


class BookRequestView(FormView):
    template_name = "book_request.html"
    form_class = BookRequestForm
    success_url = reverse_lazy("book_request")

    def form_valid(self, form):
        form.save()  # ذخیره فرم در دیتابیس
        messages.success(self.request, 'درخواست شما با موفقیت ثبت شد!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'لطفاً فرم را به‌درستی پر کنید.')
        return self.render_to_response(self.get_context_data(form=form))
