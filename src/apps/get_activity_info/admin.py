from django.contrib import admin
from apps.get_activity_info.models import SignUpInfo, ParticipationRecord, MoralActivity, AcademicReport
from django.contrib.auth.models import Group, User
from apps.get_activity_info.commen import export_as_csv_action
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.http import HttpResponse
import csv, codecs
from django.utils.http import urlquote
from django.apps import apps

# Register your models here.


class SignUpInfoResource(resources.ModelResource):
    def __init__(self):
        super(SignUpInfoResource, self).__init__()
        field_list = apps.get_model('get_activity_info',
                                    'SignUpInfo')._meta.fields
        self.vname_dict = {}
        for i in field_list:
            self.vname_dict[i.name] = i.verbose_name

    def get_export_fields(self):
        fields = self.get_fields()
        for field in fields:
            field_name = self.get_field_name(field)
            # 如果我们设置过verbose_name，则将column_name替换为verbose_name。否则维持原有的字段名
            if field_name in self.vname_dict.keys():
                field.column_name = self.vname_dict[field_name]
        return fields

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        dict = []
        id = SignUpInfo.objects.latest('id').id + 1
        for row in dataset.dict:
            tmp = row
            tmp['id'] = id

            data = SignUpInfo.objects.filter(stu_id=tmp['学号']).values_list(
                'stu_id', 'act_name', 'stu_status', 'id')
            # print(data)
            d_dict = {}
            for i in data:
                d_dict[i[:3]] = i[-1]

            if (tmp['学号'], tmp['活动名称'], tmp['参与身份']) in d_dict.keys():
                # print("ok")
                tmp['id'] = d_dict[(tmp['学号'], tmp['活动名称'], tmp['参与身份'])]
                # print(tmp['id'])

            else:
                id = id + 1
            dict.append(tmp)
        dataset.dict = dict

    class Meta:
        model = SignUpInfo
        skip_unchanged = True
        report_skipped = True
        fields = ('stu_name', 'stu_id', 'stu_class', 'act_name', 'stu_status',
                  'act_score', 'act_time', 'id')
        export_order = ('stu_name', 'stu_id', 'stu_class', 'act_name',
                        'stu_status', 'act_time', 'act_score')


class SignUpInfoAdmin(ImportExportModelAdmin):
    list_display = ('stu_name', 'stu_id', 'stu_class', 'act_name',
                    'stu_status', 'act_score', 'act_time')
    search_fields = ('stu_name', 'act_name', 'stu_id', 'act_time')
    list_filter = ["act_name"]
    date_hierarchy = 'act_time'
    actions = [
        export_as_csv_action(
            "导出Execl",
            fields=[
                'stu_name', 'stu_id', 'stu_class', 'act_name', 'stu_status',
                'act_score', 'act_time'
            ])
    ]
    resource_class = SignUpInfoResource


class ParticipationRecordResource(resources.ModelResource):
    def __init__(self):
        super(ParticipationRecordResource, self).__init__()
        field_list = apps.get_model('get_activity_info',
                                    'ParticipationRecord')._meta.fields
        self.vname_dict = {}
        for i in field_list:
            self.vname_dict[i.name] = i.verbose_name

    def get_export_fields(self):
        fields = self.get_fields()
        for field in fields:
            field_name = self.get_field_name(field)
            # 如果我们设置过verbose_name，则将column_name替换为verbose_name。否则维持原有的字段名
            if field_name in self.vname_dict.keys():
                field.column_name = self.vname_dict[field_name]
        return fields

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        dict = []
        id = ParticipationRecord.objects.latest('id').id + 1
        for row in dataset.dict:
            tmp = row
            tmp['id'] = id
            data = ParticipationRecord.objects.filter(
                stu_id=tmp['学号']).values_list('stu_id', 'act_name',
                                              'stu_status', 'id')
            # print(data)
            d_dict = {}
            for i in data:
                d_dict[i[:3]] = i[-1]

            if (tmp['学号'], tmp['活动名称'], tmp['参与身份']) in d_dict.keys():
                # print("ok")
                tmp['id'] = d_dict[(tmp['学号'], tmp['活动名称'], tmp['参与身份'])]

            else:
                id = id + 1
            dict.append(tmp)
        dataset.dict = dict

    class Meta:
        model = ParticipationRecord
        skip_unchanged = True
        report_skipped = True
        fields = ('stu_name', 'stu_id', 'stu_class', 'act_name', 'stu_status',
                  'act_score', 'act_time', 'stu_rank', 'id')
        export_order = ('stu_name', 'stu_id', 'stu_class', 'act_name',
                        'stu_status', 'act_time', 'act_score', 'stu_rank')


class ParticipationRecordAdmin(ImportExportModelAdmin):
    list_display = ('stu_name', 'stu_id', 'stu_class', 'act_name',
                    'stu_status', 'act_score', 'act_time', 'stu_rank')
    list_editable = ["act_score"]
    search_fields = ('stu_name', 'act_name', 'stu_id', 'act_time')
    list_filter = ["act_name"]
    date_hierarchy = 'act_time'
    ordering = ('-act_time', )
    actions = [
        export_as_csv_action(
            "导出Execl",
            fields=[
                'stu_name', 'stu_id', 'stu_class', 'act_name', 'stu_status',
                'act_score', 'act_time', 'stu_rank'
            ])
    ]
    resource_class = ParticipationRecordResource


