from django.contrib import admin
from .models import CustomUser, TAG, Todo

# Register your models here.

#admin.site.register(TAG)

@admin.register(CustomUser)
class myapp(admin.ModelAdmin):
    list_display = ['id','profil_pic', 'name', 'email', 'password',  ]


@admin.register(Todo)
class myapp(admin.ModelAdmin):
    list_display = ['id', 'Title', 'Description', 'Due_date', 'status', 'Created_Date', 'Updated_Date', ]



@admin.register(TAG)
class myapp(admin.ModelAdmin):
    list_display = ['id', 'tags' ]




