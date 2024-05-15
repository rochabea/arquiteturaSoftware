class View:
    @staticmethod
    def display_menu():
        print("\nBiblioteca - Menu")
        print("1. Adicionar livro")
        print("2. Buscar livro por título")
        print("3. Buscar livro por autor")
        print("4. Emprestar livro")
        print("5. Devolver livro")
        print("6. Sair")

    @staticmethod
    def get_input(prompt):
        return input(prompt)

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def display_books(books):
        if not books:
            print("Nenhum livro encontrado.")
        else:
            for book in books:
                status = "Disponível" if not book.is_borrowed else "Emprestado"
                print(f"Registro: {book.reg_number}, Título: {book.title}, Autor: {book.author}, Status: {status}")
