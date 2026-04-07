# -*- coding: utf-8 -*-

"""

Created on Tue Feb 14 18:42:48 2023

n = V
m = A

@author: icalc
"""
from grafoLista import Grafo 
from collections import deque


def leitor_arquivo(nome):
    try:
        with open(nome, 'r') as f:
            n, m = map(int, f.readline().strip().split())
            g = Grafo(n)

            for _ in range(m):
                v, w = map(int, f.readline().strip().split())
                g.insereA(v, w)
        return g
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None

def Menu():
    print("1. Informações Gerais do Grafo")
    print("2. Grau de um Vértice")
    print("3. Busca em Largura (BFS)")
    print("4. Busca em Profundidade (DFS)")
    print("5. Conectividade Fraca")
    print("6. Alcançabilidade")
    print("7. Fontes e Sumidouros")
    print("8. Fecho Transitivo")
    print("9. Sair")

def InfoGeral(g):
    print("Informações Gerais do Grafo:")
    print(f"Número de Vértices: {g.n}")
    print(f"Número de Arestas: {g.m}")

    print("\nGrau de saída:")
    print(f"Mínimo: {min(g.grauSaida)}")
    print(f"Máximo: {max(g.grauSaida)}")
    print(f"Médio: {sum(g.grauSaida)/g.n:.2f}")

    print("\nGrau de entrada:")
    print(f"Mínimo: {min(g.grauEntrada)}")
    print(f"Máximo: {max(g.grauEntrada)}")
    print(f"Médio: {sum(g.grauEntrada)/g.n:.2f}")

def GrauVertice(g):
    v = int(input("Digite o vértice: "))
   
    print(f"Grau de entrada do Vértice: {g.grauEntrada[v]}")
    print(f"Grau de saída do Vértice: {g.grauSaida[v]}")

def BFS(g, vI=None):
    if vI is None:
        vI = int(input("Digite o vértice inicial: "))

    visitado = [False] * g.n
    dist = [-1] * g.n

    fila = deque([vI])
    visitado[vI] = True
    dist[vI] = 0
    
    while fila:
        u = fila.popleft()
        print(f"Visitando vértice: {u} | Distância: {dist[u]}")

        for v in g.listaAdj[u]:
            if not visitado[v]:
                visitado[v] = True
                dist[v] = dist[u] + 1
                fila.append(v)
    return visitado # Retorna a lista de visitados para uso em outras funções

def DFS(g):
    vI = int(input("Digite o vértice inicial: "))
    visitado = [False] * g.n

    def dfs_visit(u):
        visitado[u] = True
        print(f"Visitando vértice: {u}")
        for v in g.listaAdj[u]:
            if not visitado[v]:
                dfs_visit(v)

    dfs_visit(vI)

def Conectividade_Fraca(g):
    visitado = [False] * g.n
    def dfs(u):
        visitado[u] = True
        # saída
        for v in g.listaAdj[u]:
            if not visitado[v]:
                dfs(v)
        # entrada (invertido)
        for i in range(g.n):
            if u in g.listaAdj[i]:
                if not visitado[i]:
                    dfs(i)
    dfs(0)
    if all(visitado):
        print("Grafo é FRACAMENTE conexo")
    else:
        print("Grafo NÃO é conexo")

def existe_caminho(g, origem, destino):
    visitado = [False] * g.n

    def dfs_rec(u):
        if u == destino:
            return True
        visitado[u] = True
        for v in g.listaAdj[u]:
            if not visitado[v]:
                if dfs_rec(v): 
                    return True
        return False

    return dfs_rec(origem)

def alcancabilidade(g):
    u = int(input("Vértice de origem: "))
    v = int(input("Vértice de destino: "))

    print(f"{u} -> {v}:", existe_caminho(g, u, v))
    print(f"{v} -> {u}:", existe_caminho(g, v, u)) 

def Fontes_e_Sumidouros(g):
    for i in range(g.n):
        if g.grauEntrada[i] == 0:
            print(f"Vértice {i} é uma fonte.")
        if g.grauSaida[i] == 0:
            print(f"Vértice {i} é um sumidouro.")

def Fecho_Transitivo(g):
    v = int(input("Vértice para calcular o fecho transitivo: "))
    # O fecho transitivo direto são todos os vértices alcançáveis a partir de v
    alcancaveis = BFS(g, v)
    fecho = [i for i, v in enumerate(alcancaveis) if v]
    print(f"Fecho Transitivo Direto do vértice {v}: {fecho}")

def Main():
    # Tenta carregar o grafo. Certifique-se que o arquivo existe.
    try:
        g = leitor_arquivo("grafo.txt")
    except Exception as e:
        print(f"Erro ao carregar o grafo: {e}")
        return

    while True:
        Menu()
        try:
            escolha = int(input("Escolha uma opção: "))
            print("")

            match escolha:
                case 1: InfoGeral(g)
                case 2: GrauVertice(g)
                case 3: BFS(g)
                case 4: DFS(g)
                case 5: Conectividade_Fraca(g)
                case 6: alcancabilidade(g)
                case 7: Fontes_e_Sumidouros(g)
                case 8: Fecho_Transitivo(g)
                case 9:
                    print("Encerrando o programa...")
                    break
                case _:
                    print("Opção inválida.")
                    
        except ValueError:
            print("Por favor, digite um número válido.")

if __name__ == "__main__":
    Main()