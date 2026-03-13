import numpy as np
from sklearn.preprocessing import StandardScaler

def StandardS():
    Data = np.array([
        [25,20000],
        [30,40000],
        [35,80000]
    ])
    
    scaler = StandardScaler()
    Scale_data = scaler.fit_transform(Data)
    print("Scale data",Scale_data)



def main():
    StandardS()
    

if __name__ =="__main__":
    main()