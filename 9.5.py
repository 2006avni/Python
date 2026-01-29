from heapq import nlargest 
dict={1:234,2:100,3:255,4:243,5:895} 
print("original dict==",dict) 
largestno=nlargest(3,dict,key=dict.get) 
print("Largest values==",largestno)
