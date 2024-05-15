class View:
    @staticmethod
    def menu():
        print("\nBiblioteca - Menu")
        print("1. Adicionar livro")
        print("2. Buscar livro por título")
        print("3. Buscar livro por autor")
        print("4. Emprestar livro")
        print("5. Devolver livro")
        print("6. Sair")

    @staticmethod
    def insere(prompt):
        return input(prompt)
    
    @staticmethod
    def display_mensagem(mensagem):
        print(mensagem)

    @staticmethod
    def display_livros(_livro):
        if not _livro:
            print("Nenhum livro encontrado.")
        else:
            for livro in _livro:
                status = "Disponível" if not livro._emprestado else "Emprestado"
                print(f"Registro: {livro._rg_numero}, Título: {livro._titulo}, Autor: {livro._autor}, Status: {status}")