from constant import Illuminant
import color

print(color.xyz2lab([1, 1, 1], Illuminant.d65))
#color.xyY2XYZ([1,1,1])