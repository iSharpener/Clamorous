from django.db import models


class EmployeeInfo(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    job_name = models.CharField(max_length=64)
    address = models.CharField(max_length=32)
    putdate = models.DateField()
    responsibility = models.TextField()
    telephone = models.CharField(max_length=20, blank=True, null=True)
    qualification = models.TextField(blank=True, null=True)
    e_mail = models.CharField(max_length=64, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    linkman = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.company_name

    class Meta:
        managed = False
        db_table = 'employee_info'
        verbose_name_plural = "招聘信息"