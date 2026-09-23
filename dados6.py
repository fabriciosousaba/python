import sqlite3


class loja:
    def __init__(self,produto,valor):
        self.produto=produto
        self.valor=valor

    def salvar(self):
        conexao= sqlite3.connect("loja.db")       
        cursor= conexao.cursor()

        cursor.execute(
            """
            create table if not  exists produtos(
            id integer primary key Autoincrement,
            produto text,
            valor real
            )
            """
        
        )

        cursor.execute(
            "insert into produtos (produto, valor) values (?, ?)",
             (self.produto, self.valor)
            
        )

        conexao.commit()
        conexao.close()

    def imformacoes(self):
        print(f"o produto= {self.produto} o valor= {self.valor}")


if __name__=="__main__":
    try:

       loja1= loja("garrafa", 26)
       loja1.salvar()
       loja1.imformacoes()

    except Exception as erro:
        print(f"erro: {erro}")

    finally:
        print(f"terminol")                