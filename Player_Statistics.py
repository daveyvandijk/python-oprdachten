import random
username = input
import time 

print ("tpy your character name ")
time.sleep(2)
print ("merlijn")
print ("davey")
print ("mike")
print ("lucas")
print ("max")
print ("sam")
print ("job")
print ("floor")
print ("rianne")
print ("kip")
username = input()
time.sleep(2)

a = {1 : 'lazer eyes',2 : 'teleport',3 : 'super speed',4 : 'invisible',5 : 'firehands'}



min = 1
max = 10000

if username == "merlijn":
     print (f"health {random.randint(min,max)} ")
     print ("special power", a[random.randint(1, len(a))])
     print (f"LVL {random.randint(min,max)}" )

if username == "davey":
     print (f"health {random.randint(min,max)}")
     print ("special power", a[random.randint(1, len(a))])
     print (f"LVL {random.randint(min,max)} ")

if username == "mike":
     print (f"health {random.randint(min,max)}")
     print ("special power", a[random.randint(1, len(a))])
     print (f"LVL {random.randint(min,max)}")
     
if username == "lucas":
     print (f"health {random.randint(min,max)}")
     print ("special power", a[random.randint(1, len(a))])
     print (f"LVL {random.randint(min,max)}")

if username == "max":
     print (f"health {random.randint(min,max)}")
     print ("special power", a[random.randint(1, len(a))])
     print (f"LVL {random.randint(min,max)}")     

if username == "sam":
     print (f"health {random.randint(min,max)}")
     print ("special power", a[random.randint(1, len(a))])
     print (f"LVL {random.randint(min,max)}")

if username == "job":
     print (f"health {random.randint(min,max)}")
     print ("special power", a[random.randint(1, len(a))])
     print (f"LVL{random.randint(min,max)}")

if username == "floor":
     print (f"health {random.randint(min,max)}")
     print ("special power", a[random.randint(1, len(a))])
     print (f"LVL {random.randint(min,max)}")

if username == "rianne":
     print (f"health {random.randint(min,max)}")
     print ("special power", a[random.randint(1, len(a))])
     print (f"LVL {random.randint(min,max)}")

if username == "kip":
     print (f"health {random.randint(min,max)}")
     print ("special power", a[random.randint(1, len(a))])
     print (f"LVL {random.randint(min,max)}")               