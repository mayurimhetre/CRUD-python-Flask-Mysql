show databases;
create database test;
use test;
create table test.student ( roll_no int , name varchar(20), emailid varchar(50), mobile varchar(10));
select * from student;
insert into student values ('1','mayuri mhetre','mm@gmail.com','1234567891');
SET SQL_SAFE_UPDATES=0;
update student set name = 'xyx dfg' , emailid = 'xyz@gmail.com'  , mobile = '1234567891' where roll_no = 1;

