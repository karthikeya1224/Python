class person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def get_name(self):
        return self.__name,self.__age
p=person("john",30)
print(p.get_name())