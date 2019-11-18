class _Constant_:
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise Exception("can not set value to variable.")
        self.__dict__[name] = value

    def __delattr__(self, name):
        if name in self.__dict__:
            raise Exception('can not delete variable')

Illuminant = _Constant_()
Illuminant.a = [1.09850, 1.0000, 0.35585]
Illuminant.b = [0.99072, 1.0000, 0.85223]
Illuminant.c = [0.98074, 1.0000, 1.18232]
Illuminant.e = [1.0000, 1.0000, 1.0000]
Illuminant.d50 = [0.96422, 1.0000, 0.82521]
Illuminant.d55 = [0.95682, 1.0000, 0.92149]
Illuminant.d65 = [0.95047, 1.0000, 1.08883]
Illuminant.d76 = [0.94972, 1.0000, 1.22638]
Illuminant.icc = [0.9642, 1.0000, 0.8249] #[31595, 32768, 27030]/32768
Illuminant.f2  = [0.99186, 1.0000, 0.67393]
Illuminant.f7  = [0.95041, 1.0000, 1.08747]
Illuminant.f11 = [1.00962, 1.0000, 0.64350]
    
CIE_L = _Constant_()
CIE_L.e = 0.008856
CIE_L.k = 903.3