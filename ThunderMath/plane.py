from math import *
class pt2:
   def __init__(self,x,y):
      if (type(x)==int or type(x)==float)and(type(y)==int or type(y)==float):
         self.x=x
         self.y=y
      else:
         raise TypeError("COORDINATE TYPE MUST BE OF INT OR FLOAT")
   def value(self):
      return [self.x,self.y]
   def change(self,x,y):
      if (type(x)==int or type(x)==float)and(type(y)==int or type(y)==float):
         self.x=x
         self.y=y
      else:
         raise TypeError("COORDINATE TYPE MUST BE OF INT OR FLOAT")
   def print(self):
      result="({0},{1})".format(self.x,self.y)
      print(result)
      
class pt3:
   def __init__(self,x,y,z):
      if (type(x)==int or type(x)==float)and(type(y)==int or type(y)==float)and(type(z)==int or type(z)==float):
         self.x=x
         self.y=y
         self.z=z
      else:
         raise TypeError("COORDINATE TYPE MUST BE OF INT OR FLOAT")
   def value(self):
      return [self.x,self.y,self.z]
   def change(self,x,y,z):
      if (type(x)==int or type(x)==float)and(type(y)==int or type(y)==float)and(type(z)==int or type(z)==float):
         self.x=x
         self.y=y
         self.z=z
      else:
         raise TypeError("COORDINATE TYPE MUST BE OF INT OR FLOAT")
   def print(self):
      result="({0},{1},{2})".format(self.x,self.y,self.z)
      print(result)

def dist(a,b):
   if (type(a)==pt2 and type(b)==pt2)or (type(a)==pt3 and type(b)==pt3): 
     if type(a)==pt2:
      i=pow(b.x-a.x,2)
      j=pow(b.y-a.y,2)
      result=sqrt(i+j)
      return(result)
     if type(a)==pt3:
      i=pow(b.x-a.x,2)
      j=pow(b.y-a.y,2)
      k=pow(b.z-a.z,2)
      result=sqrt(i+j+k)
      return(result)
   else:
      if (type(a)!=pt2 and type(a)!=pt3) or (type(b)!=pt2 and type(b)!=pt3):
         err="TYPE OF arg1 IS "+str(type(a))+"AND TYPE OF arg2 IS "+str(type(b))+"\nPOINTS MUST BE OF TYPE pt2 OR pt3"
         raise TypeError(err)
      elif type(a)!=type(b):
         err="TYPE OF arg1 IS "+str(type(a))+"AND TYPE OF arg2 IS "+str(type(b))+"\nPOINTS MUST BE OF SAME TYPE"
         raise TypeError(err)

      
def mid(a,b):
   if (type(a)==pt2 and type(b)==pt2)or (type(a)==pt3 and type(b)==pt3): 
     if type(a)==pt2:
      result=pt2(0,0)
      result.x=(a.x+b.x)/2
      result.y=(a.y+b.y)/2
      return(result)
     if type(a)==pt3:
      result=pt3(0,0,0)
      result.x=(a.x+b.x)/2
      result.y=(a.y+b.y)/2
      result.z=(a.z+b.z)/2
      return(result)
   else:
      if (type(a)!=pt2 and type(a)!=pt3) or (type(b)!=pt2 and type(b)!=pt3):
         err="TYPE OF arg1 IS "+str(type(a))+"AND TYPE OF arg2 IS "+str(type(b))+"\nPOINTS MUST BE OF TYPE pt2 OR pt3"
         raise TypeError(err)
      elif type(a)!=type(b):
         err="TYPE OF arg1 IS "+str(type(a))+"AND TYPE OF arg2 IS "+str(type(b))+"\nPOINTS MUST BE OF SAME TYPE"
         raise TypeError(err)

def comp(a,b):
   if (type(a)==pt2 and type(b)==pt2)or (type(a)==pt3 and type(b)==pt3): 
     if type(a)==pt2:
        if (a.x==b.x)and(a.y==b.y):return(True)   
        else:return(False)
     if type(a)==pt3:
        if (a.x==b.x)and(a.y==b.y)and(a.z==b.z):return(True)   
        else:return(False)
   else:
      if (type(a)!=pt2 and type(a)!=pt3) or (type(b)!=pt2 and type(b)!=pt3):
         err="TYPE OF arg1 IS "+str(type(a))+"AND TYPE OF arg2 IS "+str(type(b))+"\nPOINTS MUST BE OF TYPE pt2 OR pt3"
         raise TypeError(err)
      elif type(a)!=type(b):
         err="TYPE OF arg1 IS "+str(type(a))+"AND TYPE OF arg2 IS "+str(type(b))+"\nPOINTS MUST BE OF SAME TYPE"
         raise TypeError(err)