class MoralActivityResource(resources.ModelResource):
    def __init__(self):
        super(MoralActivityResource, self).__init__()
        field_list = apps.get_model('get_activity_info',
                                    'MoralActivity')._meta.fields
        self.vname_dict = {}
        for i in field_list:
            self.vname_dict[i.name] = i.verbose_name

    def get_export_fields(self):
        fields = self.get_fields()
        for field in fields:
            field_name = self.get_field_name(field)
            # 如果我们设置过verbose_name，则将column_name替换为verbose_name。否则维持原有的字段名
            if field_name in self.vname_dict.keys():
                field.column_name = self.vname_dict[field_name]
        return fields

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        dict = []
        id = MoralActivity.objects.latest('id').id + 1
        for row in dataset.dict:
            tmp = row
            tmp['id'] = id
            data = MoralActivity.objects.filter(stu_id=tmp['学号']).values_list(
                'stu_id', 'act_name', 'id')
            # print(data)
            d_dict = {}
            for i in data:
                d_dict[i[:2]] = i[-1]

            if (tmp['学号'], tmp['活动名称']) in d_dict.keys():
                # print("ok")
                tmp['id'] = d_dict[(tmp['学号'], tmp['活动名称'])]

            else:
                id = id + 1
            dict.append(tmp)
        dataset.dict = dict

    class Meta:
        model = MoralActivity
        skip_unchanged = True
        report_skipped = True
        fields = ('stu_name', 'stu_id', 'stu_class', 'act_name', 'act_score',
                  'act_time', 'id')
        export_order = ('stu_name', 'stu_id', 'stu_class', 'act_name',
                        'act_time', 'act_score')


class MoralActivityAdmin(ImportExportModelAdmin):
    list_display = ('stu_name', 'stu_id', 'stu_class', 'act_name', 'act_score',
                    'act_time')
    list_editable = ["act_score"]
    search_fields = ('stu_name', 'act_name', 'stu_id', 'act_time')
    list_filter = ["act_name"]
    date_hierarchy = 'act_time'
    ordering = ('-act_time', )
    actions = [
        export_as_csv_action(
            "导出Execl",
            fields=[
                'stu_name', 'stu_id', 'stu_class', 'act_name', 'act_score',
                'act_time'
            ])
    ]
    resource_class = MoralActivityResource


class AcademicReportResource(resources.ModelResource):
    def __init__(self):
        super(AcademicReportResource, self).__init__()
        field_list = apps.get_model('get_activity_info',
                                    'AcademicReport')._meta.fields
        self.vname_dict = {}
        for i in field_list:
            self.vname_dict[i.name] = i.verbose_name

    def get_export_fields(self):
        fields = self.get_fields()
        for field in fields:
            field_name = self.get_field_name(field)
            # 如果我们设置过verbose_name，则将column_name替换为verbose_name。否则维持原有的字段名
            if field_name in self.vname_dict.keys():
                field.column_name = self.vname_dict[field_name]
        return fields

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        dict = []
        id = MoralActivity.objects.latest('id').id + 1
        for row in dataset.dict:
            tmp = row
            tmp['id'] = id
            data = MoralActivity.objects.filter(stu_id=tmp['学号']).values_list(
                'stu_id', 'act_name', 'id')
            # print(data)
            d_dict = {}
            for i in data:
                d_dict[i[:2]] = i[-1]

            if (tmp['学号'], tmp['报告名称']) in d_dict.keys():
                # print("ok")
                tmp['id'] = d_dict[(tmp['学号'], tmp['报告名称'])]

            else:
                id = id + 1
            dict.append(tmp)
        dataset.dict = dict

    class Meta:
        model = AcademicReport
        skip_unchanged = True
        report_skipped = True
        fields = ('stu_name', 'stu_id', 'stu_class', 'act_name', 'act_time',
                  'id')
        export_order = ('stu_name', 'stu_id', 'stu_class', 'act_name',
                        'act_time')


class AcademicReportAdmin(ImportExportModelAdmin):
    list_display = ('stu_name', 'stu_id', 'stu_class', 'act_name', 'act_time')
    search_fields = ('stu_name', 'act_name', 'stu_id', 'act_time')
    list_filter = ["act_name"]
    date_hierarchy = 'act_time'
    ordering = ('-act_time', )
    actions = [
        export_as_csv_action(
            "导出Execl",
            fields=['stu_name', 'stu_id', 'stu_class', 'act_name', 'act_time'])
    ]
    resource_class = AcademicReportResource


admin.site.register(SignUpInfo, SignUpInfoAdmin)
admin.site.register(ParticipationRecord, ParticipationRecordAdmin)
admin.site.register(MoralActivity, MoralActivityAdmin)
admin.site.register(AcademicReport, AcademicReportAdmin)

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.site_header = '研究生培养信息后台管理系统'
admin.site.site_title = '后台管理'
admin.site.index_title = '后台站点管理'
