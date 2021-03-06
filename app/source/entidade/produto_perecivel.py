from app.source.entidade.lote import Lote
from app.source.entidade.produto_consumivel import ProdutoConsumivel
from app.source.helpers.setter import validacao_tipo


class ProdutoPerecivel(ProdutoConsumivel):
    def __init__(
            self,
            identificador: str,
            nome: str = "",
            descricao: str = "",
            data_fabricacao: str = "",
            categorias: dict = None,
            valor: float = 0.0,
            prioridade: int = 0,
            estoque_quantidade: int = 0,
            estoque_minimo: int = 0,
            lotes: dict = None
    ):
        super().__init__(
            identificador,
            nome,
            descricao,
            data_fabricacao,
            categorias,
            valor,
            prioridade,
            estoque_quantidade,
            estoque_minimo
        )

        if lotes is None:
            lotes = {}

        self.lotes = lotes

    @property
    def lotes(self):
        return self.__lotes

    @lotes.setter
    def lotes(self, lotes: dict):
        validacao_tipo(lotes, dict)
        self.__lotes = lotes
        self.atualizar_estoque()

    def add_lote(self, lote: Lote):
        validacao_tipo(lote, Lote)
        self.__lotes[lote.identificador] = lote
        self.atualizar_estoque()

    def remover_lote(self, identificador: str):
        validacao_tipo(identificador, str)
        del(self.__lotes[identificador])
        self.atualizar_estoque()

    def atualizar_estoque(self):
        self.estoque_quantidade = self.quantidade_total()

    def quantidade_total(self):
        quantidade_total = 0

        for lote in self.lotes.values():
            quantidade_total += lote.quantidade

        return quantidade_total

    def objeto_limite_detalhado(self) -> dict:
        resp = super().objeto_limite_detalhado()
        resp["lotes"] = self.lotes_para_limite(self.lotes)

        return resp

    @staticmethod
    def lotes_para_limite(lotes: dict) -> list:
        validacao_tipo(lotes, dict)

        resp = []
        for lote in lotes.values():
            resp.append(lote.objeto_limite())

        return resp
