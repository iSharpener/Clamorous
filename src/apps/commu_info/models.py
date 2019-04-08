from django.db import models

class CommuInformation(models.Model):
    stu_id = models.CharField(primary_key=True, max_length=255)
    telephone_num = models.CharField(max_length=20)
    qq_num = models.CharField(max_length=20, blank=True, null=True)
    weixin = models.CharField(max_length=50, blank=True, null=True)
    commu_address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.stu_id
    class Meta:
        managed = False
        db_table = 'commu_information'
        verbose_name_plural = '用户联系信息'

class UserOnlineInfo(models.Model):
    stu_id = models.CharField(primary_key=True, max_length=12)
    online_status = models.CharField(max_length=1)
    token = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.stu_id
    class Meta:
        managed = False
        db_table = 'user_online_info'
        verbose_name_plural = '用户在线信息'