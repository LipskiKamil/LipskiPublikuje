from django.contrib import admin
from .models import Articles
from .models import Comments
from .models import AboutMe
# Register your models here.

admin.site.register(Articles)
admin.site.register(Comments)
admin.site.register(AboutMe)