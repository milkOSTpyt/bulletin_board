from django.contrib import admin

from bulletin_board_app.models import Category, City, Advert


@admin.register(Category)
class BookAdmin(admin.ModelAdmin):
    ...


@admin.register(City)
class BookAdmin(admin.ModelAdmin):
    ...


@admin.register(Advert)
class BookAdmin(admin.ModelAdmin):
    ...
