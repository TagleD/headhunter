from django.contrib import admin

from applicants.models import Resume


# Register your models here.
class ResumeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'applicant', 'full_name',
        'position', 'salary', 'about',
        'telegram', 'facebook', 'linkedin',
        'is_published'
    )
    list_filter = (
        'id', 'applicant', 'full_name',
        'position', 'salary', 'about',
        'telegram', 'facebook', 'linkedin',
        'is_published'
    )
    search_fields = (
        'id', 'applicant', 'full_name',
        'position', 'salary', 'about',
        'telegram', 'facebook', 'linkedin',
        'is_published'
    )
    fields = (
        'id', 'applicant', 'full_name',
        'position', 'salary', 'about',
        'telegram', 'facebook', 'linkedin',
        'is_published'
    )
    readonly_fields = ('id',)


admin.site.register(Resume, ResumeAdmin)
