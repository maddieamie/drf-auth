# magical_creatures/admin.py

from django.contrib import admin
from .models import MagicalCreature  # import your model

# Register the model
admin.site.register(MagicalCreature)
