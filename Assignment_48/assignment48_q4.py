import numpy as np
from scipy.spatial.distance import  euclidean
from sklearn.preprocessing import StandardScaler



def StandardS():
    Data = np.array([
        [25,20000],
        [30,40000],
        [35,80000]
    ])

    pt1 = Data[0]
    pt2 = Data[1]

    distance_before = euclidean(pt1,pt2)

    scaler = StandardScaler()

    Scale_data = scaler.fit_transform(Data)

    scaled_pt1 = Scale_data[0]
    scaled_pt2 = Scale_data[1]

    distance_after = euclidean(scaled_pt1,scaled_pt2)

    print("Distance before scaling :",distance_before)

    print("Distance after scaling :",distance_after)






def main():
    StandardS()
    
    

if __name__ =="__main__":
    main()