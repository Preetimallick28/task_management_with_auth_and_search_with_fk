from django.contrib import admin
from base.models import add , HistoryModel , CompleteModel

# Register your models here.
admin.site.register(add)
admin.site.register(HistoryModel)
admin.site.register(CompleteModel)