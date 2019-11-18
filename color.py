from constant import WhitePoint

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

def xyz2lab(xyz, whitePoint=WhitePoint.d65):
    print('xyz2lab')

    