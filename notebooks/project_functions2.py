
import pandas as pd
import numpy as np




def load_and_process(csvpath):

    df = pd.read_csv(csvpath)

    dfrename = (   
        df
        .rename(columns={'G3':'Grade'})
    )
    dfdrop = (
        dfrename
        .drop(columns = ['school','sex', 'Unnamed: 0', 'Pstatus', 'famsup', 'age', 'guardian', 'address', 'famsize', 'famrel','Dalc', 'Walc', 'freetime', 'G1', 'G2','goout','Mjob', 'Fjob', 'reason', 'romantic', 'internet', 'higher', 'nursery', 'activities', 'paid', 'absences', 'health', 'traveltime','studytime', 'schoolsup'])
    )
    dfassign = (
        dfdrop
        .assign(Pedu=lambda x: (x['Medu']*1/2) + (x['Fedu']*1/2))
    )
    dfnull = (
        dfassign
        .loc[lambda x: x['Grade']>0]
  
    dfrest = (
        dfnull
        .dropna()
        .reset_index(drop=True)
    )
   
    return dfrest
