from django.db import models
from django.urls import reverse

# Create your models here.
# 发表帮助文档
class Help(models.Model):
    title = models.CharField(max_length=50, verbose_name="文章标题")  # 文章标题
    order_by = models.PositiveIntegerField(verbose_name="序号")  # 用于排序
    contents = models.TextField(blank=True)  # 文章内容
    available = models.BooleanField(default=True, verbose_name='状态')

    class Meta:
        ordering = ('order_by',)  # 根据order_by排序
        verbose_name = '文章'

    def get_absolute_url(self):
        return reverse('help:help_detail',
                       args=[self.id])

    def __str__(self):
        return self.title
