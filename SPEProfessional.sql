

CREATE TABLE unitCoordinators (
  uc_id INTEGER NOT NULL PRIMARY KEY,
  firstname TEXT NOT NULL,
  lastname TEXT NOT NULL,
  title TEXT NOT NULL,
  email NOT NULL);

CREATE TABLE surveys (
  survey_id INTEGER PRIMARY KEY NOT NULL,
  survey_name TEXT NOT NULL,
  recipients TEXT NOT NULL,
  intro TEXT NOT NULL);

CREATE TABLE teams (
  team_id INTEGER PRIMARY KEY NOT NULL,
  team_name TEXT NOT NULL,
  unit_id INTEGER,
  uc_id INTEGER,
  FOREIGN KEY(unit_id) REFERENCES units(unit_id),
  FOREIGN KEY(uc_id) REFERENCES unitCoordinators(uc_id));

CREATE TABLE admins (
  admin_id INTEGER PRIMARY KEY NOT NULL,
  firstname TEXT NOT NULL,
  lastname TEXT NOT NULL,
  title TEXT NOT NULL,
  email NOT NULL);

CREATE TABLE complaints (
  issue_id TEXT NOT NULL PRIMARY KEY,  
  FOREIGN KEY (student_id) REFERENCES students(student_id), 
  issue_subject TEXT NOT NULL);

CREATE TABLE questions (
  question_id TEXT NOT NULL PRIMARY KEY, 
  question TEXT NOT NULL);

CREATE TABLE students (
  student_id TEXT NOT NULL PRIMARY KEY, 
  firstname TEXT NOT NULL, 
  lastname TEXT NOT NULL, 
  title TEXT NOT NULL, 
  email TEXT NOT NULL);

INSERT INTO student (student_id, firstname, lastname, title, email)
  VALUES('330001', 'Anjara', 'Tiana', 'Miss', 'anjarra.tia@gmail.com');
  VALUES('330002', 'Fatima', 'Shaikh', 'Miss', 'fatimashaikkh3@gmail.com');
  VALUES('330003', 'Ahmed', 'Emadaldin', 'Mr', 'ahmedewais2002@gmail.com');
  VALUES('330004', 'Sanhita', 'Srinivas', 'Miss', 'sanhitak@gmail.com');
  VALUES('330005', 'Owaish', 'Mustafa', 'Miss', 'jilaniowaish@gmail.com');
  VALUES('330006', 'Jane', 'Doe', 'Mrs', 'janedoe@gmail.com');
  VALUES('330007', 'John', 'Doe', 'Mr', 'johndoe@gmail.com');
  VALUES('330008', 'Peter', 'Pan', 'Mr', 'peterpan@gmail.com');
  VALUES('330009', 'Steve', 'Jobs', 'Mr', 'stevejobs@gmail.com');
  VALUES('330010', 'Serena', 'Williams', 'Mrs', 'serenawilliam@gmail.com');
  VALUES('330011', 'Will', 'Gregory', 'Mr', 'willgreg@gmail.com');
  VALUES('330012', 'Noah', 'Cyrus', 'Miss', 'noahc@gmail.com');
  VALUES('330013', 'Andy', 'Murray', 'Mr', 'amurray@gmail.com');
  VALUES('330014', 'Stefan', 'King', 'Mr', 'stefk@gmail.com');
  VALUES('330015', 'Noor', 'Patterson', 'Mrs', 'noorpatty@gmail.com');

CREATE TABLE units (
  unit_id TEXT NOT NULL PRIMARY KEY, 
  unit_name TEXT NOT NULL, 
  teaching_period TEXT NOT NULL, 
  FOREIGN KEY (uc_id) REFERENCES unitCoordinators(uc_id));

INSERT INTO units (unit_id, unit_name, teaching_period, uc_id)
  VALUES('ICT302', 'IT Professional Practic Project', 'TJD23', '220001');
  VALUES('BSC302', 'Advanced Quantitative Research Methods', '220001');
  VALUES('ICT201', 'Information Technology Project Management', '220002');