import os 
import pandas as pd 

path ="./경기기록"
fileList = os.listdir(path)
#print( fileList )

season =[
    {"syear":2018, "smonth":10, "eyear":2019, "emonth":7, "foldername":"18_19"},
    {"syear":2019, "smonth":10, "eyear":2020, "emonth":9, "foldername":"19_20"},
    {"syear":2020, "smonth":10, "eyear":2021, "emonth":8, "foldername":"20_21"},
    {"syear":2021, "smonth":10, "eyear":2022, "emonth":7, "foldername":"21_22"},
    {"syear":2022, "smonth":10, "eyear":2022, "emonth":7, "foldername":"22_23"}
]

def getFolderName(year, month):
    for s in season:
        #print ( s["syear"]==year and month >=s["smonth"]);
        if s["syear"]==year and month >=s["smonth"]  or  s["eyear"]==year and month <=s["emonth"]:
            return s["foldername"] 
    return ""


i=1
for filename in fileList:
    if filename[0:4].isnumeric()==False: 
        break 
  
    year = int(filename[0:4])
    month  = int(filename[5:7])
    #print ( year, month, getFolderName(year, month) )
    foldername = getFolderName(year, month)
    path2 = "./팀 소속 멤버 스텟/동부/"+foldername+ "/" + "Milwaukee Bucks"+ foldername + ".csv"

    df1 = pd.read_csv(path +"/" + filename)
    df2 = pd.read_csv(path2)

    # if i>=5 :
    #     break 
    # i = i+1 
    #@df3 = pd.merge(df1, df2, how="left", on="PLAYER_NAME")
    df2 = df2.iloc[:, 1:]

    df2.columns = ["PLAYER_NAME", "STATUS"]
    print( filename)

    df3 = pd.merge(df1, df2, how="left", on="PLAYER_NAME")
    df3.to_csv("./합산/"+filename, encoding="CP949", index=False)
    #print(df3)

