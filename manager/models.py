# Create your models here.
from django.db import models


class Manager(models.Model):
    # 管理员Id
    id = models.AutoField(primary_key=True)
    # 管理员姓名
    name = models.CharField(max_length=20, null=False, verbose_name='姓名')
    # 管理员性别
    sex = models.IntegerField(choices=[(0, '男'), (1, '女')], verbose_name='性别')
    # 管理员手机号码
    phone_number = models.TextField(max_length=11, unique=True, verbose_name='手机号码')
    # 管理员邮箱
    email = models.EmailField(unique=True,verbose_name='邮箱')
    # 管理员权限类型
    privilege = models.IntegerField(choices=[(0, '超级管理员'), (1, '管理员')], verbose_name='权限')


class Tourist(models.Model):
    # 游客用户名称
    username = models.CharField(max_length=20, null=False, verbose_name='用户名')
    # 游客用户密码
    password = models.TextField(max_length=128, null=False, verbose_name='密码')
    # 游客姓名
    name = models.CharField(max_length=30, null=False, verbose_name='姓名')
    # 游客性别
    sex = models.IntegerField(choices=[(0, '男'), (1, '女')], verbose_name='性别')
    # 游客手机号码
    phone_number = models.TextField(max_length=11, unique=True, verbose_name='手机号码')
    # 游客邮箱
    email = models.EmailField(unique=True, verbose_name='邮箱')
    # 游客游玩状态
    status = models.IntegerField(choices=[(0, '游玩中'), (1, '排队中'), (2, '闲逛中')], verbose_name='状态')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["username"]
        verbose_name = "游客"
        verbose_name_plural = "游客"
    # Tourist = models.ForeignKey(Project,on_delete=models.CASCADE())
    @classmethod
    def create(cls, username, password, name, sex):
        pass


class Project(models.Model):
    # 项目名称
    name = models.CharField(max_length=30, null=False, verbose_name='项目名称')
    # 项目状态
    status = models.IntegerField(choices=[(0, '可用'), (1, '不可用')], verbose_name='状态')
    # 项目最大人数
    # max_number = models.
    #
    pass
