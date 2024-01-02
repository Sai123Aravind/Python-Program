import csv
#with open('mca.csv','w',newline='') as csvfile:
#    data=csv.writer(csvfile)
#   data.writerow(['id','name','mobile','email'])
#    data2=[
#        [1,'john',719721721,'jonn@123.com'],
#        [2,'alexa',797971979,'alexa@123.com'],
#        [3,'delhi',8291212911,'delhi@123.com'],
#    ]
#    data.writerows(data2)
with open('mca.csv','r') as csvfile:
    data=csv.reader(csvfile)
 #   print(data)
    for var in data:
        print(var) 