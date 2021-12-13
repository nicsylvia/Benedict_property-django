from django.contrib import admin
from Alabian_app.models import *

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}

admin.site.register(ProductCategory)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('teamMember_name',)}

