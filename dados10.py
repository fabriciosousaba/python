import sqlite3


class produto:
    def __init__(self,preco,nome,quantidade):
        self.preco=preco
        self.quantidade=quantidade
        self.nome=nome

    def salvar(self):
        conexao= sqlite3.connect("produto.db")
        cursor= conexao.cursor()

        cursor.execute(
            """
            create table if not exists produtos(
            id integer primary key autoincrement,
            nome text,
            preco real,
            quantidade integer
        )
       """
        

        )

        cursor.execute(
           "insert into produtos (preco, nome, quantidade) values (?, ?, ?)",
            (self.preco, self.nome, self.quantidade)
        )     

        conexao.commit() 
        conexao.close()

    def imformacoes(self):
        print(f"o preco= {self.preco} o nome= {self.nome}  a quantidade= {self.quantidade}")

    def atualizar(self, id_produto):
        novo_preco = float(input("Digite o novo preço: "))
        nova_quantidade = int(input("Digite a nova quantidade: "))

        conexao = sqlite3.connect("produto.db")
        cursor = conexao.cursor()

        cursor.execute(
            "update produtos set preco = ?, quantidade = ? where id = ?",
            (novo_preco, nova_quantidade, id_produto)
        )

        conexao.commit()
        conexao.close()

try:

        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade do produto: "))

        produto1 = produto(preco, nome, quantidade)
        produto1.salvar()
        produto1.imformacoes()

        id_produto = int(input("Digite o ID do produto que deseja atualizar: "))
        produto1.atualizar(id_produto)
        print("Produto atualizado com sucesso!")

except Exception as erro:
        print(f"Erro ao salvar o produto: {erro}")

finally:
     print(f"terminol")        