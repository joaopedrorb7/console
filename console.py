#catalogo
filme=[]
livro=[]
serie=[]
jogo=[]
print("-"*15+"CATALOGO"+"-"*15)
while True:
    op=int(input("\n1.cadastrar \n2.series \n3.filme \n4.livro \n5.jogo \n6.sair\n"))
    if op==1:#cadastrar
        op2=int(input("\n1.serie \n2.filme \n3.livro \n4.jogo \n5.sair \n"))
        if op2==1:
            nome=str(input("digite o nome:")).lower()
            ano=int(input("digite o ano de lançamento"))
            autor=str(input("digite o nome da autor/a:")).lower()
            genero=str(input("digite o genero:")).lower()
            inicial=nome[0]
            conjunto={"nome":nome ,"ano":ano ,"autor":autor ,"genero":genero,"inicial":inicial}
            serie.append(conjunto)
        elif op2==2:
            nome=str(input("digite o nome:")).lower()
            ano=int(input("digite o ano de lançamento"))
            autor=str(input("digite o nome do diretor/a:")).lower()
            genero=str(input("digite o genero:")).lower()
            inicial=nome[0]
            conjunto={"nome":nome ,"ano":ano ,"autor":autor ,"genero":genero,"inicial":inicial}
            filme.append(conjunto)
        elif op2==3:
            nome=str(input("digite o nome:")).lower()
            ano=int(input("digite o ano de lançamento"))
            autor=str(input("digite o nome da autor/a:")).lower()
            genero=str(input("digite o genero:")).lower()
            inicial=nome[0]
            conjunto={"nome":nome ,"ano":ano ,"autor":autor ,"genero":genero,"inicial":inicial}
            livro.append(conjunto)
        elif op2==4:
            nome=str(input("digite o nome:")).lower()
            ano=int(input("digite o ano de lançamento"))
            autor=str(input("digite o nome da autor/a:")).lower()
            genero=str(input("digite o genero:")).lower()
            inicial=nome[0]
            conjunto={"nome":nome ,"ano":ano ,"autor":autor ,"genero":genero,"inicial":inicial}
            jogo.append(conjunto) 
        elif op2==5:   
            print("voce saiu")
          
        else:
            print("opção invalida")
           
    elif op==2:#series
        op3=int(input("deseja psquisar por: \n1.autor \n2.ano \n3.genero \n4.inicial \n5.sair\n"))
        if op3==1:
            filtro=str(input("digite o nom do autor/a:")).lower()
            for elemento in serie:
                if elemento["autor"]==filtro:
                    print(f"series encontradas desse autor:{elmento}")
        elif op3==2:     
            filtro=int(input("digite o ano de lançamento:"))
            for elemento in serie:
                if elemento["ano"]==filtro:
                    print(f"series encontradas desse ano:{elmento}") 
        elif op3==3:        
            filtro=str(input("digite o genero:")).lower()
            for elemento in serie:
                if elemento["genero"]==filtro:
                    print(f"series encontradas desse genero:{elmento}")   
        elif op3==4:
            filtro=str(input("digite inicial:")).lower()
            for elemento in serie:
                if elemento["inicial"]==filtro:
                    print(f"series encontradas com essa inicial:{elmento}")
        elif op3==5:
            print("voce saiu")
    elif op==3: 
         op4=int(input("deseja psquisar por: \n1.autor \n2.ano \n3.genero \n4.inicial \n5.sair\n"))
        if op3==1:
            filtro=str(input("digite o nom do autor/a:")).lower()
            for elemento in filme:
                if elemento["autor"]==filtro:
                    print(f"filmes encontradas desse autor:{elmento}")
        elif op4==2:     
            filtro=int(input("digite o ano de lançamento:"))
            for elemento in filme:
                if elemento["ano"]==filtro:
                    print(f"filmes encontradas desse ano:{elmento}") 
        elif op4==3:        
            filtro=str(input("digite o genero:")).lower()
            for elemento in filme:
                if elemento["genero"]==filtro:
                    print(f"filmes encontradas desse genero:{elmento}")   
        elif op4==4:
            filtro=str(input("digite inicial:")).lower()
            for elemento in filme:
                if elemento["inicial"]==filtro:
                    print(f"filmes encontradas com essa inicial:{elmento}")
        elif op4==5:
            print("voce saiu")      
    elif op==4:#livro
         op5=int(input("deseja psquisar por: \n1.autor \n2.ano \n3.genero \n4.inicial \n5.sair\n"))
        if op5==1:
            filtro=str(input("digite o nom do autor/a:")).lower()
            for elemento in livro:
                if elemento["autor"]==filtro:
                    print(f"livros encontradas desse autor:{elmento}")
        elif op5==2:     
            filtro=int(input("digite o ano de lançamento:"))
            for elemento in livro:
                if elemento["ano"]==filtro:
                    print(f"livros encontradas desse ano:{elmento}") 
        elif op5==3:        
            filtro=str(input("digite o genero:")).lower()
            for elemento in livro:
                if elemento["genero"]==filtro:
                    print(f"livros encontradas desse genero:{elmento}")   
        elif op5==4:
            filtro=str(input("digite inicial:")).lower()
            for elemento in livro:
                if elemento["inicial"]==filtro:
                    print(f"livros encontradas com essa inicial:{elmento}")
        elif op5==5:
            print("voce saiu")
    elif op==5:#jogo
         op6=int(input("deseja psquisar por: \n1.autor \n2.ano \n3.genero \n4.inicial \n5.sair\n"))
        if op6==1:
            filtro=str(input("digite o nom do autor/a:")).lower()
            for elemento in jogo:
                if elemento["autor"]==filtro:
                    print(f"jogo encontradas desse autor:{elmento}")
        elif op6==2:     
            filtro=int(input("digite o ano de lançamento:"))
            for elemento in jogo:
                if elemento["ano"]==filtro:
                    print(f"jogo encontradas desse ano:{elmento}") 
        elif op6==3:        
            filtro=str(input("digite o genero:")).lower()
            for elemento in jogo:
                if elemento["genero"]==filtro:
                    print(f"jogos encontradas desse genero:{elmento}")   
        elif op6==4:
            filtro=str(input("digite inicial:")).lower()
            for elemento in jogo:
                if elemento["inicial"]==filtro:
                    print(f"jogos encontradas com essa inicial:{elmento}")
        elif op6==5:
            print("voce saiu")
    elif op== 6:
        print("voce saiu")
        break       
