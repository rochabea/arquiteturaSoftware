from model import Book

class Controller:
    def __init__(self, library, view):
        self.library = library
        self.view = view

    def run(self):
        while True:
            self.view.display_menu()
            choice = self.view.get_input("Escolha uma opção: ")

            if choice == '1':
                title = self.view.get_input("Título do livro: ")
                author = self.view.get_input("Autor do livro: ")
                reg_number = self.view.get_input("Número de registro do livro: ")
                book = Book(title, author, reg_number)
                self.library.add_book(book)
                self.view.display_message("Livro adicionado com sucesso!")

            elif choice == '2':
                title = self.view.get_input("Digite o título para buscar: ")
                books = self.library.search_by_title(title)
                self.view.display_books(books)

            elif choice == '3':
                author = self.view.get_input("Digite o autor para buscar: ")
                books = self.library.search_by_author(author)
                self.view.display_books(books)

            elif choice == '4':
                reg_number = self.view.get_input("Digite o número de registro do livro para emprestar: ")
                book = self.library.borrow_book(reg_number)
                if book:
                    self.view.display_message(f"Livro '{book.title}' emprestado com sucesso!")
                else:
                    self.view.display_message("Livro não encontrado ou já emprestado.")

            elif choice == '5':
                reg_number = self.view.get_input("Digite o número de registro do livro para devolver: ")
                book = self.library.return_book(reg_number)
                if book:
                    self.view.display_message(f"Livro '{book.title}' devolvido com sucesso!")
                else:
                    self.view.display_message("Livro não encontrado ou já devolvido.")

            elif choice == '6':
                self.view.display_message("Saindo do sistema...")
                break

            else:
                self.view.display_message("Opção inválida. Tente novamente.")
