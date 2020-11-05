from abc import ABC
from app.source.entidade.entidade_abstrata import EntidadeAbstrata
from app.source.limite.limite_abstrato import LimiteAbstrato
from app.source.exception.rotaInexistenteException import RotaInexistenteException
from app.source.helpers.setter import validacao_tipo


class ControleAbstrato(ABC):
    def __init__(
            self,
            limite: LimiteAbstrato,
            entidades: dict or None = None
    ):
        self.limite = limite
        self.entidades = entidades

    def rotas(self, nome_funcao) -> dict:
        rota = {
            "listar": {
                "c": self.criar,
                "a": self.atualizar,
                "d": self.deletar,
                "v": self.voltar_listagem,
            },
            "criar": {
                "v": self.listar,
            },
            "atualizar": {
                "v": self.listar,
            },
            "show": {
                "v": self.listar
            }
        }

        try:
            return rota[nome_funcao]
        except KeyError:
            raise RotaInexistenteException("Rota passada não existente.")

    def selecione_rota(self, rotas: dict, opcao: str, funcao):
        try:
            rotas[opcao]()
        except KeyError:
            self.limite.erro("Opção passada não existe, digite novamente.")
            funcao()

    def listar(self):
        raise Exception("Método [Listar] não permitido para este controle[%s]".format(self.__class__.__name__))

    def criar(self):
        raise Exception("Método [Criar] não permitido para este controle[%s]".format(self.__class__.__name__))

    def atualizar(self):
        raise Exception("Método [Atualizar] não permitido para este controle[%s]".format(self.__class__.__name__))

    def deletar(self):
        raise Exception("Método [Deletar] não permitido para este controle[%s]".format(self.__class__.__name__))

    def voltar_listagem(self):
        exit(0)

    def exportar_entidades(self) -> list:
        resp = []
        for chave in self.entidades:
            resp.append(self.entidades[chave].objeto_limite())

        return resp

    @property
    def entidades(self) -> dict:
        return self.__entidades

    @entidades.setter
    def entidades(self, entidades: dict or None = None):
        if entidades is None:
            entidades = {}

        validacao_tipo(entidades, dict)

        for entidade in entidades.values():
            if entidade is not None:
                validacao_tipo(entidade, self.classe_entidade())

        self.__entidades = entidades

    def adicionar_entidade(self, tipo_entidade: str, entidade: EntidadeAbstrata):
        validacao_tipo(tipo_entidade, str)
        validacao_tipo(entidade, self.classe_entidade())
        self.__entidades[tipo_entidade][entidade.identificador] = entidade

        return self

    def remover_entidade(self, entidade: EntidadeAbstrata):
        validacao_tipo(entidade, self.classe_entidade())
        del(self.__entidades[entidade.identificador])

        return self

    @staticmethod
    def classe_entidade() -> type:
        return EntidadeAbstrata

    @property
    def limite(self) -> LimiteAbstrato:
        return self.__limite

    @limite.setter
    def limite(self, limite: LimiteAbstrato):
        validacao_tipo(limite, self.classe_limite())
        self.__limite = limite

    @staticmethod
    def classe_limite() -> type:
        return LimiteAbstrato
