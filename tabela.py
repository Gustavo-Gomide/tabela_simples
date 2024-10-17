class Concecionaria:
    def __init__(self, nome="concessionaria"):
        self._nome = nome
        self._veiculos = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def veiculos(self):
        return self._veiculos

    @veiculos.setter
    def veiculos(self, veiculos):
        self._veiculos = veiculos

    def adiciona_veiculo(self, veiculo):
        self.veiculos.append(veiculo.__dict__)

    def listar_veiculos(self, tam=15):
        qtd = len(self.veiculos[0])  # quantidade de colunas
        tam *= qtd  # tamanho total
        print(f"\033[4;30;44m{self.nome:^{tam}}\033[m")
        for pos, veiculo in enumerate(self.veiculos):
            if pos % 2 == 0:
                cor1 = '\033[4;30;42m'
            else:
                cor1 = '\033[4;30;43m'
            for n, chave in enumerate(veiculo.keys()):
                if pos != 0:
                    break
                print(f"\033[4;30;45m{chave.replace("_", ""):^{int(tam / qtd)}}\033[m", end='')
                if n == len(veiculo.items()) - 1:  # ultima coluna
                    print()
            for chave, valor in veiculo.items():
                if chave == '_preco':
                    valor = f"R${valor:.2f}".replace('.', ',')
                    print(f"{cor1}{valor:^{int(tam / qtd)}}\033[m", end='')
                else:
                    print(f"{cor1}{valor:^{int(tam / qtd)}}\033[m", end='')
            print()


class Veiculo:
    def __init__(self, cor="preto", preco: float = 54_659.89):
        self._cor = cor
        self._preco = preco

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, cor):
        self._cor = cor

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        self._preco = preco


class Carro(Veiculo):
    def __init__(self, nome, porta=4, potencia=200, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._nome = nome
        self._porta = porta
        self._potencia = potencia

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome


if __name__ == '__main__':
    c1 = Concecionaria()
    car1 = Carro("hb20")
    car2 = Carro("onix")
    c1.adiciona_veiculo(car1)
    c1.adiciona_veiculo(car2)
    c1.listar_veiculos()
    car3 = Carro('creta')
    car4 = Carro('hb20', cor='vermelho')
    car5 = Carro('celta', cor='vermelho', preco=28_000)
    c2 = Concecionaria("Hyundai")
    c2.adiciona_veiculo(car3)
    c2.adiciona_veiculo(car4)
    c2.adiciona_veiculo(car5)
    print('-' * 100)
    c2.listar_veiculos(20)
