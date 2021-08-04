'''
this file should include any algorithm that can make a opponent of the player
'''
import pandas as pd
import csv
import Graphics
from sklearn.preprocessing import StandardScaler



GAME_INDEX=0

def init():
    with open("History.csv","w") as csvfile:
        writer = csv.writer(csvfile)
        list1=["index0","index1","round","player","player_RP_before","player_RP_after","ship","x","y","function","target_x","target_y","special","weapon","armour"]
        for i in range(65):
            for j in range(65):
                val=str(i)+"/"+str(j)+"/s"
                list1.append(val)
        for i in range(65):
            for j in range(65):
                val=str(i)+"/"+str(j)+"/p"
                list1.append(val)
        for i in range(65):
            for j in range(65):
                val=str(i)+"/"+str(j)+"/h"
                list1.append(val)
        for i in range(65):
            for j in range(65):
                val=str(i)+"/"+str(j)+"/d"
                list1.append(val)
        for i in range(65):
            for j in range(65):
                val=str(i)+"/"+str(j)+"/r"
                list1.append(val)
        for i in range(65):
            for j in range(65):
                val=str(i)+"/"+str(j)+"/w"
                list1.append(val)
        for i in range(65):
            for j in range(65):
                val=str(i)+"/"+str(j)+"/a"
                list1.append(val)

        writer.writerow (list1)
        '''
        index stands for the game played
        ship: 1 for torpedo 2 for destroyer 3 for cruiser 4 for carrier 5 for eship 6 for base
        x,y:initial x y 0,0 if deploy
        weapon,armour(1 for hard,2 for energy)
        target: 0 for move 1 for attack 2 for deploy
        next 3: the same, 0 for nothing
        if deploy, should be 0,0 to targetx,targety (use function deploy)
        special:move function, 1 to activate(targetx,targety should remain the same)
        '''

def get_index():
    with open("History.csv","r") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            print(line)
            if len(line)>0:
                if str(line[0])!="index0" :
                    index0=line[0]
                    index1=line[1]
                else:
                    index0=0
                    index1=0
    return int(index0)+1,int(index1)+1


def writerow(index1,round,player,player_RP_before,player_RP_after,ship,x,y,function,target_x,target_y,special,weapon,armour,lists):
    index0,n=get_index()
    '''
    with open("History.csv","w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows ([[index,round,player,player_RP_before,player_RP_after,ship,weapon,armour,x,y,function,target_type,target_weapon,target_armour,target_x,target_y,special]])
    '''

    list3=[index0,index1,round,player,player_RP_before,player_RP_after,ship,x,y,function,target_x,target_y,special,weapon,armour]
    for row in lists[0]:
        for item in row:
            list3.append(item)
    for row in lists[1]:
        for item in row:
            list3.append(item)
    for row in lists[2]:
        for item in row:
            list3.append(item)
    for row in lists[3]:
        for item in row:
            list3.append(item)
    for row in lists[4]:
        for item in row:
            list3.append(item)
    for row in lists[5]:
        for item in row:
            list3.append(item)
    for row in lists[6]:
        for item in row:
            list3.append(item)

    file=pd.read_csv("History.csv")
    file.loc[index0]=list3
    file.to_csv("History.csv",index=None)

def preprocess():
    dataframe=pd.read_csv("History.csv")
    array = dataframe.values
    X=array[6:14]
    Y=array[2:5,15:]
    scaler=StandardScaler().fit(X)
    rescaledX=scaler.transform(X)

    numpy.set_printoptions(precision=3)
    print(rescaledX[0:5,:])