import datetime
from user.models import Student, Mentor, Language, Course

python = Language.objects.create(name = 'Python', month_to_learn = 6)
javascript = Language.objects.create(name = 'Java Script', month_to_learn = 6)
uxui = Language.objects.create(name = 'UX-UI', month_to_learn = 2)

st1 = Student.objects.create(name = 'Amanov Aman', email = 'aman@mail.ru',
                             phone_number = '+996700989898',
                             work_study_place = 'School №13',
                             has_own_notebook = True,
                             preferred_os = 'windows')

st2 = Student.objects.create(name = 'Apina Alena', email = 'aapina@bk.ru',
                             phone_number = '0550888888',
                             work_study_place = 'TV', has_own_notebook = True,
                             preferred_os = 'mac')

st3 = Student.objects.create(name = 'Phil Spencer', email = 'spencer@microsoft.com',
                             phone_number = '0508312312',
                             work_study_place = 'Microsoft Gaming', has_own_notebook = False,
                             preferred_os = 'linux')

mentor1 = Mentor.objects.create(name = 'Ilona Maskova', email = 'imask@gmail.com',
                             phone_number = '0500545454',
                             experience = '2021-10-23')

mentor2 = Mentor.objects.create(name = 'Halil Nurmuhametov', email = 'halil@gmail.com',
                             phone_number = '0709989876',
                             main_work = 'University of Fort Collins',
                             experience = '2010-9-18')

course1 = Course.objects.create(name = 'Python – 21', mentor = mentor2,
                                student = [st1, st2], date_started = '2022-8-1',
                                language = python)

course2 = Course.objects.create(name = 'UXUI design – 43', mentor = mentor1,
                                student = st3, date_started = '2022-8-22',
                                language = uxui)

