# *****************************************************************************
# * Grupo:
# * Alunos integrantes:
# *
# * Descrição:  Implementa um cliente interativo que constrói um ciclo (Tour)
# * usando a heurística do vizinho mais próximo.
# ****************************************************************************

import sys
from algs4 import in_python, stddraw, stdout
from src.point import Point
from src.tour import Tour

def main():
    xscale = 512
    yscale = 512

    stddraw.set_xscale(0, xscale)
    stddraw.set_yscale(-70, yscale - 70)
    stddraw.enable_double_buffering()
    
    nearest = Tour()
    points = []
    
    showing_nearest = True
    mouse_correct = True
    mouse_was_up = True
    redraw = True

    try:
        # inicializa a estrutura de dados com pontos do arquivo
        if len(sys.argv) > 1:
            filename = sys.argv[1]
            inn = in_python.In(filename)
            xscale = inn.read_int()
            yscale = inn.read_int()

            stddraw.set_xscale(0, xscale)
            stddraw.set_yscale(-70, yscale)
            
            stdout.println(f"{xscale} {yscale}")

            while not inn.is_empty():
                x = inn.read_double()
                y = inn.read_double()
                stdout.println(f"{x} {y}")
                p = Point(x, y)
                points.append(p)
                nearest.insert_nearest(p)
        else:
            stdout.println(f"{xscale} {yscale}")

        # LOOP PRINCIPAL DE EVENTOS
        while True:
            if stddraw.has_next_key_typed():
                key = stddraw.next_key_typed()
                if key == 'n': showing_nearest = not showing_nearest
                if key == 'm': mouse_correct = not mouse_correct
                if key == 'q': break
                redraw = True
            
            if stddraw.is_mouse_pressed() and (not mouse_correct or mouse_was_up):
                mouse_was_up = False
                x, y = stddraw.mouse_x(), stddraw.mouse_y()
                
                # Para evitar adicionar pontos fora da área visível principal
                if y < 0: continue

                p = Point(x, y)
                points.append(p)
                nearest.insert_nearest(p)

                stdout.println(f"{x} {y}")
                redraw = True
            else:
                mouse_was_up = not stddraw.is_mouse_pressed()

            if redraw:
                redraw = False
                stddraw.clear()

                if showing_nearest:
                    stddraw.set_pen_radius(0.004)
                    stddraw.set_pen_color(stddraw.RED)
                    nearest.draw()

                stddraw.set_pen_color(stddraw.BLACK)
                stddraw.set_pen_radius(0.005)
                for p in points:
                    p.draw()
                
                # stddraw.text() não suporta alinhamento, então não incluímos
                # as legendas para não quebrar o visual.
                
                stddraw.show()
                stddraw.pause(50)
    
    except NotImplementedError as e:
        print(f"Execução interrompida pois uma função em Tour não foi implementada: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        sys.exit(0)

if __name__ == '__main__':
    main()
