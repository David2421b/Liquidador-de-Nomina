create table if not exists datos_obtenidos(
  cedula varchar(11) not null,
  salario_neto varchar(50) not null,
  bonificacion varchar(50) not null,
  valor_hora_extra varchar(50) not null,
  cuotas varchar(50) not null,
  foreign key (cedula) references empleados(cedula)
);