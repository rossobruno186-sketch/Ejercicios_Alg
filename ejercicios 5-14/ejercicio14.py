def existe_paso(grafo, origen, destino):
    def __existe_paso(grafo, actual, destino):
        resultado = False
        pos_vertice = grafo.search(actual, 'value')
        
        if pos_vertice is not None:
            if not grafo[pos_vertice].visited:
                grafo[pos_vertice].visited = True # Marcamos como visitado
                
                if grafo[pos_vertice].value == destino:
                    return True
                else:
                    for arista in grafo[pos_vertice].edges:
                        pos_destino_arista = grafo.search(arista.destination, 'value')
                        if pos_destino_arista is not None and not grafo[pos_destino_arista].visited:
                            resultado = __existe_paso(grafo, grafo[pos_destino_arista].value, destino)
                            if resultado:
                                break
        return resultado

    for vertice in grafo:
        vertice.visited = False

    return __existe_paso(grafo, origen, destino)
