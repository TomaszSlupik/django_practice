from django.contrib import admin
from lesson.models import Car, Driver, Student, School, Author, Book


# Register your models here.
class CarAdmin(admin.ModelAdmin):
    fields = ["producer", "model", "seats", "driver"]
    list_display = ["id", "producer", "model", "seats", "driver"]


class StudentAdmin(admin.ModelAdmin):
    fields = ["first_name", "last_name", "birth_day", "my_school"]
    list_display = ["id", "first_name", "last_name", "birth_day", "my_school"]


class SchoolAdmin(admin.ModelAdmin):
    fields = ["name_school"]
    list_display = ["name_school"]


class AuthorAdmin(admin.ModelAdmin):
    fields = ["name"]
    list_display = ["name"]

class BookAdmin(admin.ModelAdmin):
    fields = ["title", "authors"]
    # list_display = ["title", "authors"]

admin.site.register(Car, CarAdmin)
admin.site.register(Driver)
admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)