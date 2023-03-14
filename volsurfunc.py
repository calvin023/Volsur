import math


def sur_circle(vRadius):
    if not isinstance(vRadius, (int, float)):
        raise TypeError("Radius must be a number")
    elif vRadius <= 0:
        raise ValueError("Radius must be positive")
    else:
        vDiameter = 2 * vRadius
        vArea = math.pi * (vDiameter/2)**2
        vArea = round(vArea, 2)
        return vArea


def sur_triangle(vSide1, vSide2, vAngle):
    if not all(isinstance(x, (int, float)) for x in [vSide1, vSide2, vAngle]):
        raise TypeError("All sides and angles must be numbers")
    elif any(x <= 0 for x in [vSide1, vSide2, vAngle]):
        raise ValueError("All sides and angles must be positive")
    else:
        vAngle = math.radians(vAngle)
        vArea = 0.5 * vSide1 * vSide2 * math.sin(vAngle)
        vArea = round(vArea, 2)
        return vArea


def sur_square(vSide):
    if not isinstance(vSide, (int, float)):
        raise TypeError("Side length must be a number")
    elif vSide <= 0:
        raise ValueError("Side length must be positive")
    else:
        vArea = vSide**2
        vArea = round(vArea, 2)
        return vArea


def vol_sphere(vCirc):
    if not isinstance(vCirc, (int, float)):
        raise TypeError("Circumference must be a number")
    elif vCirc <= 0:
        raise ValueError("Circumference must be positive")
    else:
        vRadius = vCirc / (2 * math.pi)
        vVolume = (4/3) * math.pi * vRadius ** 3
        vVolume = round(vVolume, 2)
        return vVolume


def vol_ellipsoid(vHeight, vLength, vWidth):
    if not all(isinstance(x, (int, float)) for x in [vHeight, vLength, vWidth]):
        raise TypeError("All inputs must be numbers")
    elif any(x <= 0 for x in [vHeight, vLength, vWidth]):
        raise ValueError("All numbers must be positive")
    else:
        vVolume = (4/3) * math.pi * vHeight * vLength * vWidth
        vVolume = round(vVolume, 2)
        return vVolume


def vol_sqr_pyramid(vLength, vWidth, vHeigth):
    if not all(isinstance(x, (int, float)) for x in [vLength, vWidth, vHeigth]):
        raise TypeError("All inputs must be numbers")
    elif any(x <= 0 for x in [vLength, vWidth, vHeigth]):
        raise ValueError("All numbers must be positive")
    else:
        vVolume = (vLength * vWidth * vHeigth) / 3
        vVolume = round(vVolume, 2)
        return vVolume


def vol_tri_pyramid(vSide1, vSide2, vAngle, vHeight):
    if not all(isinstance(x, (int, float)) for x in [vSide1, vSide2, vAngle, vHeight]):
        raise TypeError("All inputs must be numbers")
    elif any(x <= 0 for x in [vSide1, vSide2, vAngle, vHeight]):
        raise ValueError("All numbers must be positive")
    else:
        vArea = sur_triangle(vSide1, vSide2, vAngle)
        vVolume = 1/3 * vArea * vHeight
        vVolume = round(vVolume, 2)
        return vVolume


def vol_cube(vEdge):
    if not isinstance(vEdge, (int, float)):
        raise TypeError("Edge must be a number")
    elif vEdge <= 0:
        raise ValueError("Edge must be positive")
    else:
        vVolume = vEdge ** 3
        vVolume = round(vVolume, 2)
        return vVolume

def vol_cone(vRadius, vHeight):
    if not all(isinstance(x, (int, float)) for x in [vRadius, vHeight]):
        raise TypeError("All inputs must be numbers")
    elif any(x <= 0 for x in [vRadius, vHeight]):
        raise ValueError("All numbers must be positive")
    else:
        vVolume = (1/3) * math.pi * vRadius**2 * vHeight
        vVolume = round(vVolume, 2)
        return vVolume
    
def vol_cylinder(vRadius, vHeight):
    if not all(isinstance(x, (int, float)) for x in [vRadius, vHeight]):
        raise TypeError("All inputs must be numbers")
    elif any(x <= 0 for x in [vRadius, vHeight]):
        raise ValueError("All numbers must be positive")
    else:
        vVolume = math.pi * vRadius**2 * vHeight
        vVolume = round(vVolume, 2)
        return vVolume