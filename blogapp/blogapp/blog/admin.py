from django.contrib import admin
from .models import*

# Register your models here.


class LanguageAdmin(admin.ModelAdmin):
    # ! to display things on admin panel ! #
    list_display = ("title","is_active","is_home","image","description","slug","is_front","is_back","is_full","selected_categories")
    # ! to make things editable on admin panel ! #
    list_editable = ("is_active","is_home","is_front","is_back","is_full",)
    # ! simply put a search field above everything on admin panel ! #
    search_fields = ("title","description",)
    # ! make some areas readable only , not interractible ! #
    readonly_fields = ("slug",)
    # ! make a filter ! #
    list_filter = ("is_active","is_home","is_front","is_back","is_full",)


    # ! we define the selected category thing up there which is in list_display ! # 
    def selected_categories(self,object):
        html =""
        
        for category in object.category.all():
            html += category.name + " "
        return html



class FrameworkAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","is_home","image","description","slug","is_front","is_back","is_full",)
    list_editable = ("is_active","is_home","is_front","is_back","is_full",)
    search_fields = ("title","description","is_front","is_back","is_full",)
    readonly_fields = ("slug",)
    


class LibrariesAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","is_home","image","description","slug","is_front","is_back","is_full",)
    list_editable = ("is_active","is_home","is_front","is_back","is_full",)
    search_fields = ("title","description","is_front","is_back","is_full",)
    readonly_fields = ("slug",)



admin.site.register(Language,LanguageAdmin)


admin.site.register(Frameworks,FrameworkAdmin)


admin.site.register(Libraries,LibrariesAdmin)


admin.site.register(Category)