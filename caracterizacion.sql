create database caracterizacion;
show databases;
use caracterizacion;
create table personas(
Num_Doc int not null primary key,
Tipo_Doc varchar (20) not null,
Vigencia_doc varchar (20) not null,
Nombres varchar(60) not null,
Apellidos varchar (60) not null, 
Fecha_Nacimiento date not null, 
Sexo varchar (12)  null, 
Edad int not null, 
Pasaporte varchar (4)  null,
Vigencia_pas varchar (60)  null,
Num_pas int not null,
Seg_Doc varchar(60)  null,
Num_seg_doc int null,
Ter_Doc varchar(60)  null,
Num_ter_doc int  null
);

select * from personas;
SET FOREIGN_KEY_CHECKS = 0;
SET FOREIGN_KEY_CHECKS = 1;
drop table personas;

use caracterizacion;
create table informacion_personal(
Direccion_Residencia varchar (20) not null,
Barrio varchar(60) not null,
Localidad varchar (20) not null,
Trabajo varchar (20) not null,
Correo varchar(20) not null,
Telefono_1 int not null,
Telefono_2 int not null,
Cuar_Doc varchar (20) not null,
Num_cuar_doc  int not null primary key,
Grado_Instruccion varchar (60) not null,
Area_instruccion varchar(60) not null,
Situacion_Migratoria varchar (60) not null,
Cant_cargafam int not null,
FOREIGN KEY(Num_cuar_doc )  REFERENCES personas (Num_doc)
);



drop table informacion_personal;

use caracterizacion;
create table informacion_medica(
Num_Doc int not null primary key,
Discapacidad varchar(60) not null, 
Desc_Discapacidad varchar (200)  not null,
Cond_Medica varchar (60) not null,
Desc_Medica varchar (200) not null,
FOREIGN KEY(Num_doc)  REFERENCES personas (Num_doc)
);



use caracterizacion;
create table familiares(
Num_doc_ref int  primary  key not null,
Tipo_doc varchar(20) not null,
Vig_doc varchar(20) not null, 
Nom_ref varchar (60)  not null,
Ape_ref varchar (60) not null,
Fecha_Nacimiento date not null, 
Edad int not null,
Sexo varchar (12) not null, 
Telef_1_ref int not null,
Telef_2_ref int not null,
Parentesco varchar (200) not null,
Ocupacion varchar (60) not null,
Seg_doc_ref varchar (60) not null,
Num_segdoc_ref int not null,
Terc_doc_ref varchar (60) not null,
Num_terdoc_ref int not null,
Observacion varchar (300) not null,
FOREIGN KEY(Num_doc_ref)  REFERENCES personas (Num_doc)
);

drop table familiares;

select * from familiares;
select * from personas;
describe personas;
describe familiares;
describe informacion_personal;
describe informacion_medica;
show tables;


create database usuario;
show databases;
use usuarios;
create table usuarios(

Num_Doc int primary  key not null,
Tipo_Doc varchar (20) not null,
Nombres varchar(45) not null,
Apellidos varchar (45) not null, 
Cargo varchar (45) not null,  
Direccion varchar (45) not null,
Telefono_prin int not null,
Telefono_sec int not null,
Usuario varchar(60) not null,
Contraseña int not null,
);


drop table usuarios;
