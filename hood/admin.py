from django.contrib import admin
from .models import Profile,neighbourhood,BlogPost,Business,Health,healthservices,notifications

# Register your models here.
admin.site.register(Profile)
admin.site.register(neighbourhood)
admin.site.register(BlogPost)
admin.site.register(Business)
admin.site.register(Health)
admin.site.register(healthservices)
admin.site.register(notifications)