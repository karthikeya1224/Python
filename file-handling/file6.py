import pickle
data={"name":"john","age":30,"city":"noida"}
with open('data.pkl',"wb") as file:
    pickle.dump(data, file)