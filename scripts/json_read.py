import json
import os
for i in range(20000,30002):
    check = os.path.isfile('C:/Users/gyans/Desktop/New folder/New folder/New folder (3)/json/'+ str(i) +'.json')
    if(check==True):
        print(i,end='\n')
        f = open('C:/Users/gyans/Desktop/New folder/New folder/New folder (3)/json/'+ str(i) +'.json')
    # print(f.type())

        data = json.load(f)
        lengg=len(data['annotation'])
        data['path']=data['annotation']['filename']
        if(lengg>6):
            data['outputs']={'object':data['annotation']['object']}
        else:
            data['outputs']={'object':[]}
        data['time_labeled']=1677265309954
        data['labeled']=True
        data['size']=data['annotation']['size']
        del data['annotation']
        with open('C:/Users/gyans/Desktop/New folder/New folder/New folder (3)/json/'+ str(i) +'.json','w') as s:
            json.dump(data,s)
        f.close()



