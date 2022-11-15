DROP database if EXISTS mysql;
CREATE DATABASE mysql;
use mysql;

DROP TABLE IF EXISTS RandomNames;
Create table RandomNames
(id int,
 name varchar(100),
 gender char(1)
);

insert into RandomNames
(id, name,gender)
select 1,'Bill','M'
union
select 2,'John','M'
union
select 3,'Steve','M'
union
select 4,'Mike','M'
union
select 5,'Phil','M'
union
select 6,'Sarah','F'
union
select 7,'Ann','F'
union
select 8,'Marie','F'
union
select 9,'Liz','F'
union
select 10,'Stephanie','F'