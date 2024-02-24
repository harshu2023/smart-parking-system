import MySQLdb
n='TN93606'
r =None
  
db=MySQLdb.connect('localhost','root','mediawiki','smart_parking')
curs=db.cursor()
curs.execute("SELECT * FROM details WHERE carnum='"+n+"'")
result=curs.fetchall()

for r in result:
    print r
    
if r == None:
    print 'CAR CANNOT BE PARKED'
else:
    print 'CAR CAN BE PARKED'

curs.close()
db.close()
