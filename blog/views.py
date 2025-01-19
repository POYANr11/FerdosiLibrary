from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView

from blog.forms import CommentForm
from blog.models import Post, Like, Dislike, Comment


class PostListView(ListView):
    paginate_by = 10
    model = Post
    template_name = "blog/home.html"

    def get_queryset(self):
        return Post.objects.filter(status='published').order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = context["object_list"]

        for post in posts:
            post.likes_count = Like.objects.filter(post=post).count()
            post.dislikes_count = Dislike.objects.filter(post=post).count()

        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/datail.html"

    def get_queryset(self):
        return Post.objects.filter(status='published')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object

        context["comments"] = post.comments.filter(is_active=True)
        context["form"] = CommentForm()

        context["likes_count"] = Like.objects.filter(post=post).count()
        context["dislikes_count"] = Dislike.objects.filter(post=post).count()

        return context


class ToggleLikeDislikeView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            post_id = request.POST.get('post_id')
            action = request.POST.get('action')  # 'like' یا 'dislike'

            post = get_object_or_404(Post, id=post_id)

            if action == 'like':
                Dislike.objects.filter(post=post, author=request.user).delete()
                like, created = Like.objects.get_or_create(post=post, author=request.user)
                if not created:
                    like.delete()
                    status = 'removed_like'
                else:
                    status = 'liked'
            elif action == 'dislike':
                Like.objects.filter(post=post, author=request.user).delete()
                dislike, created = Dislike.objects.get_or_create(post=post, author=request.user)
                if not created:
                    dislike.delete()
                    status = 'removed_dislike'
                else:
                    status = 'disliked'
            else:
                return JsonResponse({'error': 'Invalid action'}, status=400)

            likes_count = Like.objects.filter(post=post).count()
            dislikes_count = Dislike.objects.filter(post=post).count()

            return JsonResponse({
                'status': status,
                'likes_count': likes_count,
                'dislikes_count': dislikes_count,
            })

        return JsonResponse({'error': 'Authentication required'}, status=403)


class CommentCreateView(FormView):
    form_class = CommentForm

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.post = post
        comment.save()
        return redirect(post.get_absolute_url())

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.kwargs['post_pk']})


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comments/comment_form.html"

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = "blog/comments/comment_confirm_delete.html"

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})
