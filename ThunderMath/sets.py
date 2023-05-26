
class Set:
   def __init__(self):
      self.val= []
   def add(self,a):
      x=0
      if type(a)!=list: 
         for i in self.val:
            if i==a:
               x=x+1
         if x==0:
            self.val.append(a)
      else:
         for j in a:
            for i in self.val:
               if i==j:
                  x=x+1
            if x==0:
               self.val.append(j)
      
   def remove(self, a):
      if type(a)!= list:
         for i in self.val:
            if i==a:
               self.val.remove(a)
               break
      else:
         for j in a:
            n=0
            for i in self.val:
               if i==j:n=n+1
            if n!=0:
               self.val.remove(j)
               
      
         
   def clear(self):
      rem=[]
      for i in self.val:
         rem.append(i)
      for i in rem:
         self.val.remove(i)
   def print(self):
      string="{"
      n=0
      for i in self.val:
         n=n+1
         if n!=len(self.val):
            string = string+str(i)+", "
         else:
            string=string+str(i)+"}""\n"
      print(string)

   def getlist(self):
      return self.val
   def get(self):
      string="{"
      n=0
      for i in self.val:
         n=n+1
         if n!=len(self.val):
            string = string+str(i)+", "
         else:
            string=string+str(i)+"}""\n"
      return string
     
def intersect(a,b):
      result=Set()
      for i in a.val:
         for j in b.val:
            if i==j:result.val.append(i)
      return result
def union(a,b):
      result=a
      for i in b.val:
         n=0
         for j in result.val:
            if i==j:n=n+1
         if n==0:result.val.append(i)
      return result
def diff(a,b):
      result=a
      rem=[]
      for i in a.val:
         for j in b.val:
            if i==j:rem.append(j)
      for i in rem:
         result.val.remove(i)
      return result  
def prints(a):
      string="{"
      n=0
      for i in a.val:
         n=n+1
         if n!=len(a.val):
            string = string+str(i)+", "
         else:
            string=string+str(i)+"}""\n"
      print(string)

def clear(a):
      rem=[]
      for i in a.val:
         rem.append(i)
      for i in rem:
         a.val.remove(i)

def getlist(a):
      return a.val
def get(a):
      string="{"
      n=0
      for i in a.val:
         n=n+1
         if n!=len(a.val):
            string = string+str(i)+", "
         else:
            string=string+str(i)+"}""\n"
      return string
