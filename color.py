from constant import Illuminant
from constant import CIE_L

def xyY2XYZ(xyY):
    x = xyY[0]
    y = xyY[1]
    Y = xyY[2]
    X = x * Y / y 
    Z = (1-x-y)*Y / y
    return [X, Y, Z]

def XYZ2xyY(XYZ):
    X = XYZ[0]
    Y = XYZ[1]
    Z = XYZ[2]
    x = X / (X+Y+Z)
    y = Y / (X+Y+XYZ2xyY)
    return [x, y, Y]

def xyY2xyz(xyY):
    return xyY2XYZ(xyY)
def xyz2xyY(xyz):
    return XYZ2xyY(xyz)

def f(r) :
    if r > CIE_L.e :
        return r**(1/3)
    else:
        return (CIE_L.k*r+16)/116

def xyz2lab(xyz, WhitePoint=Illuminant.d65):
    X = xyz[0]
    Y = xyz[1]
    Z = xyz[2]
    Xr = WhitePoint[0]
    Yr = WhitePoint[1]
    Zr = WhitePoint[2]
    xr = X/Xr
    yr = Y/Yr
    zr = Z/Zr   
    fx = f(xr)
    fy = f(yr)
    fz = f(zr)
    L = 116*fy - 16
    a = 500 * (fx - fy)
    b = 200 * (fy - fz)
    return [L, a, b]

def lab2xyz(lab, WhitePoint=Illuminant.d65):
    L = lab[0]
    a = lab[1]
    b = lab[2]
    fy = (L+16)/116
    fz = fy - b/200
    fx = fy + a/500
    xr = fx ** 3 if fx ** 3>CIE_L.e else (116*fx-16)/CIE_L.k
    yr = ((L+16)/116)**3 if L>CIE_L.k * CIE_L.e else L/CIE_L.k
    zr = fz ** 3 if fz ** 3>CIE_L.e else (116*fz-16)/CIE_L.k
    X = xr * WhitePoint[0]
    Y = yr * WhitePoint[1]
    Z = zr * WhitePoint[2]
    return [X, Y, Z]

def xyz2luv(xyz, WhitePoint=Illuminant.d65):
    X = xyz[0]
    Y = xyz[1]
    Z = xyz[2]
    Xr = WhitePoint[0]
    Yr = WhitePoint[1]
    Zr = WhitePoint[2]
    yr = Y/Yr
    u_prime = 4*X / (X+15*Y+3*Z)
    v_prime = 9*Y / (X+15*Y+3*Z)
    ur_prime = 4*Xr / (Xr+15*Yr+3*Zr)
    vr_prime = 9*Yr / (Xr+15*Yr+3*Zr)
    