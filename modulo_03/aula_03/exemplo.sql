CREATE TABLE professores(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE TABLE alunos(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    id_professor INTEGER NOT NULL,
    FOREIGN KEY (id_professor) REFERENCES professores(id)
);
DROP TABLE alunos; -- apaga a tabela e todo seu conteudo

INSERT INTO professores(nome) VALUES ('Anderson'), ('Paulo');
SELECT * FROM professores;
INSERT INTO alunos(nome, id_professor) VALUES ('Pedro', 1), ('Maria', 2), ('José', 1);
SELECT * FROM alunos;
SELECT id AS Identificador, nome, id_professor AS 'Registro Professor' FROM alunos;

SELECT alunos.nome AS Nome_aluno, professores.nome AS Nome_Professor FROM alunos
INNER JOIN professores ON alunos.id_professor = professores.id;