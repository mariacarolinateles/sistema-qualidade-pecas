# Sistema de Controle de Qualidade de Peças

## 1. Sobre o projeto

Este projeto foi desenvolvido como parte do desafio de automação digital, com o objetivo de criar um sistema em Python para auxiliar no controle de qualidade e armazenamento de peças em um ambiente industrial.

O sistema permite cadastrar peças, verificar se elas atendem aos padrões de qualidade, registrar peças aprovadas e reprovadas, armazenar as peças aprovadas em caixas e gerar um relatório final da produção.

A aplicação funciona por meio de um menu interativo no terminal, permitindo que o usuário escolha a operação que deseja realizar.

---

## 2. Objetivo

O principal objetivo do sistema é simular uma etapa de controle de qualidade de uma linha de produção.

Para cada peça cadastrada, o sistema recebe:

- ID da peça;
- Peso em gramas;
- Cor;
- Comprimento em centímetros.

Após o cadastro, o sistema verifica automaticamente se a peça atende aos critérios estabelecidos.

As peças aprovadas são encaminhadas para o armazenamento em caixas, enquanto as peças reprovadas são registradas juntamente com os motivos da reprovação.

---

## 3. Regras de qualidade

Para que uma peça seja aprovada, ela precisa atender aos três critérios de qualidade.

### Peso

O peso deve estar entre 95 g e 105 g.

```text
95 g ≤ peso ≤ 105 g
```

### Cor

As cores permitidas são:

- Azul;
- Verde.

Outras cores são consideradas fora do padrão e fazem com que a peça seja reprovada.

### Comprimento

O comprimento deve estar entre 10 cm e 20 cm.

```text
10 cm ≤ comprimento ≤ 20 cm
```

A peça só é considerada aprovada quando atende simultaneamente aos três critérios.

---

## 4. Funcionamento do sistema

O sistema apresenta um menu principal com as seguintes opções:

```text
1 - Cadastrar nova peça
2 - Listar peças aprovadas/reprovadas
3 - Remover peça cadastrada
4 - Listar caixas fechadas
5 - Gerar relatório final
0 - Sair
```

### 4.1 Cadastrar nova peça

A opção de cadastro solicita:

- ID da peça;
- Peso da peça;
- Cor da peça;
- Comprimento da peça.

O sistema realiza as validações automaticamente.

Também existe uma verificação para impedir que duas peças tenham o mesmo ID.

Caso o usuário digite um valor não numérico no campo de peso ou comprimento, o sistema solicita novamente um valor numérico válido.

No campo de cor, caso seja digitado um valor numérico, o sistema informa que a entrada é inválida e solicita novamente uma cor.

Uma cor diferente de azul ou verde, como vermelho, é aceita como entrada, mas faz com que a peça seja reprovada pelo critério de qualidade.

---

## 5. Classificação das peças

Após verificar os critérios, o sistema classifica a peça.

### Peça aprovada

Quando todos os critérios são atendidos:

```text
Peso: APROVADO
Cor: APROVADA
Comprimento: APROVADO

STATUS: PEÇA APROVADA
```

A peça é adicionada à lista de peças aprovadas e também à caixa que está sendo preenchida.

### Peça reprovada

Quando um ou mais critérios não são atendidos:

```text
STATUS: PEÇA REPROVADA
```

O sistema registra os motivos da reprovação.

Por exemplo:

```text
ID: 004
- Peso fora do padrão
- Cor não permitida
- Comprimento fora do padrão
```

Uma mesma peça pode apresentar mais de um motivo de reprovação.

---

## 6. Armazenamento em caixas

As peças aprovadas são armazenadas em caixas.

Cada caixa pode conter no máximo 10 peças.

Quando uma caixa chega a 10 peças, ela é automaticamente fechada e uma nova caixa começa a ser utilizada.

Exemplo:

```text
CAIXA 1
Quantidade de peças: 10
```

Após o fechamento da primeira caixa, as próximas peças aprovadas começam a ser armazenadas em uma nova caixa.

A caixa que ainda não atingiu 10 peças é considerada a caixa atual.

---

## 7. Listagem de peças

A opção:

```text
2 - Listar peças aprovadas/reprovadas
```

apresenta separadamente as peças aprovadas e reprovadas.

