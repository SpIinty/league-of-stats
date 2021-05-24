import json
global RUNES
with open('runesReforged.json') as outfile:
    RUNES=json.load( outfile)

class Rune:
    def __init__(self,identification):
        self.id=identification
        for i in RUNES:
            for j in i['slots']:
                for k in j['runes']:
                    if(k['id']==self.id):
                        self.name=k['name']
                        self.desc=k['shortDesc']
                        self.png=k['icon']
                    else:
                        pass
        splitedec=self.desc.split('<')
        fixedesc=''
        for i in range(len(splitedec)):
            try:
                fixedesc+=(splitedec[i].split('>')[1])
            except:
                fixedesc+=splitedec[i]
        self.desc=fixedesc
	
        
        
                            
    
        
runes=[]
for i in RUNES:
    for j in i['slots']:
        for k in j['runes']:
            runes.append(Rune(k['id']))
