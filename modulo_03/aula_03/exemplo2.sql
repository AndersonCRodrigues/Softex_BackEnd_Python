CREATE TABLE alunos(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE TABLE cursos(
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL
);

CREATE TABLE alunos_cursos(
    id_aluno INTEGER,
    id_curso INTEGER,
    FOREIGN KEY (id_aluno) REFERENCES alunos(id),
    FOREIGN KEY (id_curso) REFERENCES cursos(id)
);

INSERT INTO alunos(nome) VALUES ('Paulo'), ('Mara'), ('Andre'), ('Carla');
SELECT * FROM alunos;
INSERT INTO cursos(titulo) VALUES ('backend'), ('frontend');
SELECT * FROM cursos;
INSERT INTO alunos_cursos(id_aluno, id_curso) VALUES (1,1), (1,2), (2,1), (3,1), (4,1), (4,2);
SELECT * FROM alunos_cursos;

SELECT alunos.nome, cursos.titulo FROM alunos
INNER JOIN alunos_cursos ON alunos_cursos.id_aluno = alunos.id
INNER JOIN cursos ON alunos_cursos.id_curso = cursos.id;

SELECT COUNT(*) FROM alunos;
SELECT count(*) FROM alunos_cursos where id_curso = 1;

SELECT COUNT(alunos.nome), cursos.titulo FROM alunos
INNER JOIN alunos_cursos ON alunos_cursos.id_aluno = alunos.id
INNER JOIN cursos ON alunos_cursos.id_curso = cursos.id
GROUP BY cursos.titulo;

SELECT COUNT(alunos.nome), cursos.titulo FROM alunos
INNER JOIN alunos_cursos ON alunos_cursos.id_aluno = alunos.id
INNER JOIN cursos ON alunos_cursos.id_curso = cursos.id
GROUP BY cursos.titulo
HAVING Count(alunos.nome) > 3;