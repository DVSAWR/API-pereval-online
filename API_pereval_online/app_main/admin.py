from django.contrib import admin

from .models import CustomUser, Coords, Post, Images

admin.site.register(CustomUser)
admin.site.register(Coords)
admin.site.register(Post)
admin.site.register(Images)
