

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.models import User
from users.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user','phone_number', 'website', 'picture') # para ver en el admin esta información en la lista de los perfiles
    list_display_links = ('pk','user') # para que se enlace cada valor de la lista a la ventana de detalle para poder editarlo
    list_editable = ('phone_number','website','picture') # esto hace los valores editables desde la lista
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name', 
        'user__last_name',
        'phone_number'
    ) # Este es para añadir una barra de busqueda

    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified'        
    ) # para agregar filtros a la busqueda


    ## Vamos a ampliar el detalle del modelo profile como el de user

    fieldsets = (
        ('profile',{
            'fields':(('user','picture'),),
        }),
        ('Extra info',{
            'fields': (
                ('website','phone_number'),
                ('biography',)
            )
        }),
        ('Metadata',{
            'fields':(('created', 'modified'),)
        }
        )
    )
    readonly_fields = ('created','modified')

    ## Vamos ahora a extender el modelo de usuario para conectar el profile con el user y hacer todo una sola vez y no tener que crear primero el usuario y despues el profile

class ProfileInline(admin.StackedInline):

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin"""
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'

    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)