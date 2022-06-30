
import pandas as pd
from pathlib import Path
import joblib
from .features import IL13_Features
import numpy as np
import os , sys

def Model_pred(fastafile,threshold):
    
    Fasta_Seq,ID,test_full_features = IL13_Features(fastafile)
    
    Result = []
    Result.append(["ID","Sequence","Classification","Probability"])
    for index,row in test_full_features.iterrows():
        row = pd.DataFrame(row)
        row_T = row.transpose()
        row_T = np.array(row_T)
        model_file = joblib.load(os.path.join(sys.path[0], "app", "XGB_model.sav"))
        probability = model_file.predict_proba(row_T)
        if probability[0][1] >= threshold:
            print(ID[index],Fasta_Seq[index],"Il13 inducing peptide",probability[0][1])
            Result.append([ID[index],Fasta_Seq[index],"Il13 inducing peptide",probability[0][1]])
        else:
            print(ID[index],Fasta_Seq[index],"Non Il13 inducing peptide",probability[0][1])
            Result.append([ID[index],Fasta_Seq[index],"Non Il13 inducing peptide",probability[0][1]])
    return Result
