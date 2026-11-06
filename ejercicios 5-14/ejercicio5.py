def eliminar_arista(self, vertice, destino):
        pos_vertice = self.search(vertice, 'value')
        if pos_vertice is None:
            return None
            
        resultado = self[pos_vertice].edges.delete_value(destino, 'destination')

        if not self.is_dir and resultado is not None:
            pos_destino = self.search(destino, 'value')
            if pos_destino is not None:
                self[pos_destino].edges.delete_value(vertice, 'destination')

        return resultado
