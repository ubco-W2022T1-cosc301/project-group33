import pandas as pd;

def load_and_process(url_or_path):
    df = (
        pd.read_csv(url_or_path)
        .rename(columns={'Unnamed: 0':'student_ic', 'failures.x':'failures', 'activities.x':'activities', 'romantic.x':'romantic_relationship','Walc.x':'Weekend_alcohol','Dalc.x':'Weekday_alcohol', 'famrel.x':'family_relationship','freetime.x':'freetime','goout.x':'socialising','absences.x':'absence'})    )
    df2 = (
        df
        .assign(math_avg = lambda x :(df['G1.x']+df['G2.x']+df['G3.x'])/3)
        .assign(por_avg = lambda x :(df['G1.y']+df['G2.y']+df['G3.y'])/3)
        .assign(alc_avg = lambda x : (df['Weekend_alcohol']+df['Weekday_alcohol'])/2)
    )
    
    df3 = (
        df2.drop(['sex','school','address','Medu','Fedu','Mjob','Fjob','reason','guardian.x','guardian.y','traveltime.x','traveltime.y','schoolsup.x','schoolsup.y','paid.x','paid.y','famsup.x','famsup.y','nursery','health.x','health.y','higher.x','higher.y','Dalc.y','Walc.y','famrel.y','freetime.y','absences.y','studytime.y','romantic.y','goout.y','failures.y','activities.y','studytime.x','G1.x','G1.y','G2.x','G2.y','G3.x','G3.y'],axis=1)
    )

    return df3