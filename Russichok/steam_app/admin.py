from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Genre)
admin.site.register(Game)
admin.site.register(GameGenre)
admin.site.register(Library)
admin.site.register(Friendship)
admin.site.register(Balance)
admin.site.register(Media)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostComment)
admin.site.register(Review)
admin.site.register(ReviewComment)
