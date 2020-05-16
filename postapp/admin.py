from django.contrib import admin
from .models import Post, Comment, Profile, Postlink, Postvideo, Postdocument
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Postlink)
admin.site.register(Postvideo)
admin.site.register(Postdocument)