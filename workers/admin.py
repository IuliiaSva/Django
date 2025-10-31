from django.contrib import admin

from .models import Images, Worker


class ImageInline(admin.TabularInline):
    model = Images
    extra = 1


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ("name", "date_of_joining", "gender", "skills",
                    "grade", "description", "workplace")
    list_editable = ("skills", "grade", "description", "workplace")
    search_fields = ("gender", "name", "skills",
                     "grade", "description", "workplace")
    list_filter = (
        "gender",
        "grade",
    )
    list_display_links: ()
    inlines = (ImageInline, )
