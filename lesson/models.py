from django.db import models

# Create your models here.
# Tworzenie struktury bazy danych:
# Model Driver 
class Driver (models.Model):
    name_driver = models.CharField(max_length=32)
    surname_driver = models.CharField(max_length=32)

    def __str__(self) -> str:
        return f"Driver: {self.name_driver} {self.surname_driver}"


# Samochód może mieć jednego kierowcę, a kierowca może mieć wielu samochodów 

class Car (models.Model):
    producer = models.CharField(max_length= 32)
    model = models.CharField(max_length=32)
    seats = models.PositiveIntegerField()
    # Samochód 1 kierowca
    # Co sie stanie jak kierowca zostanie usunięty
    # models.CASCADE - usuwaj kaskadowo
    # models.PROTECT 
    # models.SET_NULL - puste
    # models.DO_NOTHING - nic nie rób
    # models.SET_DEFAULT - wrzuc o numerze 1
    driver = models.ForeignKey(Driver, on_delete=models.SET_DEFAULT, default=2)


# Student ma 1 szkołę, ale szkoła ma wielu uczniów 
class School(models.Model):
    name_school = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name_school

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_day = models.DateField()
    my_school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        school = self.my_school if self.my_school is not None else "None"
        return f"{self.first_name} {self.last_name} school: {self.my_school}"


# Autor ma wiele książek i książka może mieć wielu autorów
class Author (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"
    

class Book(models.Model):
    title = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author)

    def __str__(self) -> str:
        author_names = [author.name for author in self.authors.all()]
        names_str = ", ".join(author_names)
        return f"Tytuł: {self.title}, Autor: {names_str}"


