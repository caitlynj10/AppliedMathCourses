import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_location = 'Dengue_trends_math122a.xls'
sheet = pd.read_excel(file_location)
Ntotal = sheet.shape[0]
DengueData = []
Searches = []
Dates = []
for rownum in range(Ntotal):
    DengueData.append(sheet.values[rownum, 1])
    Searches.append(sheet.values[rownum, 2])
    Dates.append(sheet.values[rownum, 0])

Ntraining = 36
DengueTraining = DengueData[0:Ntraining]
SearchesTraining = Searches[0:Ntraining]

# Build A matrix here using training data
# with solution vector such that DengueData = coefs[0]+coefs[1]*Searches

###### your code goes here ######

A = np.column_stack((np.ones(Ntraining), SearchesTraining))

###############################

#solve least squares problem here with qr decomposition
Q, R = np.linalg.qr(A,mode = 'reduced')
coefs = np.linalg.solve(R,Q.T@np.array(DengueTraining))
print(coefs)

DenguePrediction = coefs[0]+coefs[1]*np.array(Searches)

#least squares fit
plt.scatter(Searches,DengueData,c='b',label='Data')
plt.plot(Searches,DenguePrediction,c='r',label='Fit')
plt.legend()
plt.show()

DengueTraining = DengueData[0:Ntraining]
SearchesTraining = Searches[0:Ntraining]
plt.plot(np.arange(0,Ntraining),DengueTraining,np.arange(0,Ntraining),DenguePrediction[0:Ntraining])
plt.title('Training')
plt.legend(['Training', 'Fit'])
plt.show()

DengueValidation = DengueData[Ntraining:]
SearchesValidation = Searches[Ntraining:]
plt.plot(np.arange(0,Ntotal-Ntraining),DengueValidation,np.arange(0,Ntotal-Ntraining),DenguePrediction[Ntraining:])
plt.title('Validation')
plt.legend(['Test','Prediction'])
plt.show()

plt.plot(np.arange(0,Ntotal),DengueData,np.arange(0,Ntotal),DenguePrediction);
plt.title('Full')
plt.legend(['Data','Fit+Prediction'])
plt.show()