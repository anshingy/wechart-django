# wechart-django
用于微信服务号

### 2019年7月4日
1.增加报表导出功能，`Manager/views.py 下的 export_to_csv(request)函数`
2.新增一个网页，用于管理员查看金额页面，导出功能；`def order_list_cost`
3.优化了查询数据库和导出csv
### 2019年7月5日
~~1.提交订单、管理页面、微信发送、导出cvs，增加了订单描述.~~
2.todo新增一个页面用于展示未发货，管理员用于确认发货，添加运费，默认为0；
_3.bug手机管理页面选全部时导出为空（处理不了）_
### 2019年7月6日
1.todo 折线图展示默认最近7天的用户每样产品的购物情况，与总量的情况，添加可选时间段，导出功能
2. 每天定时统计发送数据
### 2019年7月23日
1.添加页面，统计当天提交的订单，
~~2.mall页面，css区分电脑展示和手机展示。~~
### 2019年7月24日
1.添加展示并下载Excel，15天采购清单的页面*（比较困难，暂时不做）*
~~2.添加manager含金额导出2，用于统计,删除login.model profile~~
### 2019年7月25日
`1.单独开个界面用于看我的订单(不需要了，用权限进行控制)`
~~2.使订单金额根据内容不固定~~
~~3.admin后台订单添加订单描述~~
~~4.增加个界面，选择店铺，输入字符串，判断自动完成订单。~~
~~5.今日订单最上面加一个总订单数~~
~~6.订单提交html加一个判断，判断是否有提交订单权限。~~
~~7.帮助页面增加使用帮助，如何添加到桌面，如何采购，如何查看微信信息。~~
### 2019年7月25日
~~1.bug 刷新会重复提交~~
~~2.管理员下单微信通知~~
~~3.再增加一个页面，用于添加全名称匹配的其他商品。（直接admin，后台添加可以。）~~
~~4.admin product 按品类进行筛选~~
### 2019年7月28日
~~1.帮助页面增加资料等招牌门面信息文件。~~
~~2.帮助页面增加到主页链接上。~~
~~3.修改未支付超过30天，禁止采购。(数据库中修改)~~
### 2019年7月28日
~~1.用户profile admin 添加搜索功能，product 添加搜索~~
2.用户2，inline user( 样式会变，暂时不弄了)。
### 2019年8月4日
~~1.添加上次订单页面~~
2.添加库存管理，酵母，打包袋袋等，设置阈值通知，低于这个阈值发送微信警告。
### 2019年8月8日
~~1.添加一个统计页面，展示一个店铺，一段时间，表。~~
### 2019年8月11日
~~1.图表展示统计页面~~
~~2.每天金额折线图~~
~~3.用户为全部时，展示每种材料金额占比饼状图，店铺金额饼状图，店铺金额条状图~~
### 2019年8月11日
1.手机导航栏样式修改,(有点难，暂时不修改)
~~2.个人已发货未支付订单报表页。~~~~修改我的订单最上面统计的为，已发货，未支付的金额。~~
~~3.管理员查看已发货未支付订单报表与清单。~~
~~4.手机店铺统计表样式修改。~~
### 2019年8月17日
~~1.运费订单模版，下单时自动加入到订单里。~~
~~2.今日订单，打印样式设置。~~
~~3.统计表，不选时间，默认展示最近15天的数据~~
~~4.价格组改成部门，内部员工，金华配送，其他地区。~~
~~5.过滤条件，前面再加个选项，部门。 (改成根据部门进行排序)~~
### 2019年8月18日
~~1.新建个页面，展示所有用户的订单报表。~~
~~2.修改了order tasks.py。关闭了计划任务。修改了微信发送总金额。~~
~~3.表格展示最近七天的用户，每天用户订单状况。表格展示。row 日期，column 店铺。
大于三天的，如果今天没有，做标记提示。等于三天的，判断前一天有没。~~
### 2019年8月20日
~~1.品类添加字段序号，用于排序。~~
~~2.产品加个字段序号，用于排序~~
### 2019年8月26日
1.增加个页面用于确认未发货的订单进行确认是否发货。js全选，取消全选
2.增加个页面用于管理员确认支付，报表页面。一定要超级管理员权限。
### 2019年9月4日
~~1.统计每天的每样材料的数量~~
~~2.每个店铺馅料的金额~~
