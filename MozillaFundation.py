import sys 
sys.stdout.reconfigure(encoding='utf-8') # Essa importação foi para que o texto fique no padrão utf-8 e reconheça a acentuação quando for impresso no terminal
class Navigator:
    def __init__(self):
        self.previousStack = [] # Pilha para armazenar os endereços visitados
        self.advancedStack = [] # Pilha para armazenar os enderecos voltados
        self.atualPage = None # Nenhuma página carregada inicialmente
    
    def accessingPage(self, url): # Acessa uma nova pagina e atualiza as pilhas
        if self.atualPage:
            self.previousStack.append(self.atualPage)  # Adiciona a página atual a pilha de voltar
        self.atualPage = url # Define a nova página como atual
        self.advancedStack.clear() # Ao acessar uma nova página, a pilha de avançar é esvaziada
        
        print("Acessando a pagina", url)
        self.showStatus()
    
    def toGoBack(self): # Volta para a página anterior, se possível
        if self.previousStack:
            self.advancedStack.append(self.atualPage) # Move a página atual para a pilha de avançar
            self.atualPage = self.previousStack.pop()  # Define a última página visitada como atual
            print("Voltando para", self.atualPage)
        else:
            print("Nao ha paginas para voltar")
        self.showStatus()
    def moveForward(self): #Se possivel, ira avancar para a proxima pagina
        if self.advancedStack:
            self.previousStack.append(self.atualPage)  # Move a página atual para a pilha de voltar
            self.atualPage = self.advancedStack.pop()  # Define a próxima página como atual
            print("Avançando para:", self.atualPage)
        else:
            print("Não há páginas para avançar")
        
        self.showStatus()
    
    def showStatus(self): # Exibe o estado atual do navegador
        print("\nEstado atual do navegador: \n")
        print("Página Atual:", self.atualPage)
        print("Pilha Voltar:", self.previousStack)
        print("Pilha Avançar:", self.advancedStack)
        print(40*"-")
    def execute(self): # Inicializando todas as funções da classe
        navegador = Navigator()
        print("Bem vindo ao navegador!\nVamos começar a navegar!!!!!\n")
        navegador.toGoBack()
        navegador.accessingPage("www.google.com")
        navegador.accessingPage("www.github.com")
        navegador.accessingPage("www.mozilla.org")
        navegador.toGoBack()
        navegador.toGoBack()
        navegador.moveForward()
        navegador.accessingPage("www.python.org")
        
if __name__ == '__main__':
    start = Navigator()
    start.execute()

# Foi o melhor que pude fazer no momento. Obs.: código comentado demais e beeeeem feio rsrsrs
