class knn():
    """ Classe para calcula distância entre a referencia e os dados modelo \n """

    def __init__(self, dados):
        """ Metódo construtor da classe knn \n
        Args:
            dados: Dados modelos para buscar referência\n
        Returns: \n
        """
        self.dados = dados
        return

    def calcula_distancia(self, busca):
        """ Calcula distância entre referência e os dados modelo \n
        Args: \n
            busca: Referência para buscar no dados modelos \n
        Returns: \n
            Retorna a distancia da referencia para os dados modelos \n
        """
        linha = []
        for j in range(len(self.dados)):
            linha.append((((busca[2][0]-self.dados[j][2][0])**2
                           + (busca[2][1]-self.dados[j][2][1])**2
                           + (busca[2][2]-self.dados[j][2][2])**2
                           + (busca[2][3]-self.dados[j][2][3])**2)**0.5))
        return(linha)

    def k_vizinhos(self, linha: list, k=5):
        """Busca os vizinhos de acordo com frequência \n
        Args: \n
            linha: Lista com as distancia calculadas \n
            k = Com a quantidade de vizinhos que espera retorno. Padrão é igual a 5. \n

        Returns: \n
            Lista com os vizinhos próximos de acordo com parâmetro k.  \n
        """
        tratamento = []
        resultado = []
        tratamento = list(enumerate(linha))
        tratamento = sorted(tratamento, key=lambda x: x[1])
        i = 0
        while i < k:
            resultado.append(tratamento[i])
            i += 1
        return(resultado)

    def retorna_perfil(self, lista: list):
        """Retorna o perfil de acordo com a chave \n
        Args: \n
            lista: Lista com os vizinhos mais próximo \n
        Returns: \n
            Perfil dos vizinhos \n
        """
        resultado = []
        for i in range(len(lista)):
            resultado.append(self.dados[lista[i][0]][1])
        return resultado

    def moda_lista(self, lista: list):
        """Retorna moda referente a lista enviada \n
        Args: \n
            lista: Lista com os vizinhos mais próximo \n
        Returns: \n
            Resultado com a frequência de cada perfil \n
        """
        resultado = {}
        for i in range(len(lista)):
            if(lista[i] in resultado):
                resultado[lista[i]] = resultado[lista[i]] + 1
            else:
                resultado[lista[i]] = 1
        return resultado