def load_and_process(url_or_path):
    df = (
        pd.read_csv(url_or_path)
        .rename(columns={'Unnamed: 0':'student_id', 'failures.x':'failures', 'activities.x':'activities', 'romantic.x':'romantic_relationship','Walc.x':'Weekend_alcohol','Dalc.x':'Weekday_alcohol', 'famrel.x':'family_relationship','freetime.x':'freetime','goout.x':'socialising','absences.x':'absence'})
    )
    df2 = (
        df.assign(math_avg = lambda x :df['G1.x']+df['G2.x']+df['G3.x'])
        .assign(por_avg = lambda x :df['G1.y']+df['G2.y']+df['G3.y'])
        .drop(['G1.x','G2.x','G3.x','G1.y','G2.y','G3.y'],axis=1)
    )

    return df2