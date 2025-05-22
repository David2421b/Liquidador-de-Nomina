create table if not exists datos_obtenidos(
  cedula varchar(11) not null,
  salario_neto varchar(15) not null,
  bonificacion varchar(15) not null,
  valor_hora_extra varchar(15) not null,
  foreign key (cedula) references empleados(cedula)
);