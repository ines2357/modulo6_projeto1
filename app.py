from flask import Flask, render_template, request
import fornecedores
import consumidor
import transportadoras


app = Flask(__name__)

@app.route('/api/produtos', methods=['GET'])
def get_produtos():
    produtos = fornecedores.obter_produtos_disponiveis()
    return jsonify(produtos)

@app.route('/escolher_produto', methods=['POST'])
def escolher_produto():
    produto_nome = request.form['produto_nome']
    produto_nome = consumidor.escolher_produto(produto_nome)
    
    pontuacoes_por_produto_localizacao, scores_fornecedores = fornecedores.somar_pontuacoes_por_produto_localizacao()
    pontuacoes_por_transportadora_origem, scores_transportadoras = transportadoras.somar_pontuacoes_por_transportadora_origem()

    impactos_fornecedores = [
        (localizacao, pontuacao) 
        for (produto, localizacao), pontuacao in pontuacoes_por_produto_localizacao.items() 
        if produto == produto_nome
    ]
    
    impactos_transportadoras = [
        (origem_percurso, pontuacao) 
        for (transportadora, origem_percurso), pontuacao in pontuacoes_por_transportadora_origem.items()
    ]
    
    impactos_totais = []
    for (localizacao, impacto_fornecedor) in impactos_fornecedores:
        impacto_transporte = next(
            (impacto for (origem_percurso, impacto) in impactos_transportadoras if origem_percurso == localizacao),
            0
        )
        impacto_total = impacto_fornecedor + impacto_transporte
        impactos_totais.append((localizacao, impacto_total))

    menor_impacto = min(impactos_totais, key=lambda x: x[1])
    localizacao_menor_impacto, impacto_total = menor_impacto

    return render_template('resultado.html', 
                           produto=produto_nome,
                           impactos=impactos_totais, 
                           menor_impacto=(localizacao_menor_impacto, impacto_total))




@app.route('/resumo_impactos')
def resumo_impactos():
    pontuacoes_por_produto_localizacao, scores_fornecedores = fornecedores.somar_pontuacoes_por_produto_localizacao()
    pontuacoes_por_transportadora_origem, scores_transportadoras = transportadoras.somar_pontuacoes_por_transportadora_origem()

    dados_resumo = []

    for (produto, localizacao), pontuacao in scores_fornecedores.items():
        
        score_agua = pontuacao[0] if len(pontuacao) > 0 else 0
        score_eletricidade = pontuacao[1] if len(pontuacao) > 1 else 0
        score_combustiveis = pontuacao[2] if len(pontuacao) > 2 else 0
        score_desperdicio = pontuacao[3] if len(pontuacao) > 3 else 0
        score_contaminacao = pontuacao[4] if len(pontuacao) > 4 else 0
        score_emissoes = pontuacao[5] if len(pontuacao) > 5 else 0

        transportadora_data = next(
            (data for (transportadora, origem), data in scores_transportadoras.items() if origem == localizacao),
            None
        )


        if transportadora_data:
         
            score_combustivel = transportadora_data[0] if len(transportadora_data) > 0 else 0
            score_emissoes_transporte = transportadora_data[1] if len(transportadora_data) > 1 else 0
        else:
            score_combustivel = 0
            score_emissoes_transporte = 0

        dados_resumo.append({
            'produto': produto,
            'localizacao': localizacao,
            'score_agua': score_agua,
            'score_eletricidade': score_eletricidade,
            'score_combustiveis_fornecedor': score_combustiveis,
            'score_desperdicio': score_desperdicio,
            'score_contaminacao': score_contaminacao,
            'score_emissoes': score_emissoes,
            'score_combustiveis_transportadora': score_combustivel,
            'score_emissoes_transportadora': score_emissoes_transporte
        })

    return render_template('resumo_impactos.html', dados_resumo=dados_resumo)


@app.route('/historico')
def historico():

    caminho_arquivo = './historico_de_escolhas.txt'
    
    try:
        with open(caminho_arquivo, "r") as arquivo:
            escolhas = arquivo.readlines()
    except FileNotFoundError:
        escolhas = []
    
    return render_template('historico.html', escolhas=escolhas)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")




