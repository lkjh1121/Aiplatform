import seaborn as sns 
import matplotlib.pyplot as plt 
from sklearn.datasets import load_iris
import pandas as pd 

iris = load_iris() 

df1 = pd.DataFrame(iris["data"], columns=iris["feature_names"])
print( df1.head() )
df1["species"] = iris["target"]

print( df1.head() )
sns.set_theme()
sns.pairplot(df1, hue="species")
plt.show()
print( sns.get_dataset_names() ) #시본에서 제공하는 데이터 셋
iris = sns.load_dataset("penguins")
sns.pairplot(data=df1, hue="species", palette='dark')
 # pastel, bright, deep, muted, colorblind, dark
plt.show()

