class Book:
    def __init__(self, titulo, autor, rg_numero):
        self._titulo = titulo
        self._autor = autor
        self._rg_numero = rg_numero
        self._emprestado = False

class Biblioteca:
    def __init__(self):
        self._livro = []

    def adicionar_livro(self, _livro):
        self._livro.append(_livro)

    def procura_titulo(self, _titulo):
        return [livro for livro in self._livro if _titulo.lower() in livro._titulo.lower()]
    
    def procura_autor(self, _autor):
        return [livro for livro in self._livro if _autor.lower() in livro._autor.lower()]
    
    def empresta_livro(self, _rg_numero):
        for livro in self._livro:
            if livro._rg_numero == _rg_numero and not livro._emprestado:
                livro._emprestado = True
                return livro
        return None
    
    def devolve_livro(self, _rg_numero):
        for livro in self._livro:
            if livro._rg_numero == _rg_numero and livro._emprestado:
                livro._esprestado = False
                return livro
        return None