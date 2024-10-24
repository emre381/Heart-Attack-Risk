import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

#  veriyi yükle 
df = pd.read_csv('heart.csv')
# print(df.describe())
# histogram oluşturma 
df.hist(figsize=(18,12),bins=20,edgecolor='black')
plt.suptitle('Veri Dağılımı')
# plt.show()

plt.figure(figsize=(10,6))
sns.scatterplot(data=df,x='Age',
                y='Cholesterol',hue='HeartDisease')
plt.title('Yaş ve Kolesterol Arasındaki İlişki')
# plt.show()
label_encoder=LabelEncoder()
df['Sex'] = label_encoder.fit_transform(df['Sex'])
df['ChestPainType'] = label_encoder.fit_transform(df['ChestPainType']) 
df['RestingECG'] = label_encoder.fit_transform(df['RestingECG'])
df['ExerciseAngina'] = label_encoder.fit_transform(df[ 'ExerciseAngina']) 
df['ST_Slope'] = label_encoder.fit_transform(df['ST_Slope'])

plt.figure(figsize=(12,8))
sns.heatmap(df.corr(),annot=True,cmap='coolwarm',fmt='.2f')
plt.title('korelasyon ısı haritası')
# plt.show()

plt.figure(figsize=(6,6))
sns.countplot(data=df,x='HeartDisease')
plt.title('Klap Hastalığına Yakalanma Oranları')
plt.show()
