


class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


r1 = Resistor(50e3)
print(r1.ohms)
r1.ohms = 10e3
print(r1.ohms)        

class VoltageResistor(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage
    
    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage/self.ohms


r2 = VoltageResistor(1e3)
print('Before: %5r amps' % r2.current)
r2.voltage = 10
print('After: %5r amps' % r2.current)
r2.current = 2
print(r2.current)
print(r2.voltage)
r2.voltage = 20
print(r2.current)




class BoundedResistance(Resistor):
    # def __init__(self, ohms):
    #     super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError('%f ohms must be > 0' % ohms)
        self._ohms = ohms
    
r3 = BoundedResistance(1e3)
# r3.ohms = 0
# BoundedResistance(-5)

r3.ohms = 2
print(r3.ohms)
print(r3._ohms)
print(r3.current)
print(r3.voltage)
print('r3 has attribute ohm?:', hasattr(r3, 'ohms'))


class BoundedResistance2(object):
    def __init__(self, ohms):
        self._ohms = ohms

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError('%f ohms must be > 0' % ohms)
        self._ohms = ohms
    
r32 = BoundedResistance2(2e3)
print(r32.ohms)
print(r32._ohms)
print('r32 has attribute ohm?:', hasattr(r32, 'ohms'))


class FixedResistance(Resistor):
    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Can't set attribute")
        self._ohms = ohms
        
r4 = FixedResistance(1e3)
# r4.ohms = 2e3
print(r4.ohms)
print(r4._ohms)


# class PrimaryKey:
#     def __get__(*args, **kwargs):
#         pass

#     def __set__(*args, **kwargs):
#         if hasattr(self, '_id'):
#             raise AttributeError("Can't set the id!")
#         self._id = id  


#from https://uwpce-pythoncert.github.io/Py300/metaclasses.html

class Dummy:
    pass

obj = Dummy()
print(vars(obj))  

setattr(obj, 'this', 54)
print(vars(obj))  
print(getattr(obj, 'this'))

print(Dummy.__dict__)
print(obj.__dict__)





class Meta(type):
    def __new__(meta, name, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value, Field):
                value.name = key
                value.internal_name = '_' + key
                
        cls = type.__new__(meta, name, bases, class_dict)
        return cls        


class Field:
    def __init__(self):
        self.name = None
        self.internal_name = None


class DatabaseRow(object, metaclass=Meta):
    pass


class Snippet(DatabaseRow):
    title = Field()
    desc = Field()
    vote = Field()

    def __repr__(self):
        return "<Snippet: %s>" % self.__dict__


sn = Snippet()
sn.title = 'Programming for everyone'
sn.desc = 'Everyone should learn Programming!'
sn.vote = 3

print(repr(sn), sn.__dict__)   
print(type(sn.vote)) 


class Field:
    def __init__(self, primary=False):
        self.name = None
        self.internal_name = None
        self.primary = primary



    # def __set__(self, instance, value):
    #     if self.primary_key:        
    #         raise AttributeError("Can't set the primary key!")
    #     self.__dict__[self.internal_name] = value



#https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python
#everything is an object
# >>> def foo(): pass
# >>> foo.__class__
# <type 'function'>
# >>> foo.__class__.__class__
# <type 'type'>