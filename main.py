# from statutils import flipfaircoin
# for i in range(11):
#  print(flipfaircoin())

from statutils import experiment
nu = [0., 0., 0.]

numiters = 100000
for m in range(numiters+1):
  nu1st, numin, nurnd = experiment()
  to_add = [nu1st, numin, nurnd]
  nu = [item1 + item2 for item1, item2 in zip(nu, to_add)]
  print (str(m), end='\r') # display run number, overwriting as we go...

nu = [item/numiters for item in nu]
print(nu)