import json
global items
with open('items.txt') as outfile:
    items=json.load( outfile)
items=items['data']
def checkey(key ,dic):
    if key in dic :
        return True
    else:
        return False

def isenditem(item):
    if(item.into==None):
        if(item.inStore):
            if(item.consumable==False):
                if( "Lane" not in item.tags or "GoldPer" in item.tags):
                    return True 

    return False

class Item:  
    def __init__(self,item_id):
        self.item_id=item_id
        self.mythic= "Mythic" in items[item_id]['description']
        self.name=items[item_id]['name']
        self.tags=items[item_id]['tags']
        self.cost=items[item_id]['gold']['total']
        self.stats=items[item_id]['stats']
        if(checkey('into',items[item_id])):
            self.into=items[item_id]['into']
        else:
            self.into=None
        if(checkey('consumed',items[item_id])):
            self.consumable=items[item_id]['consumed']

        else:
            self.consumable=False 
        if(checkey('inStore',items[item_id])):
            self.inStore=items[item_id]['inStore']

        else:
            self.inStore=True
            
    def __str__(self):
        return "id :{0}, name : {1} ,tags : {2},cost : {3},stats: {4}".format(self.item_id,self.name,self.tags,self.cost,self.stats)
        
    
