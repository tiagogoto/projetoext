# Aplicação Web para gerenciar reuniões e Atas

## Introdução

um sistema para gerenciamento de atas das reuniões de forma que seja fácil a busca por palavras chaves como assuntos, protocolos, interessado entre outras informações. Para o desenvolvimento do projeto foram estabelecidos:

* Objetivo:
    * sistema para gerenciar a atas e informações indexáveis;
    * gerar atas automática a partir dos dados cadastrados

* Funções funcionais:
    * Cadastro de ATAs;
    * ferramenta para gerar a ata em pdf;
    * Ferramenta de pesquisa;
* Funções não-funcionais:
    * desenvolvimento utilizando stack de código livre;
    * utilização de banco de dados de código livre;
* Restrições:
    * deve possuir autenticação e controle de permissão;
    * deve possuir forma de realizar backup


## Utilização em docker


## Configurações iniciais

Configurações da senha e e-amil do administrador deve ser realizado no arquivo .env.admin, conforme o exemplo abaixo: 

``` ENV

ADMIN_EMAIL= "teste@teste.com.br"
USER_PASSWORD="123456789"

```

## Capturas de tela da aplicação

* Cadastro de usuário;

* Painel administrativo para configuração básica

![Captura de Tela](Doc/Figures/Painel_adm.png)

* Painel de cadastro de usuário 

![Captura de Tela](Doc/Figures/user_form.png)