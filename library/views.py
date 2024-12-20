from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView, DetailView, FormView, View
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .models import Book
from .forms import *


# class HomeView(TemplateView):
#     template_name = "home.html"


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


class BookRequestView(LoginRequiredMixin, FormView):
    template_name = "book_request.html"
    form_class = BookRequestForm
    success_url = reverse_lazy("home")
    login_url = reverse_lazy("login")

    def form_valid(self, form):
        book_request = form.save(commit=False)
        book_request.student = self.request.user
        book_request.save()
        messages.success(self.request, 'درخواست شما با موفقیت ثبت شد!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'لطفاً فرم را به‌درستی پر کنید.')
        return self.render_to_response(self.get_context_data(form=form))


class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = CustomAuthenticationForm

    def get_success_url(self):
        return reverse('home')


class BookSearchAjaxView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')  # مقدار جستجو
        if query:
            books = Book.objects.filter(
                Q(title__icontains=query) | Q(author__name__icontains=query)
            ).filter(Q(status='a')).values('id', 'title', 'author__name')
            return JsonResponse({'results': list(books)}, safe=False)
        return JsonResponse({'results': []})


class HomeView(TemplateView):
    template_name = "menu.html"
