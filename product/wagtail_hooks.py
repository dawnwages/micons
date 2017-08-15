from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from .models import Brand


class BrandAdmin(ModelAdmin):
    model = Brand
    menu_label = 'Brand Model'  # ditch this to use verbose_name_plural from model
    menu_icon = 'snippet'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('author', 'title', 'created_date', 'published_date')
   # list_filter = ('author', 'title', 'created_date', 'published_date')
    search_fields = ('title')
    
modeladmin_register(BrandAdmin)