# 📊 Projeto de Grafos em Python

## 👨‍💻 Integrantes

* Enzo
* Arthur Silva Torres

---

## 📌 Descrição do Projeto

Este projeto implementa diversas operações e algoritmos clássicos sobre **grafos direcionados**, utilizando **listas de adjacência** em Python.

O programa lê um grafo a partir de um arquivo (`grafo.txt`) e oferece um menu interativo com várias funcionalidades para análise estrutural e exploração do grafo.

---

## 📂 Estrutura do Código

O código está organizado em funções, cada uma responsável por uma operação específica:

### 🔹 `leitor_arquivo(nome)`

* Lê um arquivo texto contendo:

  * Número de vértices (`n`)
  * Número de arestas (`m`)
  * Lista de arestas
* Retorna um objeto da classe `Grafo`.

---

### 🔹 `Menu()`

* Exibe as opções disponíveis para o usuário.

---

### 🔹 `InfoGeral(g)`

* Mostra informações gerais do grafo:

  * Número de vértices e arestas
  * Grau de entrada (mínimo, máximo e médio)
  * Grau de saída (mínimo, máximo e médio)

---

### 🔹 `GrauVertice(g)`

* Permite consultar:

  * Grau de entrada
  * Grau de saída
    de um vértice específico.

---

### 🔹 `BFS(g, vI)`

* Implementa a **Busca em Largura (Breadth-First Search)**.
* Calcula a distância mínima do vértice inicial até os demais.
* Retorna a lista de vértices visitados.

---

### 🔹 `DFS(g)`

* Implementa a **Busca em Profundidade (Depth-First Search)**.
* Percorre o grafo recursivamente.

---

### 🔹 `Conectividade_Fraca(g)`

* Verifica se o grafo é **fracamente conexo**.
* Considera tanto arestas diretas quanto inversas.

---

### 🔹 `existe_caminho(g, origem, destino)`

* Verifica se existe caminho entre dois vértices usando DFS.

---

### 🔹 `alcancabilidade(g)`

* Verifica:

  * Se um vértice alcança outro
  * E o caminho inverso

---

### 🔹 `Fontes_e_Sumidouros(g)`

* Identifica:

  * **Fontes**: vértices com grau de entrada 0
  * **Sumidouros**: vértices com grau de saída 0

---

### 🔹 `Fecho_Transitivo(g)`

* Calcula o **fecho transitivo direto** de um vértice:

  * Todos os vértices alcançáveis a partir dele

⚠️ Observação: Há um pequeno erro na variável `val` que deve ser corrigido para `v` ou outro nome consistente.

---

### 🔹 `Main()`

* Função principal que:

  * Carrega o grafo
  * Exibe o menu
  * Executa as operações escolhidas pelo usuário

---

## 📄 Formato do Arquivo `grafo.txt`

O arquivo deve seguir o formato:

```
n m
v1 w1
v2 w2
...
```

Exemplo:

```
5 4
0 1
1 2
2 3
3 4
```

---

## ▶️ Como Executar

1. Certifique-se de ter o arquivo `grafo.txt` no mesmo diretório.
2. Execute o script Python:

   ```
   python nome_do_arquivo.py
   ```
3. Escolha uma opção no menu.

---

## 🧠 Conceitos Aplicados

* Grafos direcionados
* Lista de adjacência
* Busca em largura (BFS)
* Busca em profundidade (DFS)
* Conectividade
* Alcance entre vértices
* Fecho transitivo

---

## ⚠️ Possíveis Melhorias

* Correção do bug no fecho transitivo
* Interface gráfica (GUI)
* Suporte a grafos ponderados
* Otimização da verificação de conectividade

---

## 📌 Conclusão

Este projeto é uma implementação prática de algoritmos fundamentais de grafos, sendo útil para estudos acadêmicos e compreensão de estruturas de dados e algoritmos clássicos.

---
