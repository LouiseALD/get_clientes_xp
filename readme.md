<h1>Puxando Clientes XP do HTML para CSV </h1> 

<p align="center">
  <img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
</p>

> Status do Script: :warning: Em aprimoramento

### Tópicos 

:small_blue_diamond: [Descrição do projeto](#descrição-do-projeto)

:small_blue_diamond: [Funcionalidades](#funcionalidades)

:small_blue_diamond: [Pré-requisitos](#pré-requisitos)

:small_blue_diamond: [Como rodar a aplicação](#como-rodar-a-aplicação-arrow_forward)

... 

Insira os tópicos do README em links para facilitar a navegação do leitor

## Descrição do projeto 

<p align="justify">
  Esse projeto tem o intúito de coletar os dados disponíveis do HTML do XP HUB

  Obs: antecessor, será necessário realizar scraping dos dados, ou baixar o html da página
  Obs2: será necessário uma lista dos códigos dos acessores, inserir em 'lista_cod_acessores'
</p>

## Funcionalidades

:heavy_check_mark: Acessa a página do HTML 

:heavy_check_mark: Puxa as informações do HTML

:heavy_check_mark: Muda o nome das colunas

:heavy_check_mark: Salva as informações em CSV



## Pré-requisitos

:warning: [Python](https://nodejs.org/en/download/)
:warning: [Pandas](https://nodejs.org/en/download/)


## Como rodar a aplicação :arrow_forward:

No terminal, clone o projeto: 

```
git clone https://github.com/LouiseALD/get_clientes_xp
```

... 

## Casos de Uso

Para conseguir realizar, é necessário o codigo do acessor além dos HTMLS da página.

## JSON :floppy_disk:

### Ordem de dados gerados no CSV: 

... 
|Nome da Origem	|Nome do Cliente	|Numero Conta	|Telefone	|Patrimonio XP	|Saldo em conta	|Codigo Proprietario da Conta|	Aplicacoes financeiras	|Rua de Correspondencia	|CEP Correspondencia	|Email	|Celular	|CNPJ	| Acessor responsavel	|receitabovespa
... 


## Iniciando/Configurando banco de dados

Se for necessário configurar algo antes de iniciar o banco de dados insira os comandos a serem executados 

## Linguagens, dependencias e libs utilizadas :books:

- [Python](https://github.com/python)
- [Pandas](https://github.com/pandas-dev)


## Resolvendo Problemas :exclamation:

Em [issues]() Pequeno bug: Ao ler todos os itens da lista, o código se encerra apresentando um erro

## Tarefas em aberto

:memo: Tarefa 1 - Necessário desenvolver um scraping a parte para coletar os dados, ou salvar o HTML da página 

## Passo a passo após coletar os CSVs

Abrir Excel
Criar qualquer projeto em branco
Acesse a aba 'Dados'
Obter Dados ( Icone de um BD com Raio e CSV)
De arquivo
Da pasta
Selecione a pasta onde estão os csvs
De 'Ok'
Combinar
Combinar e carregar
Dê 'Ok' novamente
E ta pronto o sorvetinho  :)

Obs: Caso aconteça algum erro é devido a incompatibilidade de determinados campos nos arquivos, exemplo: um csv possui campos A, B, C e o outro A, B, D, C



## Desenvolvedores/Contribuintes :octocat:

Time responsável pelo desenvolvimento do projeto

| [<sub>Louise Aldrighi</sub>](https://github.com/LouiseALD) 

## Licença 

The [MIT License]() (MIT)

Copyright :copyright: 2022 - Automação de dados clientes XP

Créditos de templante README : https://gist.github.com/reginadiana/
