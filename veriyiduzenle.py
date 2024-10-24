import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler

#  veriyi yükle 
df = pd.read_csv('heart.csv')
# print(df)
# print(df.info())
# print(df.isnull().sum())
categorical_colmns=['ChestPainType','Sex','RestingBP','ExerciseAngina','ST_Slope']
# label ile bu sütunları sayısal verile çevirme 
le=LabelEncoder()
for colmn in categorical_colmns:
    df[colmn]=le.fit_transform(df[colmn])
 # kontrol edelim 
numeric_colmns = ['Age','RestingBP','Cholesterol','FastingBS','MaxHR','Oldpeak']
#  verileri standart hale getir
scaler = StandardScaler()
df[numeric_colmns]=scaler.fit_transform(df[numeric_colmns])
df.to_csv('heart_duzenlenmis.csv', index=False)