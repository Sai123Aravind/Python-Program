import csv
# with open("mca1.csv","w",newline='') as csvfile:
#     fieldnames=["id","name","mobile","email"]
#     data=csv.DictWriter(csvfile,fieldnames)
#     data.writeheader()
   
#     rows=[
#         {'id':1,'name':'lokesh kanagaraj','mobile':9078190235,'email':"djdgjded@gamil"},
#         {'name':'Leo','id':2,'email':'lokesh@gmail','mobile': 8390279347}
#     ]
#     data.writerows(rows)
with open("mca1.csv",'r') as csvfile:
    data=csv.DictReader(csvfile)
    for var in data:
        print(var)