actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]

tp = tn = fp = fn = 0

for i,j in zip(actual,predicted):
    if i == 1 and j == 1:
        tp += 1
    elif i == 0 and j == 0:
        tn +=1
    elif i == 0 and j == 1:
        fp +=1
    elif i == 1 and j == 0:
        fn +=1

print("True Positive",tp)

print("True Negative",tn)

print("TFalse Positive",fp)

print("False Negative",fn)