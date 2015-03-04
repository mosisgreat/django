from django.contrib import admin
from sndc.models import *

wysiwyg = ('/static/js/tiny_mce/tiny_mce.js', '/static/js/textareas.js')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class WelcomeMessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        js = wysiwyg

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name',)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')

    prepopulated_fields = {"slug": ("name",)}
    fieldsets = (
        (None, {
            'fields': ('name', 'function', 'image', 'description', 'slug', 'is_active')
        }),
        ('Reseaux sociaux', {
            'classes': ('collapse',),
            'fields': ('tweeter', 'facebook', 'pinterest', 'google')
        }),
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(WelcomeMessage, WelcomeMessageAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Team, TeamAdmin)
