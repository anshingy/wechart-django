from django.db import models
from django.conf import settings
from mall.models import ProductPriceGroup


class WechatTag(models.Model):
    wechat_tag_name = models.CharField(max_length=25, verbose_name="企业号标签名称")
    wechat_tag_id = models.IntegerField(null=True, blank=True, verbose_name="企业号标签ID")

    def __str__(self):
        return str(self.wechat_tag_name)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)  # 和系统的user model一对一
    address = models.CharField(max_length=250, verbose_name="地址")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    wechat_name = models.CharField(max_length=25, null=True, blank=True, verbose_name="企业号个人账号")
    wechat_tag = models.ManyToManyField(WechatTag)
    price_group = models.ForeignKey(ProductPriceGroup, null=True, blank=True, on_delete=models.SET_NULL,
                                    related_name='price_group',
                                    verbose_name='价格组')

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)