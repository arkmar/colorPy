class _Constant_:
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise Exception("can not set value to variable.")
        self.__dict__[name] = value

    def __delattr__(self, name):
        if name in self.__dict__:
            raise Exception('can not delete variable')

WhitePoint = _Constant_()
WhitePoint.a = [1.09850, 1.0000, 0.35585]
WhitePoint.b = [0.99072, 1.0000, 0.85223]
WhitePoint.c = [0.98074, 1.0000, 1.18232]
WhitePoint.e = [1.0000, 1.0000, 1.0000]
WhitePoint.d50 = [0.96422, 1.0000, 0.82521]
WhitePoint.d55 = [0.95682, 1.0000, 0.92149]
WhitePoint.d65 = [0.95047, 1.0000, 1.08883]
WhitePoint.d76 = [0.94972, 1.0000, 1.22638]
WhitePoint.icc = [0.9642, 1.0000, 0.8249] #[31595, 32768, 27030]/32768
WhitePoint.f2  = [0.99186, 1.0000, 0.67393]
WhitePoint.f7  = [0.95041, 1.0000, 1.08747]
WhitePoint.f11 = [1.00962, 1.0000, 0.64350]
    
