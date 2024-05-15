from model import Library
from model import Book
from controller import Controller
from view import View

def main():
    library = Library()
    view = View()
    controller = Controller(library, view)
    controller.run()

if __name__ == "__main__":
    main()
