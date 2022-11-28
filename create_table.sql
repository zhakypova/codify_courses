create table payments
(
id serial primary key,
course_id integer References user_course(id) on delete cascade,
amount numeric,
pay_date date
);

insert into payments(course_id,amount, pay_date)
values(
(select id from get_course_id_by_email('aman@mail.ru')),
 15000, '2022-8-15');
 (
(select id from get_course_id_by_email('aapina@bk.ru')),
 55000, '2022-8-05');
 (
(select id from get_course_id_by_email('spencer@microsoft.com')),
 5000, '2022-8-25');

