# Importando SQLite3
import sqlite3 as lite

# Criando conexao
try:
	con = lite.connect('cadastro_alunos.db')
	print('Conexao com o Banco de Dados realizada com sucesso!')
except lite.Error as e:
	print('Erro ao conectar com o Banco de Dados:', e)


# Tabela de Cursos ------------------------------------------------------

# Criar Cursos (Create C)
def criar_curso(i):
	with con:
		cur = con.cursor()
		query = "INSERT INTO Cursos (nome, duracao, preco) VALUES (?,?,?)"
		cur.execute(query,i)

#criar_curso(['Python','Semanas','50'])

# Ver todos os cursos (Read R)
def ver_cursos():
	lista = []
	with con:
		cur = con.cursor()
		cur.execute('SELECT * FROM Cursos')
		linha = cur.fetchall()

		for i in linha:
			lista.append(i)
		return lista

# Atualizar Cursos (Update U)
def atualizar_curso(i):
	with con:
		cur = con.cursor()
		query = "UPDATE Cursos SET nome=?, duracao=?, preco=? WHERE id=?"
		cur.execute(query,i)

l = ['Python', 'Duas Semanas', 50.0, 1]

#atualizar_curso(l)

# Deletar Cursos (Delete D)
def deletar_curso(i):
	with con:
		cur = con.cursor()
		query = "DELETE FROM Cursos WHERE id=?"
		cur.execute(query,i)

#deletar_curso([1])


# Tabela de Turmas ------------------------------------------------------

# Criar Turmas (Create C)
def criar_turma(i):
	with con:
		cur = con.cursor()
		query = "INSERT INTO Turmas (nome, curso_nome, data_inicio) VALUES (?,?,?)"
		cur.execute(query,i)

# Ver todos as Turmas (Read R)
def ver_turmas():
	lista = []
	with con:
		cur = con.cursor()
		cur.execute('SELECT * FROM Turmas')
		linha = cur.fetchall()

		for i in linha:
			lista.append(i)
		return lista

# Atualizar Turmas (Update U)
def atualizar_turma(i):
	with con:
		cur = con.cursor()
		query = "UPDATE turmas SET nome=?, curso_nome=?, data_inicio=? WHERE id=?"
		cur.execute(query,i)

# Deletar Turmas (Delete D)
def deletar_turma(i):
	with con:
		cur = con.cursor()
		query = "DELETE FROM Turmas WHERE id=?"
		cur.execute(query,i)


# Tabela de Alunos ------------------------------------------------------

# Criar Alunos (Create C)
def criar_aluno(i):
	with con:
		cur = con.cursor()
		query = "INSERT INTO Alunos (nome, email, telefone, sexo, imagem, data_nascimento, cpf, turma_nome) VALUES (?,?,?,?,?,?,?,?)"
		cur.execute(query,i)

# Ver todos as Alunos (Read R)
def ver_alunos():
	lista = []
	with con:
		cur = con.cursor()
		cur.execute('SELECT * FROM Alunos')
		linha = cur.fetchall()

		for i in linha:
			lista.append(i)
		return lista

# Atualizar Alunos (Update U)
def atualizar_aluno(i):
	with con:
		cur = con.cursor()
		query = "UPDATE Alunos SET nome=?, email=?, telefone=?, sexo=?, imagem=?, data_nascimento=?, cpf=?, turma_nome=? WHERE id=?"
		cur.execute(query,i)

# Deletar Alunos (Delete D)
def deletar_aluno(i):
	with con:
		cur = con.cursor()
		query = "DELETE FROM Alunos WHERE id=?"
		cur.execute(query,i)