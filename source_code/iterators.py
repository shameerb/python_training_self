class Deck(object):
    cards=[]
    def __init__(self,card=[]):
        self.cards=card
    def __iter__(self):
        return iter(self.cards)


n=Deck([1,2,3])
print dir(n)

