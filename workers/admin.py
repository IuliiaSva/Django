from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Worker


#class WorkerResource(resources.ModelResource):
#    def for_delete(self, row, instance):
#        return row['delete']=='1'
#    class Meta:
#        model = Worker


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('gender','name', 'skills', 'grade', 'discription', 'workplace')
    list_editable = ('skills', 'grade', 'discription', 'workplace')
    search_fields = ('gender','name', 'skills', 'grade', 'discription', 'workplace')
    list_filter = ('gender','grade',)
    list_display_links: tuple= ('name',)
#class WorkerAdmin(admin.ModelAdmin):
 #    resource_class = WorkerResource


# Register your models here.
