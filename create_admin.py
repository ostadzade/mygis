# در فایل create_admin.py در پوشه اصلی
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mygis.settings')
import django
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'password123')
    print("Superuser created successfully!")
else:
    print("Superuser already exists!")