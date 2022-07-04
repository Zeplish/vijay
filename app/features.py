
import pandas as pd
from collections import Counter
import math
import numpy as np
import joblib
import os
import sys
############## BTC ####################3

def aacp_comp(df):
    std = list("H")
    AAC_Result = []
    #AAC_Result.append("AAC_H")
    zz = df.iloc[:,0]
    for j in zz:
        Result = []
        for i in std:
            count = 0
            for k in j:
                temp1 = k
                if temp1 == i:
                    count += 1
                composition = (count/len(j))*100
            Result.append(composition) 
        AAC_Result.append(Result)
        #print(AAC_Result)
    header = ["AAC_H"]   
    df_AAC= round(pd.DataFrame(AAC_Result,columns = header),3)
    return df_AAC
def bond(df) :
    tota = []
    hy = []
    Si = []
    Du = []
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    bb = pd.DataFrame()
    
    
    bonds=pd.read_csv(os.path.join(sys.path[0],"modal_csv", "bonds.csv"), sep = ",")
    for i in range(0,len(df)) :
        tot = 0
        h = 0
        S = 0
        D = 0
        tota.append([i])
        hy.append([i])
        Si.append([i])
        Du.append([i])
        for j in range(0,len(df[0][i])) :
            temp = df[0][i][j]
            for k in range(0,len(bonds)) :
                if bonds.iloc[:,0][k] == temp :
                    tot = tot + bonds.iloc[:,1][k]
                    h = h + bonds.iloc[:,2][k]
                    S = S + bonds.iloc[:,3][k]
                    D = D + bonds.iloc[:,4][k]
        tota[i].append(tot)
        hy[i].append(h)
        Si[i].append(S)
        Du[i].append(D)
    for m in range(0,len(df)) :
        b1.append(tota[m][1])
        b2.append(hy[m][1])
        b3.append(Si[m][1])
        b4.append(Du[m][1])

    bb["BTC_T"] = b1
    bb["BTC_H"] = b2
    bb["BTC_S"] = b3
    bb["BTC_D"] = b4
    
    bb1 = bb[["BTC_T","BTC_H","BTC_S"]]
    return bb1

################## SER ####################




def SE_residue_level(df):
    data = df[0].to_list()
    GH=[]
    for i in range(len(data)):
        my_list={'I':0,'L':0,'P':0,'T':0}
        seq=data[i]
        num, length = Counter(seq), len(seq)
        num=dict(sorted(num.items()))
        C=list(num.keys())
        F=list(num.values())
        for key, value in my_list.items():
             for j in range(len(C)):
                if key == C[j]:
                    my_list[key] = round(((F[j]/length)* math.log(F[j]/length, 2)),3)
        GH.append(list(my_list.values()))
    header_SER = ["SER_I","SER_L","SER_P","SER_T"] 
    df_SER = round(pd.DataFrame(GH,columns = header_SER),3)
    return df_SER

# df_SER = SE_residue_level(df)
# print(df_SER)


############### TPC #########################

def tpc_comp(df):
    std = ["L","R"]
    std1 = ["M","Q"]
    std2 = ["F","Q"]
    comb = ["LMQ","RQF"]
    header_list = []
    for i in comb:
        header_list.append(f"TPC_{i}")
    list_result = []
    zz = df.iloc[:,0]
    for i in range(0,len(zz)):
        list_2 = []
        for j in std:
            for k in std1:
                for m1 in std2:
                    count = 0
                    temp = j+k+m1
                    if temp in comb:
                        for m3 in range(0,len(zz[i])):
                            b = zz[i][m3:m3+3]
                            if b == temp:
                                count += 1
                            composition = (count/(len(zz[i])-2))*100
                        list_2.append("%.2f" %composition)
      
        list_result.append(list_2)
    TPC = round(pd.DataFrame(list_result,columns = header_list),3)
    return TPC


##################### CeTD ##################################



def ctd(df):
    attr=pd.read_csv(os.path.join(sys.path[0], "modal_csv", "aa_attr_group.csv"), sep="\t")
    n = 0
    stt1 = []
    m = 1
    for i in range(0,len(attr)) :
        st =[]
        stt1.append([])
        for j in range(0,len(df)) :
            stt1[i].append([])
            for k in range(0,len(df[0][j])) :
                while m < 4 :
                    while n < len(attr.iloc[i,m]) :
                        if df[0][j][k] == attr.iloc[i,m][n] :
                            st.append(m)
                            stt1[i][j].append(m)
                        n += 2
                    n = 0
                    m += 1
                m = 1

       
#####################Composition##################### 
    std = [1,2,3]
    result_CTD = []
    for p in range (0,len(df)) :
        result = []
        for ii in range(0,len(stt1)) :
            for pp in std :
                count = 0
                for kk in stt1[ii][p] :
                    temp1 = kk
                    if temp1 == pp :
                        count += 1
                    composition = (count/len(stt1[ii][p]))*100
                result.append("%.2f"%composition)      
        result_CTD.append(result)    
        df_Comp = pd.DataFrame(result_CTD)    
    header1 = ['CeTD_HB','CeTD_VW','CeTD_PO','CeTD_PZ','CeTD_CH','CeTD_SS','CeTD_SA']
    head = []
    for i in header1:
        for j in range(1,4):
            head.append(i+str(j))
    df_Comp.columns = head
   
################# Distribution ################    
    
    c_22 = []
    for x in range(0,len(stt1)) :
        c_22.append([])
        k = 0
        j = 0
        for y in range(0,len(stt1[x])):
            
            c_22[x].append([])
            for i in range(1,4) :
                cc = []
                c1 = [index for index,value in enumerate(stt1[x][y]) if value == i]
                c_22[x][y].append(c1)
    cc = []

    for ss in range(0,len(df)):
        for uu in range(0,len(c_22)):
            for mm in range(0,3):
                for ee in range(0,101,25):
                    k = (ee*(len(c_22[uu][ss][mm])))/100
                    cc.append(math.floor(k))
                    
    x = [cc[i:i+105] for i in range(0, len(cc), 105)] 
    df_Distribution = pd.DataFrame(x)
    
    head3 = []
    header3 = ['CeTD_0_p','CeTD_25_p','CeTD_50_p','CeTD_75_p','CeTD_100_p']
    header4 = ['HB','VW','PO','PZ','CH','SS','SA']
    for j in range(1,4):
        for k in header4:
            for i in header3:
                head3.append(i+'_'+k+str(j))
     
    #print(len(head3))   
    df_Distribution.columns = head3     
    df_Comp_distribution = pd.concat([df_Comp,df_Distribution],axis = 1)
    
    return df_Comp_distribution[["CeTD_75_p_HB1","CeTD_SS1"]]


Desired_10_Features =["BTC_S","CeTD_SS1","TPC_RQF","SER_I","SER_L","SER_T","BTC_T","CeTD_75_p_HB1","AAC_H","SER_P"]

def IL13_Features(sequence):
    Fasta_df = [i[1].upper() for i in sequence ]
    Seq = [i[0] for i in sequence]
    df = pd.DataFrame(Fasta_df)
    df_AAC = aacp_comp(df)
    df_TPC = tpc_comp(df)
    df_BOND = bond(df)
    df_CTD = ctd(df)
    df_SER = SE_residue_level(df)
    df_result = pd.concat([df_AAC,df_TPC,df_BOND,df_CTD,df_SER],axis = 1)
    df_result_ordered  = df_result[Desired_10_Features]
    
    
    return Fasta_df,Seq,df_result_ordered