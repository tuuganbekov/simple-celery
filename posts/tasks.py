from random import randint
from celery import shared_task

from posts.models import Post


@shared_task
def new_post():
    print("in task")
    post = Post.objects.create(
        title=f"title: {randint(0, 12)}",
        description=f"description: {randint(0, 12)}",
    )
    post.save()
    print("title:", post.title)
    return post.title


@shared_task
def hello():
    print("Hello world")
    return "Hello world"
