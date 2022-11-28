create or replace function get_course_id_by_email(email varchar(254))  
returns table (id bigint) as'
select student_id from user_course
where student_id in (select id from user_student where email like email);
' language sql;

select * from get_course_id_by_email('spencer@microsoft.com')

-- select * from user_course
select * from user_student


