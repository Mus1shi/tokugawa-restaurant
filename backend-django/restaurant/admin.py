from django.contrib import admin
from restaurant.models import Menu, Category, Chef, Comment, Reservation

admin.site.register(Menu)
admin.site.register(Category)
admin.site.register(Chef)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'created_at', 'likes', 'dislikes')
    list_filter = ('created_at',)
    search_fields = ('name', 'content')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'date', 'time', 'people', 'content')
    list_filter = ('date','time')
    search_fields = ('name', 'content','date','time')
