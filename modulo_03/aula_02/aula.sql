-- Active: 1759768637734@@127.0.0.1@3306
CREATE TABLE alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER
);

INSERT INTO alunos (nome, idade) VALUES ('João', 20);
INSERT INTO alunos (nome, idade) VALUES ('Maria', 22);

SELECT * FROM alunos;

-- Comentario

/*
bloco de comentario
pulei uma linha e continua sendo comentario
*/
SELECT nome, idade FROM alunos;

DELETE FROM alunos WHERE id = 3;

INSERT INTO 
    alunos(nome, idade) 
VALUES
    ('Carlos', 18),
    ('José', 32),
    ('Ana',25);