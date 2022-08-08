from typing import Sequence
from django.contrib import admin
from .models import Alumnos
from .models import Comentario
from .models import ComentarioContacto

class AdministarModelo(admin.ModelAdmin):
    readonly_fields: Sequence[str] = ('created', 'update')
    list_display = ('matricula', 'nombre', 'carrera', 'turno', 'created')
    search_fields: Sequence[str] = ('matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy = 'created'
    list_filter = ('carrera','turno')
    list_per_page=2
    list_display_links=('matricula', 'nombre')
    list_editable=('turno',)

    def get_readonly_fields(self, request, obj=None):
        #si el usuario pertenece al grupo de permisos "Usuario"
        if request.user.groups.filter(name="Usuario").exists():
            #Bloquea los campos
            return ('matricula', 'carrera', 'turno')
        #Caulquier otro usuario que no pertenece al grupo "Usuario"
        else: 
            #Bloquea los campos
            return('created', 'update')

admin.site.register(Alumnos, AdministarModelo)

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id','coment')
    search_fields: Sequence[str] = ('id','created')
    date_hierarchy = 'created'
    readonly_fields: Sequence[str] = ('created', 'id')
    
admin.site.register(Comentario, AdministrarComentarios)


class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id','usuario','mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields: Sequence[str] = ('created', 'id')
    
admin.site.register(ComentarioContacto, AdministrarComentariosContacto)