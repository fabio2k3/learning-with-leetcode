class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        # 1. Frecuencias necesarias de t
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        # 2. Ventana actual y contadores
        window = {}
        required = len(need)      # número de caracteres únicos en t
        formed = 0                # cuántos de esos ya cumplen la cantidad

        # 3. Lista de posiciones relevantes (simulamos cola con índice)
        positions = []            # guardamos posiciones donde s[i] in t
        head = 0                  # índice del primer elemento en la lista

        # 4. Mejor ventana encontrada
        best_len = float('inf')
        best_start = 0

        # 5. Recorremos s con puntero derecho (p2)
        p2 = 0
        while p2 < len(s):
            ch = s[p2]

            # Solo nos interesan los caracteres que están en t
            if ch in need:
                positions.append(p2)          # guardamos la posición
                window[ch] = window.get(ch, 0) + 1

                # Si con esta adición alcanzamos la cantidad necesaria
                if window[ch] == need[ch]:
                    formed += 1

                # 6. Mientras la ventana sea válida, intentamos reducirla
                while formed == required and head < len(positions):
                    # El extremo izquierdo es la posición en positions[head]
                    left_pos = positions[head]
                    curr_len = p2 - left_pos + 1

                    # Actualizar el mínimo
                    if curr_len < best_len:
                        best_len = curr_len
                        best_start = left_pos

                    # 7. Quitamos el carácter de la izquierda de la ventana
                    left_ch = s[left_pos]
                    window[left_ch] -= 1
                    if window[left_ch] < need[left_ch]:
                        formed -= 1

                    # 8. Avanzamos el head para "eliminar" esa posición
                    head += 1

            p2 += 1

        # 9. Devolver el resultado
        if best_len == float('inf'):
            return ""
        else:
            return s[best_start:best_start + best_len]