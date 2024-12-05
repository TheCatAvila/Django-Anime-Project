from django.contrib import admin
from .models import User

# Personalización del admin para Persona
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'passhash', 'register_at')  
    search_fields = ('username',)  

# Registrar los modelos en el panel de administración
admin.site.register(User, UsersAdmin)
