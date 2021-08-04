'''
this file should include any algorithm that can make a opponent of the player
'''
import pandas as pd
import csv
import Graphics
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn.metrics import roc_auc_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor

GAME_INDEX=0

def init():
    with open("History.csv","w") as csvfile:
        writer = csv.writer(csvfile)
        list1=["index0","index1","r","round","player","player_RP_before","player_RP_after","ship","x","y","function","target_x","target_y","special","weapon","armour"]
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
            #print(line)
            if len(line)>0:
                if str(line[0])!="index0" :
                    index0=line[0]
                    index1=line[1]
                else:
                    index0=0
                    index1=0
    return int(index0)+1,int(index1)+1

def get_index0():
    d=pd.read_csv("History.csv",usecols=["index0"])
    return len(d)+1


def writerow(index1,r,round,player,player_RP_before,player_RP_after,ship,x,y,function,target_x,target_y,special,weapon,armour,lists):
    index0=get_index0()
    '''
    with open("History.csv","w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows ([[index,round,player,player_RP_before,player_RP_after,ship,weapon,armour,x,y,function,target_type,target_weapon,target_armour,target_x,target_y,special]])
    '''
    '''
    list3=[index0,index1,r,round,player,player_RP_before,player_RP_after,ship,x,y,function,target_x,target_y,special,weapon,armour]
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

    '''

def load_data():
    dataframe=pd.read_csv("History.csv")
    #dataframe.drop(['index0'],axis = 1, inplace = True)
    #dataframe.drop(['index1'],axis = 1, inplace = True)
    columns = dataframe.columns.tolist()
    k=0
    for list in columns:
        if len(list)<2:
            print(list)
            print(k)
            print(dataframe.iloc[:,k:k+1].values)
        k=k+1


    feature_array = dataframe.iloc[:,7:16].values
    label_array1=dataframe.iloc[:,2:7]
    label_array2=dataframe.iloc[:,16:29591]
    label_array=pd.concat([label_array1,label_array2],axis=1,ignore_index=True).values

    
    return train_test_split(dataframe, label_array, test_size=0.1, random_state=5)

def test_bayes(*data):
    # 导入X、Y的训练集和测试集数据
    X_train, X_test, y_train, y_test = data
    
    clf = naive_bayes.GaussianNB()
    clf = DecisionTreeRegressor(criterion="mse", max_depth=5)
    clf.fit(X_train, y_train)
    print("bayes:training score:{:.4f}".format(clf.score(X_train, y_train)))
    print("bayes:testing score:{:.4f}".format(clf.score(X_test, y_test)))
    # ????
    bayes_train_pre = clf.predict_proba(X_train)[:,1]
    bayes_test_pre = clf.predict_proba(X_test)[:,1]
   
    auc_train = roc_auc_score(y_train,bayes_train_pre)
    auc_test = roc_auc_score(y_test,bayes_test_pre)
    print("auc_train:", auc_train)
    print("auc_test:",auc_test)
