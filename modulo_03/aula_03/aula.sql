CREATE Table professores(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE TABLE alunos(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    id_professor INTEGER NOT NULL,
    FOREIGN KEY (id_professor) REFERENCES professores(id)
    ON DELETE CASCADE
);
DROP TABLE alunos; -- apaga a tabela e tudo dentro
INSERT INTO professores(nome) VALUES('Anderson');
INSERT INTO professores(nome) VALUES('Fabricio');
SELECT * FROM professores;

INSERT INTO alunos(nome, id_professor) VALUES ('João', 1);
INSERT INTO alunos(nome, id_professor) VALUES ('Mara', 1);
INSERT INTO alunos(nome, id_professor) VALUES ('Pedro', 2);
DELETE FROM alunos WHERE nome = 'Pedro';
SELECT * FROM alunos;
SELECT id AS Identificador, nome AS Priemeiro_Nome FROM alunos;

SELECT alunos.nome AS nome_aluno, professores.nome AS nome_professor
FROM alunos
INNER JOIN professores ON alunos.id_professor = professores.id;
DELETE FROM professores WHERE id = 2;