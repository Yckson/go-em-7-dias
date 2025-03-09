import os

# Lista com os detalhes de cada dia do roadmap
dias = [
    {
        "folder": "Dia_1_Fundamentos",
        "title": "Fundamentos de Go",
        "description": (
            "Aprenda a sintaxe e os conceitos básicos da linguagem Go, como variáveis, controle de fluxo e funções, "
            "comparando com sua experiência em C e JavaScript."
        ),
        "project": (
            "Neste projeto, você implementará um algoritmo que verifica se um número é primo e imprime todos os números "
            "primos até um valor N, fornecido pelo usuário. Essa atividade reforça o uso de loops, condicionais e funções, "
            "fundamentais para dominar a lógica da linguagem Go."
        )
    },
    {
        "folder": "Dia_2_Estruturas_Ponteiros",
        "title": "Estruturas e Ponteiros",
        "description": (
            "Explore arrays, slices, maps, structs e o uso de ponteiros em Go, entendendo a diferença entre valores e referências."
        ),
        "project": (
            "Neste projeto, você desenvolverá um gerenciador de contatos. Crie uma struct para representar um contato (nome, telefone, email) "
            "e utilize um map para armazenar os contatos. Implemente funcionalidades para adicionar, remover e listar contatos, "
            "praticando o uso de ponteiros e o gerenciamento de dados complexos."
        )
    },
    {
        "folder": "Dia_3_Concorrencia",
        "title": "Concorrência com Goroutines",
        "description": (
            "Aprenda a implementar concorrência utilizando goroutines e canais (channels) para executar tarefas em paralelo de forma segura."
        ),
        "project": (
            "Neste projeto, você criará um programa que realiza múltiplas requisições HTTP simultaneamente. Utilize goroutines para disparar as requisições "
            "e canais para coletar os tempos de resposta de cada uma. Esse exercício é essencial para entender a gestão da concorrência em Go."
        )
    },
    {
        "folder": "Dia_4_Interfaces_OOP",
        "title": "Interfaces e Programação Orientada a Objetos",
        "description": (
            "Compreenda o uso de interfaces em Go para alcançar polimorfismo e criar designs desacoplados, explorando a abordagem não orientada a classes da linguagem."
        ),
        "project": (
            "Neste projeto, implemente um sistema de pagamento utilizando interfaces. Crie uma interface que defina um método de pagamento e implemente "
            "diferentes métodos (Pix, Boleto, Cartão). Utilize type assertions para tratar casos específicos e explore os conceitos de polimorfismo em Go."
        )
    },
    {
        "folder": "Dia_5_Arquivos_BD",
        "title": "Manipulação de Arquivos e Banco de Dados",
        "description": (
            "Aprenda a ler e escrever arquivos, manipular JSON e conectar-se a bancos de dados usando Gorm e SQLite."
        ),
        "project": (
            "Neste projeto, você construirá um CRUD (Create, Read, Update, Delete) para gerenciamento de tarefas. Utilize o SQLite como banco de dados e o Gorm "
            "para gerenciar as operações. O projeto envolve a leitura/escrita de arquivos e a manipulação de dados em JSON, proporcionando uma visão completa de como "
            "integrar armazenamento de dados em suas aplicações Go."
        )
    },
    {
        "folder": "Dia_6_WebAPI_Gin",
        "title": "APIs REST com Gin",
        "description": (
            "Desenvolva uma API RESTful utilizando o framework Gin, trabalhando com rotas, middlewares e autenticação via JWT."
        ),
        "project": (
            "Neste projeto, crie uma API REST para cadastro e autenticação de usuários. Implemente endpoints para registro, login e recuperação de informações, "
            "utilizando JWT para autenticação. Essa atividade oferece experiência prática com desenvolvimento web em Go e a integração de segurança em APIs."
        )
    },
    {
        "folder": "Dia_7_Projeto_Final",
        "title": "Projeto Final - Sistema de Fila de Atendimento",
        "description": (
            "Consolide todo o conhecimento adquirido durante a semana criando um sistema real que simula uma fila de atendimento utilizando goroutines e canais."
        ),
        "project": (
            "No projeto final, você desenvolverá um sistema de fila de atendimento. O sistema deverá simular o processamento paralelo de tarefas, "
            "usando goroutines e canais para gerenciar a fila de requisições. Este projeto integrará os conceitos de concorrência, organização de código e "
            "melhores práticas em Go, resultando em uma aplicação robusta e eficiente."
        )
    }
]

# Pasta raiz onde a estrutura será criada
root = "GoRoadmap"

# Cria a pasta raiz, se não existir
if not os.path.exists(root):
    os.mkdir(root)

# Para cada dia, cria a subpasta, o README.md e um arquivo base main.go
for dia in dias:
    path = os.path.join(root, dia["folder"])
    os.makedirs(path, exist_ok=True)

    # Conteúdo detalhado do README.md
    readme_content = f"""# {dia['title']}

## Descrição
{dia['description']}

## Projeto do Dia
{dia['project']}

## Como Começar
1. Abra o arquivo `main.go` para iniciar o desenvolvimento.
2. Execute o programa com o comando `go run main.go`.
3. Explore diferentes soluções para implementar o desafio proposto.

Boa codificação e bons estudos!
"""

    # Cria o arquivo README.md
    readme_path = os.path.join(path, "README.md")
    with open(readme_path, "w", encoding="utf-8") as file:
        file.write(readme_content)

    # Arquivo base main.go
    main_go_content = """package main

import "fmt"

func main() {
    fmt.Println("Hello, Go!")
}
"""
    main_go_path = os.path.join(path, "main.go")
    with open(main_go_path, "w", encoding="utf-8") as file:
        file.write(main_go_content)

    print(f"Diretório criado: {path}")

print("\nEstrutura de pastas e arquivos criada com sucesso!")
