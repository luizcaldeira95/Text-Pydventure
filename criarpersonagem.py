# Codigo para a criação de personagens levando em conta um sistema simplificado de D&D

from glossario import descricaoRacas



def criar ():
    
    #Boco de texto de introdução, apresentação da sessão de criar personagem
    print("""
          
<!!! CRIE SEU PERSONAGEM !!!>

""")
    
    # Bloco de codigo que define um nome para o personagem principal 
    confirmarNome = "EsperarConfirmacao"
    while confirmarNome != "s" and confirmarNome != "S":
        nome = input("Escolha um nome para o seu personagem:\n\n")
        confirmarNome = input("\n\nVocê escolheu " + nome + " esta correto? [s,n]\n\n")
        if confirmarNome == "s" or "S":
            break
    
    # Bloco de codigo que define uma raça para o personagem principal

    confirmarRaca = "3sP3r4r"
    while confirmarRaca != "s" and confirmarRaca != "S":
        
        while confirmarRaca != 's' or confirmarRaca != 'S': 
            Raca = input ("""\nEscolha a raça do seu personagem:\n**Para informações sobre as raças disponiveis, digite [i]**
\nHumano  [H]  Elfo  [E]  Anão  [A]\n\n""")
            if Raca == "i" or Raca == "I":
                descricaoRacas()
            elif Raca == "h" or Raca == ("H") or Raca == "Humano" or Raca == "humano" or Raca == "HUMANO":
                Raca = "Humano"
                confirmarRaca = input("\nVocê escolheu Humano(a), deseja confirmar? [s] [n] \n\n")
                if confirmarRaca == "s" or confirmarRaca == "S":
                    break
            elif Raca == "e" or Raca == ("E") or Raca == "Elfo" or Raca == "ELFO" or Raca == "elfo":
                Raca = "Elfo"
                confirmarRaca = input("\nVocê escolheu Elfo(a), deseja confirmar? [s] [n]\n\n")
                if confirmarRaca == "s" or confirmarRaca == "S":
                    break
            elif Raca == "a" or Raca == "A" or Raca == "Anão" or Raca == "Anao" or Raca == "anao" or Raca == "anão" or Raca == "ANÃO" or Raca == "ANAO":
                Raca = "Anao"
                confirmarRaca = input("\n\nVocê escolheu Anão(a), deseja confirmar?\n\n")
                if confirmarRaca == "s" or confirmarRaca == "S":
                    break
            else:
                print("""\n\nNão entendi o que voce disse
.
.
.""")
                continue
        if confirmarRaca == "s" or confirmarRaca == "S":
            print('\n\nParabéns meu amigo, estamos indo bem mas so programei ate aqui haha :)')
            print("Em breve adicionarei novas funcionalidades ao jogo... obrigado pelo seu apoio :pp\n\n")

criar()