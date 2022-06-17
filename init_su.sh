#!/bin/sh

echo "------ create default admin user ------"
echo "from django.contrib.auth.models import User; User.objects.create_superuser('jimin', 'admin@myapp.local', 'jym37557')" | python manage.py shell