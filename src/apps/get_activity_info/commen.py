from django.http import HttpResponse
import csv, codecs
from django.utils.http import urlquote


def export_as_csv_action(description='Export selected objects as csv file',
                         fields=None,
                         exclude=None,
                         header=True):
    def export_as_csv(modeladmin, request, queryset):
        opts = modeladmin.model._meta
        if not fields:
            field_names = [field for field in opts]
        else:
            field_names = fields

        response = HttpResponse(content_type='text/csv')
        response.write(codecs.BOM_UTF8)
        response['Content-Disposition'] = 'attachment;filename="%s"' % (
            urlquote("download.csv"))
        writer = csv.writer(response)
        if header:
            writer.writerow(field_names)
        for obj in queryset:
            # 正常的这样处理就行了
            row = [
                getattr(obj, field)()
                if callable(getattr(obj, field)) else getattr(obj, field)
                for field in field_names
            ]

            # 如果新添处理功能比如处理下时间的显示格式
            # row=[]
            # forfieldinfield_names:
            # value=getattr(obj,field)
            # ifisinstance(value,datetime.datetime):
            # value=value.'WW^sY')
            # row.append(value)

            writer.writerow(row)
        return response

    export_as_csv.short_description = description
    return export_as_csv