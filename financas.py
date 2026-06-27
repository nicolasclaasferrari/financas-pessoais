import json

arquivo = "lancamentos.json"

try:
    f = open(arquivo, "r")
    lancamentos = json.load(f)
    f.close()
except:
    lancamentos = []

while True:

    print("\n===== APP DE FINANÇAS =====")
    print("1 - Registrar")
    print("2 - Extrato")
    print("3 - Relatório")
    print("4 - Exportar")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        print("\n--- REGISTRAR ---")

        data = input("Data: ")
        tipo = input("Tipo (receita/despesa): ")

        while True:
            try:
                valor = float(input("Valor: "))
                break
            except:
                print("Digite apenas números.")

        categoria = input("Categoria: ")
        descricao = input("Descrição: ")

        lancamento = [data, tipo, valor, categoria, descricao]

        lancamentos.append(lancamento)

        f = open(arquivo, "w")
        json.dump(lancamentos, f)
        f.close()

        print("Lançamento salvo!")

    elif opcao == "2":

        print("\n--- EXTRATO ---")

        if len(lancamentos) == 0:
            print("Nenhum lançamento.")
        else:

            for item in lancamentos:

                print("--------------------")
                print("Data:", item[0])
                print("Tipo:", item[1])
                print("Valor:", item[2])
                print("Categoria:", item[3])
                print("Descrição:", item[4])

    elif opcao == "3":

        receitas = 0
        despesas = 0

        categorias = {}

        for item in lancamentos:

            if item[1] == "receita":
                receitas = receitas + item[2]
            else:
                despesas = despesas + item[2]

            if item[3] in categorias:
                categorias[item[3]] = categorias[item[3]] + item[2]
            else:
                categorias[item[3]] = item[2]

        saldo = receitas - despesas

        print("\n--- RELATÓRIO ---")
        print("Receitas:", receitas)
        print("Despesas:", despesas)
        print("Saldo:", saldo)

        print("\nTotal por categoria:")

        for cat in categorias:
            print(cat, ":", categorias[cat])

    elif opcao == "4":

        f = open("relatorio.txt", "w")

        f.write("RELATÓRIO\n\n")

        for item in lancamentos:
            f.write(str(item) + "\n")

        f.close()

        print("Relatório exportado!")

    elif opcao == "5":

        print("Programa encerrado.")
        break

    else:

        print("Opção inválida!")
