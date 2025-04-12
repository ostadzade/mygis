# gis_app/views.py

from django.shortcuts import render

def map_view(request):
    # می‌توانید داده‌های مورد نیاز برای نقشه را اینجا آماده کنید
    context = {
        'map_title': 'نقشه سیستم GIS من'
    }
    return render(request, 'gis_app/map.html', context)