from django.contrib import admin

# Register your models here.
from . models import SchoolType, User, state_province, School, Ratings

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Score', 'Address', 'get_State', 'Phone', 'get_typeName')
    list_filter = ('Name', 'Score', 'State_Province', 'Type')
    fields = ['Name', ('ImageMD', 'ImageProfile'), 'Address', 'State_Province', 'Phone', 'Type', 'Review']
    
    # def get_typeName(self, obj):
    #     return obj.Type.Description
    # get_typeName.short_description = 'Tipo Establecimiento'
    def get_State(self, obj):
        return obj.State_Province.NameSP
    get_State.short_description = 'Comuna'

    def get_typeName(self, obj):
        return obj.Type.Description
    #     return ', '.join([ Type.Description for Typedescription in self.Type.all()[:3] ])
    # return ', '.join([ User.Email for User in self.User.all()[:3] ])
    get_typeName.short_description = 'Tipo Establecimiento'

admin.site.register(School, SchoolAdmin)

class SchoolTypeAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Description')

admin.site.register(SchoolType, SchoolTypeAdmin)

class StateProviceAdmin(admin.ModelAdmin):
    list_display = ('Id', 'get_name')
    
    def get_name(self, obj):
        return obj.NameSP
    get_name.short_description = 'Nombre Comuna'


admin.site.register(state_province, StateProviceAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('get_name','Email', 'Phone')

    def get_name(self, obj):
        return(obj.Name+' '+obj.Last_Name)

    get_name.short_description = 'Nombre'

admin.site.register(User, UserAdmin)

class RatingAdmin(admin.ModelAdmin):
    # list_display = ('get_email','get_user','Score', 'display_School') 
    list_display = ('get_email','get_user','Score', 'display_School') 
    list_filter = ('User', 'Score', 'Schools')
admin.site.register(Ratings, RatingAdmin)