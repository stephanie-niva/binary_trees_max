class Node:
    def __init__(self,data):
        self.data= data
        self.left= None
        self.right= None

class LargestNode:  
    def __init__(self): 
        self.root = None;  

    def largestElement(self, time): 
         if(self.root == None):  
            print("empty");  
            return 0;  

         else:     
             maximum = time.data;  
         if(time.left != None):  
             leftMax = self.largestElement(time.left);  
             maximum = max(maximum, leftMax);  
         if(time.right != None):  
             rightMax = self.largestElement(time.right);     
             maximum = max(maximum, rightMax);  
              
         return maximum;  
   
root = LargestNode(); 
root.root = Node(15);  
root.root.left = Node(20);  
root.root.right = Node(35);  
root.root.left.left = Node(74);  
root.root.right.left = Node(55);  
root.root.right.right = Node(6);  

print("Largest element: " + str(root.largestElement(root.root)));  