Para as peças aprovadas, são exibidos:

- ID;
- Peso;
- Cor;
- Comprimento.

Para as peças reprovadas, além dessas informações, são exibidos os motivos da reprovação.

---

## 8. Remoção de peças

A opção:

```text
3 - Remover peça cadastrada
```

permite remover uma peça informando seu ID.

O sistema verifica se a peça existe.

Caso a peça esteja na caixa que ainda está sendo preenchida, ela pode ser removida.

Caso a peça já esteja em uma caixa fechada, sua remoção não é permitida.

Isso evita alterações em caixas que já foram finalizadas.

---

## 9. Listagem de caixas

A opção:

```text
4 - Listar caixas fechadas
```

apresenta as caixas que já atingiram sua capacidade máxima.

Para cada caixa são exibidos:

- Número da caixa;
- Quantidade de peças;
- ID de cada peça;
- Peso;
- Cor;
- Comprimento.

Exemplo:

```text
CAIXA 1
Quantidade de peças: 10

ID: 001 | Peso: 100.0 g | Cor: azul | Comprimento: 15.0 cm
ID: 002 | Peso: 98.0 g | Cor: azul | Comprimento: 15.0 cm
...
```

---

## 10. Relatório final

A opção:

```text
5 - Gerar relatório final
```

apresenta um resumo da produção.

O relatório informa:

- Total de peças aprovadas;
- Total de peças reprovadas;
- Motivos das reprovações;
- Quantidade de caixas utilizadas;
- Quantidade de peças na caixa atual.

Exemplo:

```text
========================================
          RELATÓRIO FINAL
========================================

TOTAL DE PEÇAS APROVADAS: 11
TOTAL DE PEÇAS REPROVADAS: 4

PEÇAS REPROVADAS E MOTIVOS:

ID: 009
- Peso fora do padrão
- Comprimento fora do padrão

ID: 011
- Peso fora do padrão

ID: 013
- Cor não permitida

ID: 015
- Peso fora do padrão

QUANTIDADE DE CAIXAS UTILIZADAS: 2
PEÇAS NA CAIXA ATUAL: 1
```

---

## 11. Estrutura do código

O sistema foi desenvolvido utilizando funções para organizar as diferentes responsabilidades da aplicação.

Principais funções:

```text
id_ja_cadastrado()
```

Verifica se o ID informado já foi utilizado.

```text
listar_pecas()
```

Exibe as peças aprovadas e reprovadas.

```text
listar_caixas()
```

Exibe as caixas fechadas e suas peças.

```text
remover_peca()
```

Permite remover uma peça cadastrada, respeitando as regras do sistema.

```text
gerar_relatorio()
```

Gera o relatório final da produção.

```text
ler_numero()
```

Valida entradas numéricas de peso e comprimento.

```text
cadastrar_peca()
```

Realiza o cadastro e a avaliação da peça.

---

## 12. Estruturas utilizadas

O projeto utiliza diferentes estruturas da linguagem Python.

### Listas

São utilizadas para armazenar:

- Peças aprovadas;
- Peças reprovadas;
- Caixas fechadas;
- Peças da caixa atual;
- Motivos de reprovação.

Exemplo:

```python
pecas_aprovadas = []
pecas_reprovadas = []
caixas_fechadas = []
caixa_atual = []
```

### Dicionários

Cada peça é armazenada como um dicionário contendo seus dados.

Exemplo:

```python
peca = {
    "id": id_peca,
    "peso": peso,
    "cor": cor,
    "comprimento": comprimento,
    "motivos": motivos
}
```

### Estruturas condicionais

São utilizadas estruturas `if`, `elif` e `else` para tomar decisões.

Exemplo:

```python
if 95 <= peso <= 105:
    print("Peso: APROVADO")
else:
    print("Peso: REPROVADO")
```

### Estruturas de repetição

O sistema utiliza `while` e `for`.

O `while` mantém o menu funcionando até que o usuário escolha sair.

Os `for` são utilizados para percorrer peças, caixas e motivos de reprovação.

---

## 13. Tecnologias utilizadas

- Python 3
- Visual Studio Code
- Git
- GitHub

O projeto foi desenvolvido utilizando apenas recursos básicos da linguagem Python, sem necessidade de bibliotecas externas.

