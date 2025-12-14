from django.shortcuts import render, redirect
from django.views import generic
from django.core.paginator import Paginator

from .models import Post
from .forms import CommentaryForm


def index(request):
    all_posts = Post.objects.all().order_by("-created_time")

    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "post_list": page_obj,
    }
    return render(request, "blog/index.html", context=context)


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()

        context["commentaries"] = post.commentaries.all()
        context["form"] = CommentaryForm()

        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.get(request, *args, **kwargs)

        self.object = self.get_object()
        form = CommentaryForm(request.POST)

        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.user = request.user
            commentary.post = self.object
            commentary.save()

            return redirect(self.object.get_absolute_url())

        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)
