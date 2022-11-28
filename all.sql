select
usc.name,
usc.date_started,
uss.name,
usm.name,
usc.language
from user_course as usc
inner join user_student as uss
on uss.id = usc.student_id
inner join user_mentor as usm
on usm.id = usc.mentor_id;




























