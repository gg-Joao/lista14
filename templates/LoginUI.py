import streamlit as st
from agenda import View

class LoginUI:
    @staticmethod
    def main():
        st.title("Login no Sistema")

        if "usuario" in st.session_state:
            usuario = st.session_state["usuario"]
            st.success(f"Você já está logado como: {usuario['nome']}")
            if st.button("Sair"):
                del st.session_state["usuario"]
                st.info("Sessão encerrada com sucesso.")
                st.rerun()
            return

        tipo = st.radio("Entrar como:", ["Profissional", "Cliente"])
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password") if tipo == "Profissional" else st.text_input("Telefone")

        if st.button("Entrar"):
            if tipo == "Profissional":
                usuario = View.autenticar_profissional(email, senha)
            else:
                usuario = View.autenticar_cliente(email, senha)

            if usuario:
                st.session_state["usuario"] = {
                    "id": usuario.id,
                    "nome": usuario.nome,
                    "email": usuario.email,
                    "tipo": tipo
                }
                st.success(f"Bem-vindo, {usuario.nome}!")
                st.rerun()
            else:
                st.error("Dados incorretos. Verifique e tente novamente.")
