  stock = {}

  def adicionar_material(stock):
    item = input("Insira o nome do material: ")
    if item in stock:
      print(f"{item} já existe no nosso stock!")
    else:
      quantidade = int(input(f"Quantidade inicial de {item}: "))
      stock[item] = quantidade
      print(f"{item} foi colocado com sucesso!")
      i = open("stock.txt", "w")
      print(i.write(f"{stock}"))
      i.close()

  def ver_stock():
    x = open("stock.txt", "r")
    print(x.read())
    x.close()

  def mostrar_stock(stock):
    print("\nEstado Geral do Stock:")
    print("Material\tQuantidade")
    print("-" * 30)
    for material, quantidade in stock.items():
      print(f"{material}\t\t{quantidade}")


  def atualizar_stock(stock):
    nome = input("Nome do material a atualizar: ")
    if nome in stock:
      operacao = input("Deseja adicionar (A) ou remover (R)? ").upper()
      quantidade = int(input("Quantidade: "))
      if operacao == "A":
          stock[nome] += quantidade
          print(f"{quantidade} unidade(s) adicionada(s) ao stock de {nome}.")
      elif operacao == "R":
          stock[nome] -= quantidade
          print(f"{quantidade} unidade(s) removida(s) ao stock de {nome}.")
      else:
        print("Quantidade insuficiente em stock!")


  def main():
    while True:
      print("-----------------------------")
      print("      Gestão de Stock")
      print("\n1. Adicionar Material")
      print("2. Ver Stock")
      print("3. Atualizar Stock")
      print("4. Mostrar Stock Geral")
      print("5. Sair")
      print("-----------------------------")
      opcao = input("Escolha uma opção: ")

      if opcao == "1":
        adicionar_material(stock)
      elif opcao == "2":
        ver_stock()
      elif opcao == "3":
        atualizar_stock(stock)
      elif opcao == "4":
        mostrar_stock(stock)
      elif opcao == "5":
        print("Encerrando o programa...")
        break
      else:
          print("Opção inválida! Escolha outra opção.")

  if __name__ == "__main__":
    main()
