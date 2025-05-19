filme = []
livro = []
serie = []
jogo = []

print("-" * 15 + "CATALOGO" + "-" * 15)

while True:
    op = int(input("\n1. Cadastrar \n2. Series \n3. Filme \n4. Livro \n5. Jogo \n6. Sair\n"))
    
    if op == 1:
        op2 = int(input("\n1. Serie \n2. Filme \n3. Livro \n4. Jogo \n5. Sair \n"))
        
        if op2 == 1:
            nome = str(input("Digite o nome: ")).lower()
            ano = int(input("Digite o ano de lançamento: "))
            autor = str(input("Digite o nome do autor/a: ")).lower()
            genero = str(input("Digite o gênero: ")).lower()
            inicial = nome[0]
            conjunto = {"nome": nome, "ano": ano, "autor": autor, "genero": genero, "inicial": inicial}
            serie.append(conjunto)
        
        elif op2 == 2:
            nome = str(input("Digite o nome: ")).lower()
            ano = int(input("Digite o ano de lançamento: "))
            autor = str(input("Digite o nome do diretor/a: ")).lower()
            genero = str(input("Digite o gênero: ")).lower()
            inicial = nome[0]
            conjunto = {"nome": nome, "ano": ano, "autor": autor, "genero": genero, "inicial": inicial}
            filme.append(conjunto)
        
        elif op2 == 3:
            nome = str(input("Digite o nome: ")).lower()
            ano = int(input("Digite o ano de lançamento: "))
            autor = str(input("Digite o nome do autor/a: ")).lower()
            genero = str(input("Digite o gênero: ")).lower()
            inicial = nome[0]
            conjunto = {"nome": nome, "ano": ano, "autor": autor, "genero": genero, "inicial": inicial}
            livro.append(conjunto)
        
        elif op2 == 4:
            nome = str(input("Digite o nome: ")).lower()
            ano = int(input("Digite o ano de lançamento: "))
            autor = str(input("Digite o nome do autor/a: ")).lower()
            genero = str(input("Digite o gênero: ")).lower()
            inicial = nome[0]
            conjunto = {"nome": nome, "ano": ano, "autor": autor, "genero": genero, "inicial": inicial}
            jogo.append(conjunto)
        
        elif op2 == 5:
            print("Você saiu")
        
        else:
            print("Opção inválida")
    
    elif op == 2:  
        op3 = int(input("Deseja pesquisar por: \n1. Autor \n2. Ano \n3. Gênero \n4. Inicial \n5. Sair\n"))
        
        if op3 == 1:
            filtro = str(input("Digite o nome do autor/a: ")).lower()
            for elemento in serie:
                if elemento["autor"] == filtro:
                    print(f"Séries encontradas desse autor: {elemento}")
        
        elif op3 == 2:
            filtro = int(input("Digite o ano de lançamento: "))
            for elemento in serie:
                if elemento["ano"] == filtro:
                    print(f"Séries encontradas desse ano: {elemento}")
        
        elif op3 == 3:
            filtro = str(input("Digite o gênero: ")).lower()
            for elemento in serie:
                if elemento["genero"] == filtro:
                    print(f"Séries encontradas desse gênero: {elemento}")
        
        elif op3 == 4:
            filtro = str(input("Digite inicial: ")).lower()
            for elemento in serie:
                if elemento["inicial"] == filtro:
                    print(f"Séries encontradas com essa inicial: {elemento}")
        
        elif op3 == 5:
            print("Você saiu")
    
    elif op == 3:  
        op4 = int(input("Deseja pesquisar por: \n1. Autor \n2. Ano \n3. Gênero \n4. Inicial \n5. Sair\n"))
        
        if op4 == 1:
            filtro = str(input("Digite o nome do autor/a: ")).lower()
            for elemento in filme:
                if elemento["autor"] == filtro:
                    print(f"Filmes encontrados desse autor: {elemento}")
        
        elif op4 == 2:
            filtro = int(input("Digite o ano de lançamento: "))
            for elemento in filme:
                if elemento["ano"] == filtro:
                    print(f"Filmes encontrados desse ano: {elemento}")
        
        elif op4 == 3:
            filtro = str(input("Digite o gênero: ")).lower()
            for elemento in filme:
                if elemento["genero"] == filtro:
                    print(f"Filmes encontrados desse gênero: {elemento}")
        
        elif op4 == 4:
            filtro = str(input("Digite inicial: ")).lower()
            for elemento in filme:
                if elemento["inicial"] == filtro:
                    print(f"Filmes encontrados com essa inicial: {elemento}")
        
        elif op4 == 5:
            print("Você saiu")
    
    elif op == 4:  # Livro
        op5 = int(input("Deseja pesquisar por: \n1. Autor \n2. Ano \n3. Gênero \n4. Inicial \n5. Sair\n"))
        
        if op5 == 1:
            filtro = str(input("Digite o nome do autor/a: ")).lower()
            for elemento in livro:
                if elemento["autor"] == filtro:
                    print(f"Livros encontrados desse autor: {elemento}")
        
        elif op5 == 2:
            filtro = int(input("Digite o ano de lançamento: "))
            for elemento in livro:
                if elemento["ano"] == filtro:
                    print(f"Livros encontrados desse ano: {elemento}")
        
        elif op5 == 3:
            filtro = str(input("Digite o gênero: ")).lower()
            for elemento in livro:
                if elemento["genero"] == filtro:
                    print(f"Livros encontrados desse gênero: {elemento}")
        
        elif op5 == 4:
            filtro = str(input("Digite inicial: ")).lower()
            for elemento in livro:
                if elemento["inicial"] == filtro:
                    print(f"Livros encontrados com essa inicial: {elemento}")
        
        elif op5 == 5:
            print("Você saiu")
    
    elif op == 5:  # Jogo
        op6 = int(input("Deseja pesquisar por: \n1. Autor \n2. Ano \n3. Gênero \n4. Inicial \n5. Sair\n"))
        
        if op6 == 1:
            filtro = str(input("Digite o nome do autor/a: ")).lower()
            for elemento in jogo:
                if elemento["autor"] == filtro:
                    print(f"Jogos encontrados desse autor: {elemento}")
        
        elif op6 == 2:
            filtro = int(input("Digite o ano de lançamento: "))
            for elemento in jogo:
                if elemento["ano"] == filtro:
                    print(f"Jogos encontrados desse ano: {elemento}")
        
        elif op6 == 3:
            filtro = str(input("Digite o gênero: ")).lower()
            for elemento in jogo:
                if elemento["genero"] == filtro:
                    print(f"Jogos encontrados desse gênero: {elemento}")
        
        elif op6 == 4:
            filtro = str(input("Digite inicial: ")).lower()
            for elemento in jogo:
                if elemento["inicial"] == filtro:
                    print(f"Jogos encontrados com essa inicial: {elemento}")
        
        elif op6 == 5:
            print("Você saiu")
    
    elif op == 6:
        print("Você saiu")
        break
