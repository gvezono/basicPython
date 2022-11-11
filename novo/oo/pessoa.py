from datetime import datetime as dt


class Pessoa:

    def __init__(self, nome, dt_nascimento, cpf, cargo='Estágio'):
        self.nome = nome
        self.dt_nascimento = self.modela_data_nascimento(dt_nascimento)
        self.cpf = self.modela_cpf(cpf)
        self.cargo = cargo

    # ----- GETTERS -----

    @property
    def nome(self):
        return self._nome

    @property
    def dt_nascimento(self):
        return self._dt_nascimento

    @property
    def cpf(self):
        return self._cpf

    @property
    def cargo(self):
        return self._cargo

    # ----- END GETTERS -----

    # ----- SETTERS -----

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @dt_nascimento.setter
    def dt_nascimento(self, nova_dt_nascimento):
        self._dt_nascimento = nova_dt_nascimento

    @cpf.setter
    def cpf(self, novo_cpf):
        self._cpf = novo_cpf

    @cargo.setter
    def cargo(self, novo_cargo):
        self._cargo = novo_cargo

    # ----- END SETTERS -----

    # STATICS

    @staticmethod
    def modela_data_nascimento(data):
        aux = data.split('/')
        dia_nascimento = int(aux[0])
        mes_nascimento = int(aux[1])
        ano_nascimento = int(aux[2])
        return dt(ano_nascimento, mes_nascimento, dia_nascimento)

    @staticmethod
    def modela_cpf(cpf):
        cpf_list1 = cpf.split('.')
        cpf_list2 = cpf_list1[2].split('-')
        return cpf_list1[0]+cpf_list1[1]+cpf_list2[0]+cpf_list2[1]

    # ----- DEMAIS MÉTODOS -----

    def idade_anos(self):
        hoje = dt.today()
        delta = hoje - self.dt_nascimento
        return delta.days // 365
