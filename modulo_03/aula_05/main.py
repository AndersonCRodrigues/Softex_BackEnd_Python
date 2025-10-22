from modulo_03.aula_06.database import DatabaseConnection
from student_model import StudentModel
from course_model import CourseModel
from enrollment_model import EnrollmentModel

# Inicializa as conexões e modelos globalmente
db_conn = DatabaseConnection("escola.db")
student_model = StudentModel(db_conn)
course_model = CourseModel(db_conn)
enrollment_model = EnrollmentModel(db_conn)


def display_menu():
    """Exibe o menu principal de opções do sistema escolar."""
    print("\n==================================")
    print("      SISTEMA DE GESTÃO ESCOLAR     ")
    print("==================================")
    print("1. Gerenciar Alunos (CRUD)")
    print("2. Gerenciar Cursos (CRUD)")
    print("3. Gerenciar Matrículas (N:N)")
    print("4. Sair")
    print("----------------------------------")


def display_submenu(title, options):
    """Exibe submenus genéricos."""
    print(f"\n--- {title} ---")
    for key, value in options.items():
        print(f"{key}. {value}")
    print("V. Voltar ao menu principal")
    print("-------------------------")


def handle_student_management():
    """Lida com as operações CRUD de Alunos."""
    options = {
        "1": "Cadastrar novo aluno",
        "2": "Buscar aluno por ID",
        "3": "Listar todos os alunos",
    }
    while True:
        display_submenu("Gerenciar Alunos", options)
        choice = input("Escolha uma opção: ").upper()

        if choice == "1":
            print("\n--- Cadastro de Aluno ---")
            nome = input("Nome: ")
            email = input("E-mail: ")
            student_model.create_student(nome, email)

        elif choice == "2":
            print("\n--- Buscar Aluno ---")
            try:
                student_id = int(input("Digite o ID do aluno: "))
                student = student_model.find_student_by_id(student_id)
                if student:
                    print("\nAluno encontrado:")
                    print(
                        f"ID: {student['id']} | Nome: {student['nome']} | E-mail: {student['email']}"
                    )
                else:
                    print("Aluno não encontrado.")
            except ValueError:
                print("ID inválido. Por favor, digite um número.")

        elif choice == "3":
            print("\n--- Lista de Alunos ---")
            students = student_model.get_all_students()
            if students:
                for student in students:
                    print(
                        f"ID: {student['id']} | Nome: {student['nome']} | E-mail: {student['email']}"
                    )
            else:
                print("Nenhum aluno cadastrado.")

        elif choice == "V":
            break

        else:
            print("Opção inválida. Tente novamente.")


def handle_course_management():
    """Lida com as operações CRUD de Cursos."""
    options = {
        "1": "Cadastrar novo curso",
        "2": "Buscar curso por ID",
        "3": "Listar todos os cursos",
    }
    while True:
        display_submenu("Gerenciar Cursos", options)
        choice = input("Escolha uma opção: ").upper()

        if choice == "1":
            print("\n--- Cadastro de Curso ---")
            nome = input("Nome do curso: ")
            descricao = input("Descrição do curso: ")
            course_model.create_course(nome, descricao)

        elif choice == "2":
            print("\n--- Buscar Curso ---")
            try:
                course_id = int(input("Digite o ID do curso: "))
                course = course_model.find_course_by_id(course_id)
                if course:
                    print("\nCurso encontrado:")
                    print(
                        f"ID: {course['id']} | Nome: {course['nome']} | Descrição: {course['descricao']}"
                    )
                else:
                    print("Curso não encontrado.")
            except ValueError:
                print("ID inválido. Por favor, digite um número.")

        elif choice == "3":
            print("\n--- Lista de Cursos ---")
            courses = course_model.get_all_courses()
            if courses:
                for course in courses:
                    print(
                        f"ID: {course['id']} | Nome: {course['nome']} | Descrição: {course['descricao']}"
                    )
            else:
                print("Nenhum curso cadastrado.")

        elif choice == "V":
            break

        else:
            print("Opção inválida. Tente novamente.")


def handle_enrollment_management():
    """Lida com as operações N:N de Matrículas."""
    options = {
        "1": "Matricular aluno em curso",
        "2": "Ver cursos de um aluno (Aluno -> N Cursos)",
        "3": "Ver alunos de um curso (Curso -> N Alunos)",
    }
    while True:
        display_submenu("Gerenciar Matrículas (N:N)", options)
        choice = input("Escolha uma opção: ").upper()

        if choice == "1":
            print("\n--- Registrar Matrícula ---")
            try:
                id_aluno = int(input("ID do Aluno: "))
                id_curso = int(input("ID do Curso: "))
                enrollment_model.enroll_student(id_aluno, id_curso)
            except ValueError:
                print("IDs inválidos. Por favor, digite números.")

        elif choice == "2":
            print("\n--- Cursos por Aluno ---")
            try:
                id_aluno = int(input("Digite o ID do Aluno: "))
                courses = enrollment_model.get_courses_by_student(id_aluno)
                if courses:
                    print(f"\nCursos matriculados pelo Aluno ID {id_aluno}:")
                    for course in courses:
                        print(
                            f"ID: {course['id']} | Curso: {course['nome']} | Data: {course['data_matricula']}"
                        )
                else:
                    print(
                        f"O Aluno ID {id_aluno} não está matriculado em nenhum curso."
                    )
            except ValueError:
                print("ID inválido.")

        elif choice == "3":
            print("\n--- Alunos por Curso ---")
            try:
                id_curso = int(input("Digite o ID do Curso: "))
                students = enrollment_model.get_students_by_course(id_curso)
                if students:
                    print(f"\nAlunos matriculados no Curso ID {id_curso}:")
                    for student in students:
                        print(
                            f"ID: {student['id']} | Nome: {student['nome']} | E-mail: {student['email']}"
                        )
                else:
                    print(f"Nenhum aluno matriculado no Curso ID {id_curso}.")
            except ValueError:
                print("ID inválido.")

        elif choice == "V":
            break

        else:
            print("Opção inválida. Tente novamente.")


def main():
    """Função principal do programa, controlando o menu principal."""
    while True:
        display_menu()
        choice = input("Escolha uma opção: ")

        if choice == "1":
            handle_student_management()

        elif choice == "2":
            handle_course_management()

        elif choice == "3":
            handle_enrollment_management()

        elif choice == "4":
            print("Saindo do programa. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
