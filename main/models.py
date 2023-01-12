from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пост")
    title = models.CharField(max_length=255, verbose_name="Название поста")
    content = models.TextField(verbose_name="Содержание поста")

    def __str__(self):
        return f"Пост {self.title} - от пользователя {self.user.username}"

    class Meta:
        verbose_name = "Пост"
        verbose_name = "Посты"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Лайк")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост", related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Лайк на {self.post.title} от {self.user.username}"

    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"
