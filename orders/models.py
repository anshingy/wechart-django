from django.db import models
from mall.models import Product
from login.models import Profile


# 订单数据
class Order(models.Model):
    user = models.ForeignKey(Profile, related_name='items', null=True,
                             on_delete=models.SET_NULL, verbose_name='用户')
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # email = models.EmailField()
    # address = models.CharField(max_length=250)
    # postal_code = models.CharField(max_length=20)  # 邮政编码
    # city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    paid = models.BooleanField(default=False, verbose_name='是否支付')  # 区分支付和未支付
    send = models.BooleanField(default=False, verbose_name='是否发货')  # 是否发货
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')  # FALSE时表示未删除，True表示改订单删除了。
    description = models.TextField(verbose_name='订单描述', blank=True, null=True)  # 订单描述,为管理员时使用
    total_cost = models.CharField(max_length=20, verbose_name='订单金额')  # 订单金额

    class Meta:
        ordering = ('-created',)  # 按创建时间倒叙排列
        verbose_name = 'Orders'
        verbose_name_plural = '订单'

    def __str__(self):
        return '订单号 {}'.format(self.id)

    # 订单中购买物品的总花费。
    def get_total_cost(self):
        # self.items = OrderItem.objects.filter(order=)
        return sum(item.get_cost() for item in self.items.all())   # 不知道为什么可以？？？没用items啊


# 订单中的商品信息
# 保存物品，数量和每个物品的支付价格。
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', null=True,
                              on_delete=models.SET_NULL,
                              verbose_name='订单')
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                null=True,
                                on_delete=models.SET_NULL,
                                verbose_name='产品'
                                )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='单价')
    quantity = models.PositiveIntegerField(default=1, verbose_name='数量')

    def __str__(self):
        return '{}'.format(self.id)

    # 返回物品的花费
    def get_cost(self):
        return self.price * self.quantity


# （一天）内的订单每样产品的数量统计表
class OrderStatistics(models.Model):
    date = models.DateField(verbose_name='统计日期')
    product = models.ForeignKey(Product,
                                null=True,
                                on_delete=models.SET_NULL,
                                verbose_name='产品'
                                )
    quantity = models.PositiveIntegerField(verbose_name='数量')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='金额')

    class Meta:
        verbose_name = '订单统计'

    def __str__(self):
        return '{}'.format(self.id)
