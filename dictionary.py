#dictionary in python is one of the data type which is use to key value pair map

# Dictionary is denoted by the curly brackets <<<<<<<<<{ dictionary }>>>>>>>>>>>>
from turtle import update


d2 = {  "harry" : "burger" , "Gaurav" : " Roti " , "Vaibhav " : "Rise",
"shubham": { "B": "Maggie" , "L": "Roti", "d":"Pongal"}
}
d2["Akshay"] = "Pushpa" # iska matlb rhenga ki d2 mai add kr do akshay ko 
d2["490"] = "Manchurian"
del d2["490"] # for the deleting the value pairs 
#print(d2["shubham"]["B"]) #pale woh d2 ko fetch krenga then shubham mai ke "B" ko..
# print(d2)



# **get () function is used to geting the value of the key

# print(d2.get("harry"))
# print(d2.keys())
# print(d2.items())
d2 : update({"leena" : " soffe"})
print(d2)







