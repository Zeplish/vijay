
import pandas as pd
from pathlib import Path
import joblib
from .features import IL13_Features
import numpy as np
import os , sys

def Model_pred(fastafile,threshold):
    
    Fasta_Seq,ID,test_full_features = IL13_Features(fastafile)
    
    Result = []
    for index,row in test_full_features.iterrows():
        row = pd.DataFrame(row)
        row_T = row.transpose()
        row_T = np.array(row_T)
        model_file = joblib.load(os.path.join(sys.path[0], "app", "XGB_model.sav"))
        probability = model_file.predict_proba(row_T)
        probability  = np.round(probability,2)
        if probability[0][1] >= threshold:
            Result.append([ID[index],Fasta_Seq[index],"IL-13 inducing peptide",probability[0][1]])
        else:
            Result.append([ID[index],Fasta_Seq[index],"IL-13 non-inducing peptide",probability[0][1]])
    return Result
