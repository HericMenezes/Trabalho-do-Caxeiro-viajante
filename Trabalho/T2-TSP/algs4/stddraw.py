import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as lines
import time
import numpy as np

# Drawing state variables
_window_title = "Standard Draw"
_canvas_width = 512
_canvas_height = 512
_xmin, _xmax = 0.0, 1.0
_ymin, _ymax = 0.0, 1.0
_pen_color = 'black'
_pen_radius = 0.002
_font_size = 16
_font_family = 'sans-serif'
_defer = False

# Matplotlib objects
_fig, _ax = None, None

# --- Interactivity State ---
_keys_typed = []
_is_mouse_pressed = False
_mouse_x, _mouse_y = 0.0, 0.0

# --- Event Handlers ---
def _on_key_press(event):
    _keys_typed.append(event.key)

def _on_mouse_press(event):
    global _is_mouse_pressed, _mouse_x, _mouse_y
    if event.inaxes == _ax:
        _is_mouse_pressed = True
        _mouse_x = event.xdata
        _mouse_y = event.ydata

def _on_mouse_release(event):
    global _is_mouse_pressed
    _is_mouse_pressed = False

def _on_mouse_move(event):
    global _mouse_x, _mouse_y
    if event.inaxes == _ax:
        _mouse_x = event.xdata
        _mouse_y = event.ydata

def _init_canvas():
    global _fig, _ax
    if _fig is None:
        _fig, _ax = plt.subplots()
        _ax.set_aspect('equal', adjustable='box')
        
        # Set window title based on latest call to setTitle
        _fig.canvas.manager.set_window_title(_window_title)
        
        # Invert y-axis to match StdDraw's origin at bottom-left
        _ax.invert_yaxis()
        
        # Hide axes
        _ax.xaxis.set_visible(False)
        _ax.yaxis.set_visible(False)
        _ax.spines['top'].set_visible(False)
        _ax.spines['right'].set_visible(False)
        _ax.spines['bottom'].set_visible(False)
        _ax.spines['left'].set_visible(False)

# --- Public API ---

def set_canvas_size(width=512, height=512):
    global _canvas_width, _canvas_height
    _canvas_width, _canvas_height = width, height
    if _fig: _fig.set_size_inches(width / _fig.get_dpi(), height / _fig.get_dpi())

def set_xscale(min_val=0.0, max_val=1.0):
    global _xmin, _xmax
    _xmin, _xmax = min_val, max_val
    if _ax: _ax.set_xlim(_xmin, _xmax)

def set_yscale(min_val=0.0, max_val=1.0):
    global _ymin, _ymax
    _ymin, _ymax = min_val, max_val
    if _ax: _ax.set_ylim(_ymin, _ymax)

def set_pen_color(color='black'):
    global _pen_color
    _pen_color = color

def set_pen_radius(radius=0.002):
    global _pen_radius
    _pen_radius = radius

def has_next_key_typed():
    return len(_keys_typed) > 0

def next_key_typed():
    return _keys_typed.pop(0)

def is_mouse_pressed():
    return _is_mouse_pressed

def mouse_x():
    return _mouse_x

def mouse_y():
    return _mouse_y
    
def clear(color='white'):
    _init_canvas()
    _ax.clear()
    _ax.set_facecolor(color)
    set_xscale(_xmin, _xmax)
    set_yscale(_ymin, _ymax)
    _ax.invert_yaxis()
    if not _defer: show()

def point(x, y):
    _init_canvas()
    marker_size = _pen_radius * 1000
    _ax.plot(x, y, marker='o', markersize=marker_size, color=_pen_color, linestyle='None')
    if not _defer: show()

def line(x0, y0, x1, y1):
    _init_canvas()
    linewidth = _pen_radius * 500
    l = lines.Line2D([x0, x1], [y0, y1], color=_pen_color, linewidth=linewidth)
    _ax.add_line(l)
    if not _defer: show()

def enable_double_buffering():
    global _defer
    _defer = True
    plt.ion()

def show():
    _init_canvas()
    _fig.canvas.draw()
    _fig.canvas.flush_events()

def pause(t):
    time.sleep(t / 1000.0)

def circle(x, y, radius):
    _init_canvas()
    linewidth = _pen_radius * 250
    circ = patches.Circle((x, y), radius, facecolor='none', edgecolor=_pen_color, linewidth=linewidth)
    _ax.add_patch(circ)
    if not _defer:
        show()

def filled_circle(x, y, radius):
    _init_canvas()
    circ = patches.Circle((x, y), radius, facecolor=_pen_color, edgecolor='none')
    _ax.add_patch(circ)
    if not _defer:
        show()
        
def rectangle(x, y, half_width, half_height):
    _init_canvas()
    linewidth = _pen_radius * 250
    rect = patches.Rectangle((x - half_width, y - half_height), 2 * half_width, 2 * half_height, 
                               facecolor='none', edgecolor=_pen_color, linewidth=linewidth)
    _ax.add_patch(rect)
    if not _defer:
        show()

def filled_rectangle(x, y, half_width, half_height):
    _init_canvas()
    rect = patches.Rectangle((x - half_width, y - half_height), 2 * half_width, 2 * half_height, 
                               facecolor=_pen_color, edgecolor='none')
    _ax.add_patch(rect)
    if not _defer:
        show()

def polygon(x_coords, y_coords):
    _init_canvas()
    linewidth = _pen_radius * 250
    poly = patches.Polygon(np.column_stack((x_coords, y_coords)), closed=True,
                             facecolor='none', edgecolor=_pen_color, linewidth=linewidth)
    _ax.add_patch(poly)
    if not _defer:
        show()

def filled_polygon(x_coords, y_coords):
    _init_canvas()
    poly = patches.Polygon(np.column_stack((x_coords, y_coords)), closed=True,
                             facecolor=_pen_color, edgecolor='none')
    _ax.add_patch(poly)
    if not _defer:
        show()

def text(x, y, s):
    _init_canvas()
    _ax.text(x, y, s,
             fontsize=_font_size,
             family=_font_family,
             ha='center', va='center',
             color=_pen_color)
    if not _defer:
        show()

def enable_double_buffering():
    global _defer
    _defer = True
    plt.ion()

def disable_double_buffering():
    global _defer
    _defer = False
    plt.ioff()

def show():
    _init_canvas()
    _fig.canvas.draw()
    _fig.canvas.flush_events()

def pause(t):
    time.sleep(t / 1000.0)

def save(filename):
    if _fig:
        _fig.savefig(filename)
