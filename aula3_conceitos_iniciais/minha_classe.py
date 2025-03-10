class MinhaClasse:
    def __init__(self, info, elem):     #método construtor é o primeiro método que é chamado quando instanciamos um objeto
        self.atributo_1 = 'Atributo 1'
        self.atributo_2 = [1, 2, "a"]
        self.atributo_3 = elem 
        self.new_atribute = info
        print(self.new_atribute)



    def metodo_1(self):
        print('Minha ação 1')
        print('Minha ação 2')
        print(self.atributo_2)
        print(self.atributo_3)
        return "Olá, mundo!"
    
    def metodo_2(self, numero):
        self.metodo_1()
        print(self.atributo_2[1] + numero)

#objeto         #classe ->instanciar um objeto
minha_classe = MinhaClasse("info aqui no construtor", 213)

# response = minha_classe.metodo_1()
# print(response)
minha_classe.metodo_2(3)