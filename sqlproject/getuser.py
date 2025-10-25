import os
import sys
import django

# --- 1. Configure Django environment ---
# Adjust the path to point to your project root (the folder that has manage.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

# Replace 'myproject.settings' with your actual settings module name
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sqlproject.settings')

# Initialize Django
django.setup()

# --- 2. Import your User model ---
from django.contrib.auth import get_user_model
User = get_user_model()

# --- 3. Fetch and display users ---
print("=== Django Users ===")
for user in User.objects.all():
    print(
        f"ID: {user.id} | Username: {user.username} | "
        f"Email: {getattr(user, 'email', '')} | Superuser: {user.is_superuser}"
    )

print("=== Done ===")