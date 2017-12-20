from django.contrib import admin
from publishers.models import Publisher, Category


class CategoryAdmin(admin.ModelAdmin):
    pass
# Register your models here.


class PublisherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Publisher, PublisherAdmin)
