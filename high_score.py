class GameEntry:
    
    def __init__(self,name,score):
        self._name = name
        self._score= score
    def get_name(self):
        return self._name
    def get_score(self):
        return self._score
    
    def __str__(self):
        return "({0},{1})".format(self._name,self._score)
    

marc = GameEntry("Marcus",56);
print(marc.__str__())


