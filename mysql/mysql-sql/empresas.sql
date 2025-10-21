-- CREAR BASE DE DATOS
CREATE DATABASE db_g5
    DEFAULT CHARACTER SET = 'utf8mb4';
-- ENTRAR A LA BASE DE DATOS
use db_g5;

CREATE TABLE empresa(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary Key',
    ruc VARCHAR(20) NOT NULL,
    razon_social VARCHAR(255) NOT NULL,
    nombre_comercial VARCHAR(255),
    direccion VARCHAR(255)
);

# Le pedi a la IA q me llene los datos del insert
INSERT INTO empresa (ruc, razon_social, nombre_comercial, direccion)
VALUES
('20111111111', 'Soluciones Integrales S.A.C.', 'SolIntegra', 'Av. Primavera 123'),
('20222222222', 'Comercial Andina S.R.L.', 'ComAndina', 'Calle Los Pinos 456'),
('20333333333', 'Importadora del Pacífico E.I.R.L.', 'Impacif', 'Jr. Amazonas 789'),
('20444444444', 'Distribuidora Central S.A.', 'DisCen', 'Av. Central 101'),
('20555555555', 'Servicios Logísticos del Sur S.A.C.', 'LogiSur', 'Calle Los Olivos 202'),
('20666666666', 'Tecnologías del Norte S.R.L.', 'TecNor', 'Av. Libertad 303'),
('20777777777', 'Industrias Rivera S.A.C.', 'InduRiv', 'Jr. Industria 404'),
('20888888888', 'Consultores Globales S.A.', 'ConGlobal', 'Av. Los Proceres 505'),
('20999999999', 'Grupo Empresarial Luna S.R.L.', 'LunaCorp', 'Calle Estrella 606'),
('21000000000', 'Inversiones del Valle S.A.C.', 'InverValle', 'Av. Los Laureles 707');