from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserMedia)
admin.site.register(UserCategories)
admin.site.register(Artwork)
admin.site.register(ArtworkView)
