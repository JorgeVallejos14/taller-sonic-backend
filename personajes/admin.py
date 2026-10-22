from django.contrib import admin
from .models import Personaje, Producto

# Register your models here.
admin.site.site_header = "Administración de personajes"

class ProductoInline(admin.TabularInline):
    model = Personaje
    extra = 1
    fields = ("nombre", "poder", "especial")
    show_change_link = True

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "especie", "catalogo")
    list_filter = ("catalogo",)
    search_fields = ("nombre", "especie", "catalogo__nombre")
    ordering = ("nombre",)
    inlines = [ProductoInline]

    @admin.display(description="Nombre del personaje")
    def total_productos(self, obj):
        return obj.productos.count()
    
@admin.register(Personaje)
class PersonajeAdmin(admin.ModelAdmin):
    list_display = ("nombre", "poder", "especial", "total_productos")
    search_fields = ("nombre", "poder")
    ordering = ("nombre",)
    list_editable = ("poder", "especial")
    list_select_related = ("productos",)
    actions = ["duplicar_personaje"]

    fieldsets = (
        ("Información básica")
    )