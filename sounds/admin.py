from django.contrib import admin
from . models import Subscribe, Post, AudioMessages, Letter,Poems

admin.site.register(Post)
admin.site.register(AudioMessages)
admin.site.register(Letter)
admin.site.register(Poems)

