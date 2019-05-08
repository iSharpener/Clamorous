from django.contrib import admin
from apps.base_info.models import BaseInformation, BindWechat
from apps.get_activity_info.commen import export_as_csv_action
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.http import HttpResponse
import csv, codecs
from django.utils.http import urlquote
from django.apps import apps

class ReadOnlyModelAdmin(admin.ModelAdmin):
    # actions = None
    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]

    def has_add_permission(self, request):
        return False

    # Allow viewing objects but not actually changing them
    def has_change_permission(self, request, obj=None):
        if request.method not in ('GET', 'HEAD'):
            return False
        return super(ReadOnlyModelAdmin, self).has_change_permission(
            request, obj)

    def has_delete_permission(self, request, obj=None):
        return True


class BaseInforAdmin(admin.ModelAdmin):
    list_display = ('stu_name', 'stu_id', 'stu_gender', 'stu_class',
                    'stu_college', 'stu_graduation')
    search_fields = ('stu_name', 'stu_college', 'stu_id', 'stu_class')
    list_filter = ["stu_college", "stu_graduation"]
    list_per_page = 50
    list_max_show_all = 50


class BaseInformationResource(resources.ModelResource):
    def __init__(self):
        super(BaseInformationResource, self).__init__()
        field_list = apps.get_model('base_info',
                                    'BaseInformation')._meta.fields
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

    # def before_import(self, dataset, using_transactions, dry_run, **kwargs):
    #     dict = []
    #     id = MoralActivity.objects.latest('id').id + 1
    #     for row in dataset.dict:
    #         tmp = row
    #         tmp['id'] = id
    #         data = MoralActivity.objects.filter(stu_id=tmp['学号']).values_list(
    #             'stu_id', 'act_name', 'id')
    #         # print(data)
    #         d_dict = {}
    #         for i in data:
    #             d_dict[i[:2]] = i[-1]

    #         if (tmp['学号'], tmp['报告名称']) in d_dict.keys():
    #             # print("ok")
    #             tmp['id'] = d_dict[(tmp['学号'], tmp['报告名称'])]

    #         else:
    #             id = id + 1
    #         dict.append(tmp)
    #     dataset.dict = dict

    class Meta:
        model = BaseInformation
        skip_unchanged = True
        report_skipped = True
        fields = ('stu_name', 'stu_id', 'stu_class', 'stu_college',
                  'stu_gender', 'stu_graduation')
        export_order = ('stu_name', 'stu_id', 'stu_gender', 'stu_class',
                        'stu_college', 'stu_graduation')


class BaseInformationAdmin(ImportExportModelAdmin):
    list_display = ('stu_name', 'stu_id', 'stu_gender', 'stu_class',
                    'stu_college', 'stu_graduation')
    search_fields = ('stu_name', 'stu_college', 'stu_id', 'stu_class')
    list_filter = ["stu_college", "stu_graduation"]
    list_per_page = 50
    list_max_show_all = 50

    actions = [
        export_as_csv_action(
            "导出Execl",
            fields=[
                'stu_name', 'stu_id', 'stu_gender', 'stu_class', 'stu_college',
                'stu_graduation'
            ])
    ]
    resource_class = BaseInformationResource


class BindWechatAdmin(ReadOnlyModelAdmin):
    list_display = ('stu_name', 'stu_id', 'stu_class', 'stu_openid')
    # actions = None


# admin.site.register(BindWechat, BindWechatAdmin)
admin.site.register(BaseInformation, BaseInformationAdmin)
