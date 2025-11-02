from models.horario import Horario
from models.horarioDAO import HorarioDAO
from models.agendamentoDAO import AgendamentoDAO

class View:
    @staticmethod
    def horario_listar():
        return HorarioDAO.listar()

    @staticmethod
    def horario_inserir(data, hora, id_profissional):
        horarios = HorarioDAO.listar()

        for h in horarios:
            h_data = h.get_data() if hasattr(h, "get_data") else getattr(h, "data", None)
            h_hora = h.get_hora() if hasattr(h, "get_hora") else getattr(h, "hora", None)
            h_prof = h.get_id_profissional() if hasattr(h, "get_id_profissional") else getattr(h, "id_profissional", None)
            if h_data == data and h_hora == hora and h_prof == id_profissional:
                raise ValueError("Já existe um horário igual para este profissional.")
        HorarioDAO.inserir(Horario(0, data, hora, id_profissional))

    @staticmethod
    def horario_atualizar(id, data, hora, id_profissional):
        horarios = HorarioDAO.listar()

        for h in horarios:
            h_id = h.get_id() if hasattr(h, "get_id") else getattr(h, "id", None)
            h_data = h.get_data() if hasattr(h, "get_data") else getattr(h, "data", None)
            h_hora = h.get_hora() if hasattr(h, "get_hora") else getattr(h, "hora", None)
            h_prof = h.get_id_profissional() if hasattr(h, "get_id_profissional") else getattr(h, "id_profissional", None)
            if h_id != id and h_data == data and h_hora == hora and h_prof == id_profissional:
                raise ValueError("Já existe um horário igual para este profissional.")
        HorarioDAO.atualizar(Horario(id, data, hora, id_profissional))

    @staticmethod
    def horario_excluir(id):
        agendamentos = AgendamentoDAO.listar()
        # localizar o horário para comparar data/hora/profissional
        horario = next(
            (h for h in HorarioDAO.listar()
             if (h.get_id() if hasattr(h, "get_id") else getattr(h, "id", None)) == id),
            None
        )
        hd = horario.get_data() if horario and hasattr(horario, "get_data") else (horario.data if horario else None)
        hh = horario.get_hora() if horario and hasattr(horario, "get_hora") else (horario.hora if horario else None)
        hp = horario.get_id_profissional() if horario and hasattr(horario, "get_id_profissional") else (horario.id_profissional if horario else None)

        for a in agendamentos:
            # verifica ligação explícita por id_horario ou por data/hora/profissional
            if getattr(a, "id_horario", None) == id:
                raise ValueError("Este horário já foi agendado por um cliente e não pode ser excluído.")
            if hd is not None and hh is not None and hp is not None:
                if getattr(a, "data", None) == hd and getattr(a, "hora", None) == hh and getattr(a, "id_profissional", None) == hp:
                    raise ValueError("Este horário já foi agendado por um cliente e não pode ser excluído.")
        HorarioDAO.excluir(id)
