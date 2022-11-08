import pandas as pd
import numpy as np

def load_and_process(address):

    df = pd.read_csv(address)

    # Method Chain 1 
    df1 = (   
        df
        .rename(columns={"freetime": "ft"})
        .dropna()
    )
    # Method Chain 2 
    df2 = (
        df1
        .assign(color_filter=lambda x: 1)
        .loc[lambda x: x['absences']>5]


    )
    # Method Chain 3
    df3 = (
        df2
        .sort_values("absences", ascending=False)
        .reset_index(drop=True)

    )
    # Method Chain 4 
    df4 = (
        df3
        .loc[:, ["absences", "ft"]]


    )
    # Method Chain 5 
    df5 = (
        df4
        .rename(columns={"famsize": "fs"})
        .dropna()              
        
    )


    return df5