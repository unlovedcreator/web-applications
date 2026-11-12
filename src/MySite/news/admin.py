
from django.contrib import admin
from .models import News, Category, Patient, Doctor


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'spec', 'cabinet')
    list_display_links = ('name',)
    list_filter = ('spec',)


class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birth_date', 'telephone', 'diagnosis', 'doctor')
    list_display_links = ('name',)
    list_filter = ('doctor__spec',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