---

## 14. Como executar o projeto

### Pré-requisitos

É necessário ter o Python instalado no computador.

Também é recomendado utilizar um editor de código, como o Visual Studio Code.

### Executando o sistema

Abra a pasta do projeto no Visual Studio Code.

Abra o terminal integrado e execute:

```bash
python main.py
```

Caso o comando `python` não funcione no Windows, também pode ser utilizado:

```bash
py main.py
```

Após executar, o sistema apresentará o menu principal.

---

## 15. Exemplo de utilização

Ao iniciar o programa:

```text
========================================
   SISTEMA DE CONTROLE DE QUALIDADE
========================================

1 - Cadastrar nova peça
2 - Listar peças aprovadas/reprovadas
3 - Remover peça cadastrada
4 - Listar caixas fechadas
5 - Gerar relatório final
0 - Sair
```

O usuário pode escolher a opção 1 para cadastrar uma peça.

Exemplo:

```text
Digite o ID da peça: 001
Digite o peso da peça (g): 100
Digite a cor da peça: azul
Digite o comprimento da peça (cm): 15
```

Resultado:

```text
Peso: APROVADO
Cor: APROVADA
Comprimento: APROVADO

STATUS: PEÇA APROVADA
```

Outro exemplo:

```text
Digite o ID da peça: 002
Digite o peso da peça (g): 110
Digite a cor da peça: vermelho
Digite o comprimento da peça (cm): 25
```

Resultado:

```text
Peso: REPROVADO
Cor: REPROVADA
Comprimento: REPROVADO

STATUS: PEÇA REPROVADA

Motivos:
- Peso fora do padrão
- Cor não permitida
- Comprimento fora do padrão
```

---

## 16. Tratamento de entradas inválidas

O sistema possui mecanismos para evitar erros durante a utilização.

### Entrada numérica inválida

Caso o usuário digite:

```text
Digite o peso da peça (g): abc
```

o sistema informa:

```text
Digite um valor numérico válido.
```

e solicita novamente o valor.

### Entrada inadequada no campo de cor

Caso o usuário digite:

```text
Digite a cor da peça: 100
```

o sistema informa:

```text
Cor inválida. Digite uma cor.
```

e solicita novamente a cor.

Por outro lado, uma cor como `vermelho` é aceita como entrada, mas a peça será reprovada porque apenas azul e verde atendem ao padrão de qualidade.

---

## 17. Organização do projeto

A estrutura básica do projeto é:

```text
sistema-qualidade-pecas/
│
├── main.py
│
└── README.md
```

O arquivo `main.py` contém todo o código-fonte do sistema.

O arquivo `README.md` contém a documentação e as instruções para utilização do projeto.

---

## 18. Possíveis melhorias futuras

O sistema desenvolvido é uma simulação de um processo de automação industrial. Em uma aplicação real, seria possível ampliar suas funcionalidades.

Algumas possibilidades são:

- Utilização de sensores para coletar automaticamente peso, cor e comprimento;
- Integração com equipamentos industriais;
- Utilização de banco de dados para armazenar as informações;
- Geração automática de relatórios;
- Interface gráfica;
- Integração com sistemas de produção;
- Utilização de inteligência artificial para identificação de padrões e possíveis falhas;
- Monitoramento da produção em tempo real.

Essas melhorias poderiam transformar o protótipo desenvolvido em uma solução mais próxima de um sistema industrial real.

---

## 19. Conclusão

O projeto demonstra como conceitos básicos de programação podem ser utilizados para representar um processo de automação industrial.

Por meio de estruturas condicionais, funções, listas, dicionários e estruturas de repetição, foi possível desenvolver um sistema capaz de cadastrar peças, avaliar critérios de qualidade, identificar reprovações, armazenar peças aprovadas em caixas e gerar informações sobre a produção.

A automação desse tipo de processo pode contribuir para aumentar a organização, padronização e eficiência das atividades industriais, além de reduzir erros causados por processos manuais.

O projeto também permite visualizar como um sistema simples pode servir como base para futuras integrações com sensores, equipamentos industriais, bancos de dados e outras tecnologias.

---

## 20. Autoria

Projeto desenvolvido para atividade acadêmica de Algoritmos e Lógica de Programação.

Desenvolvido em Python.
