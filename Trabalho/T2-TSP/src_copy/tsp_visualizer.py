# *****************************************************************************
# * Grupo:
# * Alunos integrantes:
# *
# * Descrição:  Implementa um cliente interativo que constrói um ciclo (Tour)
# * usando a heurística do vizinho mais próximo.
# ****************************************************************************

import sys
from algs4 import in_python, stddraw, stdout
from src_copy.point import Point
from src_copy.tour import Tour

def main():
    xscale_default = 512
    yscale_default = 512

    stddraw.set_xscale(0, xscale_default)
    stddraw.set_yscale(-70, yscale_default)
    
    stddraw.enable_double_buffering()
    
    nearest = Tour()
    points = []
    
    showing_nearest = True
    mouse_correct = True
    mouse_was_up = True
    redraw = True

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
        redraw = True
    else:
        stdout.println(f"{xscale_default} {yscale_default}")

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
            
            stddraw.set_pen_color(stddraw.BLACK)
            # stddraw.text(100, -10, f"número de pontos: {len(points)}")
            stddraw.set_pen_color(stddraw.RED)
            # stddraw.text(100, -35, f"vizinho mais próximo: {nearest.length():.2f}")
            
            stddraw.show()
            stddraw.pause(50)
            
    sys.exit(0)

if __name__ == '__main__':
    main()
