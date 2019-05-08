from django.db import models


class BaseInformation(models.Model):
    stu_id = models.CharField('学号', primary_key=True, max_length=12)
    stu_name = models.CharField('姓名', max_length=20)
    stu_class = models.CharField('班级', max_length=20)
    stu_college = models.CharField('学院', max_length=30)
    stu_gender = models.CharField('性别', max_length=5)
    stu_graduation = models.BooleanField('是否今年毕业', default=0)

    def __str__(self):
        return self.stu_name

    class Meta:
        managed = False
        db_table = 'base_information'
        verbose_name_plural = '学生信息'
        verbose_name = '学生信息'


class BindWechat(models.Model):
    stu_name = models.CharField('姓名', max_length=20)
    stu_class = models.CharField('班级', max_length=20)
    stu_id = models.CharField('学号', primary_key=True, max_length=12)
    stu_openid = models.CharField('绑定的微信号', max_length=50)

    def __str__(self):
        return self.stu_name

    class Meta:
        managed = False
        db_table = 'bind_wechat'
        verbose_name_plural = '微信绑定信息'
        verbose_name = '微信绑定'
