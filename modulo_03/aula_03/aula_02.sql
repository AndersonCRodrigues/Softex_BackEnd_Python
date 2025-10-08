CREATE TABLE usuarios(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE TABLE cursos(
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL
);

CREATE TABLE usuarios_cursos(
    id_usuario INTEGER NOT NULL,
    id_curso INTEGER NOT NULL,
    Foreign Key (id_usuario) REFERENCES usuarios(id),
    Foreign Key (id_curso) REFERENCES cursos(id)
);

INSERT INTO usuarios(nome) VALUES ('Pedro'), ('Michele'), ('Rafael'), ('Carol');
INSERT INTO cursos(titulo) VALUES ('backend'),('frontend');
INSERT INTO usuarios_cursos(id_usuario, id_curso) VALUES (1,1), (1,2), (2,1), (3,2);
INSERT INTO usuarios_cursos(id_usuario, id_curso) VALUES (4,1);

SELECT * FROM usuarios;
SELECT * FROM cursos;
SELECT * FROM usuarios_cursos; 

SELECT usuarios.nome, cursos.titulo FROM usuarios_cursos
INNER JOIN usuarios ON usuarios_cursos.id_usuario = usuarios.id
INNER JOIN cursos ON usuarios_cursos.id_curso = cursos.id;

SELECT count(nome) from usuarios WHERE nome = 'Carol';

SELECT COUNT(usuarios.nome) AS QTD_Alunos, cursos.titulo FROM usuarios_cursos
INNER JOIN usuarios ON usuarios_cursos.id_usuario = usuarios.id
INNER JOIN cursos ON usuarios_cursos.id_curso = cursos.id
GROUP BY cursos.titulo;

SELECT COUNT(usuarios.nome) AS QTD_Alunos, cursos.titulo FROM usuarios_cursos
INNER JOIN usuarios ON usuarios_cursos.id_usuario = usuarios.id
INNER JOIN cursos ON usuarios_cursos.id_curso = cursos.id
GROUP BY cursos.titulo
HAVING COUNT(usuarios.nome) > 2;