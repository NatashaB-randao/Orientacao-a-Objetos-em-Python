class MinhaClasse:
    def __init__(self):     #método construtor
        pass 



    def metodo_1(self):
        print('Minha ação 1')
        print('Minha ação 2')
        return "Olá, mundo!"

#objeto         #classe ->instanciar um objeto
minha_classe = MinhaClasse()

response = minha_classe.metodo_1()
print(response)