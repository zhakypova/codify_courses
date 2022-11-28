from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=20)
    month_to_learn = models.IntegerField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.name.islower():
            return self.name.title()

class AbstractPerson(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return f'{self.name} - {self.email} - {self.phone_number}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.phone_number.startswith('0'):
            return self.phone_number.replace('0', '+996')
        else:
            return self.phone_number

class Student(AbstractPerson):
    work_study_place = models.CharField(max_length=30, null=True)
    has_own_notebook = models.BooleanField()
    os_choices = [('windows', 'win'), ('macOS', 'mac'), ('linux', 'lin')]
    preferred_os = models.CharField(max_length=20, choices=os_choices)

    def __str__(self):
        return self.name

class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=30, null=True)
    experience = models.DateField()


class Course(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    date_started = models.DateField()

    def __str__(self):
        return f'{self.student.name} - {self.mentor.name} - {self.name}'

    def get_end_date(self):
        lasting = Language.month_to_learn * 30
        date_end = lasting + self.date_started
        return date_end


