import pandas as pd
import os
data = {
    'Name':["Alice","Bob","Charlie"],
    'Age':[20,30,35],
    'City':["NYC","LA",'DC']
}

df = pd.DataFrame(data)
new_rec = {'Name':'Milly','Age':21,'City':'California'}
df.loc[len(df.index)] = new_rec
# data_dir = "data"
os.makedirs("data",exist_ok=True)
file_path = os.path.join("data",'Sample_data.csv')

df.to_csv(file_path,index=False)

print(f"the file is saved at {file_path}")
