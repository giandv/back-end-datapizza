psql -U postgres

create database $POSTGRES_USER
create user $POSTGRES_USER with encrypted password '$POSTGRES_PASSWORD'
grant all privileges on database $POSTGRES_DATABASE to $POSTGRES_USER

CREATE TABLE IF NOT EXISTS job ( id SERIAL PRIMARY KEY, name character varying(100), schedule character varying(100));
CREATE TABLE IF NOT EXISTS company ( id SERIAL PRIMARY KEY, logo character varying(255), name character varying(100), UNIQUE(name), job_id integer not null references job(id));
CREATE TABLE IF NOT EXISTS technology ( id SERIAL PRIMARY KEY, skillname character varying(100), job_id integer not null references job(id));
CREATE TABLE IF NOT EXISTS info ( id SERIAL PRIMARY KEY, infoname character varying(100), job_id integer not null references job(id));

INSERT INTO job(name, schedule) VALUES('Data Engineer','full_time');

INSERT INTO technology(skillname, job_id) VALUES('Python', 1);
INSERT INTO technology(skillname, job_id) VALUES('AWS', 1);
INSERT INTO technology(skillname, job_id) VALUES('SQL', 1);
INSERT INTO technology(skillname, job_id) VALUES('Terraform', 1);

INSERT INTO info(infoname, job_id) VALUES('👨🏽‍💻 3-5 Years Experience', 1);
INSERT INTO info(infoname, job_id) VALUES('💸 RAL: 40k-50k', 1);
INSERT INTO info(infoname, job_id) VALUES('📍 Milano Citylife Tretorri', 1);
INSERT INTO info(infoname, job_id) VALUES('💻 3 giorni a settimana in smart', 1);

INSERT INTO company(logo, name, job_id) VALUES('https://api.datapizza.tech/media/companies/4a454315-de4e-4d73-8a96-a7b96c863bfd/generali_real_estate_logo.jpeg','Generali Real Estate', 1);
