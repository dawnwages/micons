from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from .models import (Brand, Sku, Color, Processor, Os, Memory, Hd, Ss)

class ProcessorAdmin(ModelAdmin):
    model = Processor
    menu_label = 'Processor Model'  # ditch this to use verbose_name_plural from model
    menu_icon = 'snippet'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('author', 'title', 'created_date', 'published_date')
   # list_filter = ('author', 'title', 'created_date', 'published_date')
    search_fields = ('title')
    
class OsAdmin(ModelAdmin):
    model = Os
    menu_label = 'Operating System Model'  # ditch this to use verbose_name_plural from model
    menu_icon = 'snippet'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('author', 'title', 'created_date', 'published_date')
   # list_filter = ('author', 'title', 'created_date', 'published_date')
    search_fields = ('title')
    
class MemoryAdmin(ModelAdmin):
    model = Memory
    menu_label = 'Memory Model'  # ditch this to use verbose_name_plural from model
    menu_icon = 'snippet'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('author', 'title', 'created_date', 'published_date')
   # list_filter = ('author', 'title', 'created_date', 'published_date')
    search_fields = ('title')
    
class HdAdmin(ModelAdmin):
    model = Hd
    menu_label = 'Hard Drive Model'  # ditch this to use verbose_name_plural from model
    menu_icon = 'snippet'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('author', 'title', 'created_date', 'published_date')
   # list_filter = ('author', 'title', 'created_date', 'published_date')
    search_fields = ('title')
    
class SsAdmin(ModelAdmin):
    model = Ss
    menu_label = 'Hard Drive Model'  # ditch this to use verbose_name_plural from model
    menu_icon = 'snippet'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('author', 'title', 'created_date', 'published_date')
   # list_filter = ('author', 'title', 'created_date', 'published_date')
    search_fields = ('title')
    
    
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
    
class ColorAdmin(ModelAdmin):
    model = Color
    menu_label = 'Color Model'  # ditch this to use verbose_name_plural from model
    menu_icon = 'snippet'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('author', 'title', 'created_date', 'published_date')
   # list_filter = ('author', 'title', 'created_date', 'published_date')
    search_fields = ('title')
    

#STILL DOESNT WORK - WTF -- I needed to makemigrations and migrate. you dummy! Fixed
class SkuAdmin(ModelAdmin):
    model = Sku
    menu_label = 'Sku Model'  # ditch this to use verbose_name_plural from model
    menu_icon = 'snippet'  # change as required
    menu_order = 100  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('author', 'title', 'article', 'friendly_name', 'country_choice', 'status_choices', 'type_choices', 'sku_link', 'processor_choice', 'os_choice',  'memory_choice', 'hd_choice', 'display_choice', 'ss_choice', 'color_choice', 'price_choice', 'created_date', 'live_date')
   # list_filter = ('author', 'title', 'created_date', 'published_date')
    search_fields = ('title')
    
modeladmin_register(SkuAdmin)


class MyModelAdminGroup(ModelAdminGroup):
    menu_label = 'Product Features'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (ProcessorAdmin, MemoryAdmin, OsAdmin, HdAdmin, BrandAdmin, ColorAdmin, SsAdmin)
    
modeladmin_register(MyModelAdminGroup)