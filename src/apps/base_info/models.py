from django.db import models

class BaseInformation(models.Model):
    stu_id = models.CharField(primary_key=True, max_length=12)
    stu_name = models.CharField(max_length=20)
    name_piyin = models.CharField(max_length=20, blank=True, null=True)
    english_name = models.CharField(max_length=50, blank=True, null=True)
    used_name = models.CharField(max_length=20, blank=True, null=True)
    stu_gender = models.CharField(max_length=5)
    nation = models.CharField(max_length=20)
    native_place = models.CharField(max_length=20, blank=True, null=True)
    document_type = models.CharField(max_length=20)
    id_number = models.CharField(max_length=20)
    birth_day = models.DateField(blank=True, null=True)
    enroll_day = models.DateField(blank=True, null=True)
    political_outlook = models.CharField(max_length=32, blank=True, null=True)
    reg_residence = models.CharField(max_length=32, blank=True, null=True)
    biogenic_land = models.CharField(max_length=32, blank=True, null=True)
    birth_place = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.stu_name
    class Meta:
        managed = False
        db_table = 'base_information'
        verbose_name_plural = '用户基础信息'