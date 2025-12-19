from django.contrib import admin
from .models import Certificate


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'certificate_id',
        'course',
        'issue_date',
        'is_valid'
    )

    search_fields = (
        'full_name',
        'certificate_id',
        'course'
    )

    list_filter = (
        'course',
        'is_valid',
        'issue_date'
    )
