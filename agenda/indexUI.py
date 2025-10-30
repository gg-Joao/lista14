
import streamlit as st
from templates.manterClienteUI import ManterClienteUI
from templates.manterServicoUI import ManterServicoUI
from templates.manterProfissionalUI import ManterProfissionalUI
from templates.manterHorarioUI import ManterHorarioUI
from templates.LoginUI import LoginUI
from templates.PerfilUI import PerfilUI

class IndexUI:

    @staticmethod
    def main():
        st.sidebar.title("Sistema de Agendamento")
        menu = [
            "Entrar no Sistema",
            "Meu Perfil",
            "Clientes",
            "Serviços",
            "Profissionais",
            "Horários"
        ]
        escolha = st.sidebar.radio("Navegação", menu)

        if "usuario" not in st.session_state and escolha not in ["Entrar no Sistema"]:
            st.warning("Você precisa entrar no sistema primeiro.")
            LoginUI.main()
            return

        if escolha == "Entrar no Sistema":
            LoginUI.main()
        elif escolha == "Meu Perfil":
            PerfilUI.main()
        elif escolha == "Clientes":
            ManterClienteUI.main()
        elif escolha == "Serviços":
            ManterServicoUI.main()
        elif escolha == "Profissionais":
            ManterProfissionalUI.main()
        elif escolha == "Horários":
            ManterHorarioUI.main()

if __name__ == "__main__":
    IndexUI.main()
