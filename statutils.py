import pandas as pd
import numpy as np
import random

# function to flip a fair coin
def flipfaircoin():
  x = int(random.uniform(0.,0.9999)*2)
  return x # 1=heads, 0=tails

def experiment():
# create dataframe with 1000 rows (coins), 10 cols (tosses):
  df = pd.DataFrame(np.random.randint(0,2,size=(1000, 10)))
  df["hedz"]=df.sum(axis=1) # 1=heads, 0=tails
#  print(df.head())
# Select relevant coins (rows) as as per Q1 in HW 2:
  c1st = df.iloc[[0]] #                         1st coin
  crnd = df.sample() #                          randomly selected coin
  cmin = df[df.hedz==df.hedz.min()].iloc[[0]] # 1st coin with fewest heads
#   print(c1st)
#   print(cmin)
#   print(crnd)
  nu1st=c1st["hedz"].loc[c1st.index[0]]/10.
  numin=cmin["hedz"].loc[cmin.index[0]]/10.
  nurnd=crnd["hedz"].loc[crnd.index[0]]/10.
  return nu1st, numin, nurnd