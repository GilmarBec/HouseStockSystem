from app.source.limite_console.limite_abstrato import LimiteAbstrato


class LimiteProduto(LimiteAbstrato):

    def opcoes(self) -> dict:
        return {
            "listar": {
                "menu": "Opções: \n" +
                " - Criar novo produto (c) \n" +
                " - Atualizar produto (a) \n" +
                " - Mostrar detalhes do produto (m) \n" +
                " - Deletar produto (d) \n" +
                " - Voltar (v) \n\n: ",
            },
            "formulario": {
                "codigo_referencia": "Código de referência: ",
                "nome": "Nome: ",
                "descricao": "Descrição: ",
                "data_fabricacao": "Data de fabricação: ",
                "valor": "Valor: ",
                "prioridade": "Prioridade: ",
                "estoque": "Quantidade em estoque: ",
                "estoque_minimo": "Estoque mínimo: ",
                "tem_categorias": "Tem categorias? ",
                "eh_perecivel": "É perecível? "
            },
            "mostrar": {
                "codigo_referencia": "Código de referência: "
            },
            "deletar": {
                "codigo_referencia": "Código de referência: "
            },
            "categorias": {
                "codigo_referencia": "Código de referência: ",
            }
        }

    def listar(self, produtos: list or None = None):
        super().cabecalho()
        print("=================>  Listagem de produtos  <=================")
        self.cabecalho()

        if isinstance(produtos, list) and len(produtos) > 0:
            self.gerar_tabela(
                produtos,
                produtos[0].keys()
            )

        self.roda_pe()

    def criar(self):
        super().cabecalho()
        print("==================>  Criação de produto  <==================")
        self.cabecalho()

    def atualizar(self):
        super().cabecalho()
        print("==================>  Edição de produto   <==================")
        self.cabecalho()

    def mostrar(self, produto: dict):
        super().cabecalho()
        print("=================>  Detalhes de produtos  <================")
        self.cabecalho()

        if isinstance(produto, dict):
            for atributo in produto:
                valor = produto.get(atributo)

                if isinstance(valor, dict):
                    print(f"{atributo}: ")
                    for entidade in valor:
                        entidade = valor.get(entidade)

                        for propriedade in entidade:
                            print("- {atributo}: {valor}".format(atributo=propriedade, valor=entidade.get(propriedade)))

                        print("----------------------------------------")
                    continue

                print("{atributo}: {valor}".format(atributo=atributo, valor=valor))

    def categorias(self):
        super().cabecalho()
        print("===========>  Adicionar categorias no produto   <===========")
        self.cabecalho()

    def cabecalho(self):
        super().cabecalho()
        print("")
