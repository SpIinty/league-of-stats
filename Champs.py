import json
global champs
global champion_keys
with open('champs.txt',encoding="utf8") as outfile:
    champs=json.load( outfile)
champion_keys=champs['keys']
champs=champs['data']
#importent things from the json
#['partype']=abilty cost ,['tags'],(ad,def,ap=['info']) ,['enemytips'],['spells']
#['passive']|['name']|['description']
#spells[0-3] |['cooldown'] |['description'] |['name'] |


class Champion:
    
    def __init__(self,name):
        self.name=name
        my_champs=champs[name]
        self.key=my_champs['key']
        self.cost_type=my_champs['partype']
        self.ally_tips=my_champs['allytips']
        self.enemy_tips=my_champs['enemytips']
        self.tags=my_champs['tags']
        self.type=my_champs['info']['attack'],my_champs['info']['defense'],my_champs['info']['magic']
        self.passive={'name':my_champs['passive']['name'],'description':my_champs['passive']['description']}
        self.abilty1={'name':my_champs['spells'][0]['name'],'description':my_champs['spells'][0]['description'],'cooldown':my_champs['spells'][0]['cooldown']}
        self.abilty2={'name':my_champs['spells'][1]['name'],'description':my_champs['spells'][1]['description'],'cooldown':my_champs['spells'][1]['cooldown']}
        self.abilty3={'name':my_champs['spells'][2]['name'],'description':my_champs['spells'][2]['description'],'cooldown':my_champs['spells'][2]['cooldown']}
        self.abilty4={'name':my_champs['spells'][3]['name'],'description':my_champs['spells'][3]['description'],'cooldown':my_champs['spells'][3]['cooldown']}
        if(self.type[0]>self.type[1]):
            if(self.type[0]>self.type[2]):
                self.type='attack'
            else:
                self.type='magic'
        else:
            if(self.type[1]>self.type[2]):
                self.type='defense'
            else:
                self.type='magic'        
    
    
        
