from django.contrib import admin
from .models import Target

class TargetAdmin(admin.ModelAdmin):
    # Ekranda kolonlar halinde nelerin görüneceği
    list_display = ('ip_address', 'hostname', 'vulnerability_status', 'discovered_at')
    
    # Sağ tarafa filtreleme menüsü ekler (Sadece Zafiyetlileri göster gibi)
    list_filter = ('vulnerability_status', 'discovered_at')
    
    # Üst tarafa arama çubuğu ekler (IP veya Hostname'e göre arama)
    search_fields = ('ip_address', 'hostname', 'open_ports')
    
    # Kolonlara tıklayarak detayına gitme
    list_display_links = ('ip_address', 'hostname')

# Modeli ve yeni admin ayarlarımızı sisteme kaydediyoruz
admin.site.register(Target, TargetAdmin)