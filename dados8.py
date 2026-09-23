import sqlite3

class cliente:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade


    def salvar(self):
        conexao= sqlite3.connect("cliente.db")
        cursor= conexao.cursor()


        cursor.execute(
            """
            create table if not exists nomes(
            id integer primary key autoincrement,
             nome text,
             idade integer    
        )
        """
        )

        cursor.execute(
            "insert into nomes (nome, idade) values (?, ?) ",
             (self.nome, self.idade)
        )

        conexao.commit()        
        conexao.close()
        
    def  imformacoes(self):
        print(f"o nome= {self.nome} a idade= {self.idade}")

if __name__=="__main__":
    try:

       cliente1= cliente("rodrigo", 26)
       cliente1.salvar()
       cliente1.imformacoes()

    except  Exception as erro:
        print(f"erro: {erro}") 

    finally:
        print(f"terminol")    
    
