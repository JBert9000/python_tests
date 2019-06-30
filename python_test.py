#map() and lamba functions
numbers1=(1,2,3)
numbers2=(4,5,6)

funcs=[numbers1,numbers2]

result=map(lambda x,y: x+y,numbers1,numbers2)
print("lambda and map() function result: "+str(result))
