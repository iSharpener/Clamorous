from django.db import models

class CampusHireInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.CharField(max_length=20, blank=True, null=True)
    style = models.CharField(max_length=32, blank=True, null=True)
    detail_url = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    md5 = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'campus_hire_info'
        verbose_name_plural = '校园招聘信息'

class PartyBuildingInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.CharField(max_length=20, blank=True, null=True)
    style = models.CharField(max_length=32, blank=True, null=True)
    detail_url = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    md5 = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'party_building_info'
        verbose_name_plural = '党建信息'

class ResearchInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    day = models.CharField(max_length=20, blank=True, null=True)
    style = models.CharField(max_length=32, blank=True, null=True)
    month = models.CharField(max_length=16, blank=True, null=True)
    detail_url = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    md5 = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'research_info'
        verbose_name_plural = '科研成果信息'