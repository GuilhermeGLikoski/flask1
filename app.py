from flask import Flask, render_template, request, redirect, url_for

# cria uma instancia 
app = Flask(__name__)

# lista
tarefas = []
# contado de id para atribuir em cada tarefa
contador_id = 1

# rota principal que me apresenta todas as tarefas 
@app.route('/')
def listar_tarefas():
    # renderiza o 'index.html' e passa a lista de tarefas para ele
    return render_template('index.html', tarefas=tarefas)

# rota que mostra o envio do formulário para adicionar uma nova tarefa
@app.route('/adicionar', methods=['POST'])
def adicionar_tarefa():
    # para modificar a variavel
    global contador_id
    # recebe a descrição da tarefa enviada pelo formulario
    descricao = request.form['descricao']
    # cria um dicionário representando a nova tarefa
    nova_tarefa = {'id': contador_id, 'descricao': descricao, 'concluida': False}
    # Adiciona a nova tarefa
    tarefas.append(nova_tarefa)
    # incrementa o contador para o ID da próxima tarefa
    contador_id += 1
    # redireciona o usuario de volta para a página principal para ver a lista atualizada
    return redirect(url_for('listar_tarefas'))

# garante que o servidor flask só rode se o script for executado diretamente
if __name__ == '__main__':

    # mostra os erros e tem recarregamento automático
    app.run(debug=True)








        # EXPLICANDO COMANDOS ESPECIFICOS
# def:  definir nova funcao
# return: pode ser duas coisas-1) especificar o valor que uma funcao deve retornar. 2) encerrar a execucao da funcao. ("nesse caso e a primeira opcao")
# global: permite que voce acesse e modifique variaveis que foram definidas fora dela.
# request.form: e um objeto que contem os dados do formulario que foi enviado.
# nova_tarefa: cria um dicionario em py. ('concluida: False') significa que quando ela e criada, seu status sera nao concluida.
# append(): adiciona o item que voce escreve ao final da lista.
# contador_id += 1: apos todos os passos anteriores, adiciona 1 a variavel, essa linha garante que cada tarefa receba um ID diferente do anterior.
# url_for: gera a URL para uma rota com base no nome da função que define essa rota.
# redirect(): resposta HTTP que leva o navegador do usuário a fazer uma nova requisição para uma URL diferente.
