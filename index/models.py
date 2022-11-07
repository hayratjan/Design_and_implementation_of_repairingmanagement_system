from datetime import datetime

from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe


# Create your models here.
class User(models.Model):
    choices = ((1, '男'), (2, '女'), (3, '其他'))
    choices_type = ((1, '学生'), (2, '宿管'), (3, '管理员'), (4, '停用'))
    id = models.AutoField(verbose_name="id", primary_key=True)
    name = models.CharField(verbose_name="姓名", max_length=22, default='')
    gender = models.IntegerField(verbose_name="性别", choices=choices)
    password = models.CharField(verbose_name="密码", max_length=34, default='')
    phone = models.CharField(verbose_name="手机号", max_length=18, default='')
    email = models.CharField(verbose_name="邮箱", max_length=30, default='')
    time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    photo = models.FileField(verbose_name="图片", default='', upload_to="user/photo/")
    type = models.IntegerField(verbose_name="状态", choices=choices_type, default=True)

    def admin_sample(self):
        return mark_safe('<img src="/media/%s" height="60" width="40" />' % (self.photo,))

    admin_sample.short_description = '图片'

    def __str__(self):
        return self.name

    class Meta:
        # 数据库列表名
        db_table = 'User'
        # 后台管理名
        verbose_name_plural = '用户管理'


class Repair(models.Model):
    choices = ((1, '已提交'), (3, '待修复'), (4, '已修复'), (5, '失败！'))
    id = models.AutoField(verbose_name="id", primary_key=True)
    user = models.ForeignKey(to='User', on_delete=models.CASCADE, verbose_name='提交用户', default='')
    # audit_user = models.ForeignKey(to='User', on_delete=models.CASCADE, verbose_name="审核人", null=True)
    single = models.CharField(verbose_name="单号", max_length=28, default='')
    flor = models.CharField(verbose_name="楼号", max_length=18, default='')
    title = models.CharField(verbose_name="主题", max_length=60, default='')
    content = models.TextField(verbose_name="内容")
    time = models.DateTimeField(verbose_name="创建时间", default=datetime.now)
    photo = models.FileField(verbose_name="图片", default='', upload_to="Repair/photo/")
    type = models.IntegerField(verbose_name="状态", choices=choices, default=True)

    def __str__(self):
        return self.title
    def admin_sample(self):
        return mark_safe('<img src="/media/%s" height="60" width="40" />' % (self.photo,))

    admin_sample.short_description = '图片'

    class Meta:
        # 数据库列表名
        db_table = 'Repair'
        # 后台管理名
        verbose_name_plural = '保修单'


class Notice(models.Model):
    choices = ((1, '活跃'), (2, '已删除'))
    id = models.AutoField(verbose_name="id", primary_key=True)
    title = models.CharField(verbose_name="主题", max_length=60, default='')
    content = models.TextField(verbose_name="内容")
    time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    type = models.IntegerField(verbose_name="状态", choices=choices, default=True)

    def __str__(self):
        return self.title

    class Meta:
        # 数据库列表名
        db_table = 'Notice'
        # 后台管理名
        verbose_name_plural = '通知内容'
