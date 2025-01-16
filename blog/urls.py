from django.urls import include, path

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
