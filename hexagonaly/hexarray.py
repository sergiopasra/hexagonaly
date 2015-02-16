
# Coordinates
# See here for details http://www.redblobgames.com/grids/hexagons/
#

def cube_to_axial(x,y,z):
    q = x
    r = z
    return r, q

def axial_to_cube(r, q):
    x = q
    z = r
    y = -x - z
    return x, y, z

def cube_to_evenq(x, y, z):
    q = x
    r = z + (x + (x & 1)) / 2
    return r, q

def cube_to_oddq(x, y, z):
    q = x
    r = z + (x - (x & 1)) / 2
    return r, q

def cube_to_evenr(x, y, z):
    q = x + (z + (z & 1)) / 2
    r = z
    return r, q

def cube_to_oddr(x, y, z):
    q = x + (z - (z & 1)) / 2
    r = z
    return r, q

def evenq_to_cube(r, q):
    x = q
    z = r - (q + (q & 1)) / 2
    y = -x-z
    return x, y, z

def oddq_to_cube(r, q):
    x = q
    z = r - (q - (q & 1)) / 2
    y = -x-z
    return x, y, z

def evenr_to_cube(r, q):
    x = q - (r + (r&1)) / 2
    z = r
    y = -x-z
    return x, y, z

def oddr_to_cube(r, q):
    x = q - (r - (r&1)) / 2
    z = r 
    y = -x-z
    return x, y, z


class HexArray(object):
    pass
