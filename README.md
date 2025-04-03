


# Módulo 6 - Projeto 1

 ## Introdução
O projeto tem como objetivo a construção de uma REST API para uma aplicação desenvolvida anteriormente, cuja finalidade era a gestão de encomendas para fornecer o Continente do Centro Comercial Colombo, tendo em conta o impacto ambiental que a produção e transporte dos seus produtos provocam. Os detalhes da aplicação inicial estão localizados em: https://github.com/ines2357/modulo5_projeto1.
Para este projeto, foi feito o deploy da aplicação pela App Service da Azure. 


## 1. Desenvolvimento da aplicação
- Foi mantida toda a estrutura da aplicação original, sendo acrescentadas novas APIs às diferentes rotas do ficheiro app.py, responsável por executar a aplicação. Estas APIs devolvem os dados em formato JSON. 
- Realizou-se, também, a integração com uma API específica que devolve a lista dos produtos disponíveis, interligando-se ao ficheiro consumidores.py, que gere a seleção dos produtos pelo utilizador. 

 ### 1.1. Teste das APIs
 Para testar as APIs, utilizou-se a extensão EchoAPI no VSCode, que funcionou como um Client REST.
 - api/produtos
  
 - api/escolha_produtos
 
- api/resumo_impactos

- api/historico


## 2. App Service

### 2.1 Clonar o Repositório
 O desenvolvimento da aplicação foi feito com recurso a um repositório git, que contém os ficheiros necessários para correr a aplicação python.
 
`git clone git@github.com:ines2357/modulo6_projeto1.git`

### 2.2 Criação do ambiente virtual

Os passos seguintes devem ser executados dentro do repositório clonado.
- 1º Passo: Criação do ambiente virtual

`python3 -m venv .venv`

`source .venv/bin/activate`

- 2º Passo: Instalação dos requisitos da aplicação

`pip install -r requirements.txt`

### 2.3 Deploy da aplicação através do App Service

`az webapp up --runtime PYTHON:3.12 --name <nome>`

### 2.4  Acesso à aplicação
Através da interface gráfica da Azure, nos Serviços Aplicacionais, procura-se pelo nome da aplicação. Para executar a aplicação, clica-se no link.

