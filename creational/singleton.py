#Intent: lets you ensure that a class has only one instance, while providing a global access point to this instance 
#Code example:
class Singleton:
    #make the default constructor private
    __instance = None

    #static creation method that acts as a constructor; this method will call the private contructor (__init) to create an object and save it in a static field
    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance
    
    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("Singleton exists already!")
        else:
            Singleton.__instance = self

s1 = Singleton.getInstance()

s2 = Singleton.getInstance()

#checking if both s1 and s2 are the same object 
print(s1 is s2)
