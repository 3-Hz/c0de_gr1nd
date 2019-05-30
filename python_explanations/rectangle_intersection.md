# Rectangle Intersection  
  
Problem:  
Write a program which tests if two rectangles have a nonempty intersection. If the intersection is nonempty, return the rectangle formed by their intersection.  

The Rectangle is defined by the parameters [x, y, width, height]. The (x, y) coordinate corresponds to the bottom-left corner of the rectangle.  
  
If two boundaries of the rectangle touch, it is considered an intersection.  
  
Examples:  
```
 Input: R1 = [36, 65, 69, 5]
        R2 = [99, 83, 99, 61]
Output: Rectangle(x=0, y=0, width=-1, height=-1)
Conclusion: No Intersection

 Input: R1 = [26, 12, 76, 62]
        R2 = [68, 59, 77, 28]
Output: Rectangle(x=68, y=59, width=34, height=15)
Conclusion: Nonempty Intersection

 Input: R1 = [17, 77, 58, 67]
        R2 = [5, 19, 32, 60]
Output: Rectangle(x=17, y=77, width=20, height=2)
Conclusion: Nonempty Intersection
```  
  
Solution - from [rectangle-intersection-mysol.py](rectangle-intersection-mysol.py):  
```python
def is_intersect(R1, R2):
    return not (R1.x + R1.width < R2.x or
                R1.x > R2.x + R2.width or
                R1.y > R2.y + R2.height or
                R1.y + R1.height < R2.y)

def intersect_rectangle(R1, R2):
    if is_intersect(R1, R2):
        return (Rectangle(max(R1.x, R2.x), max(R1.y, R2.y), 
                        min(R1.x + R1.width, R2.x + R2.width) - max(R1.x, R2.x),
                        min(R1.y + R1.height, R2.y + R2.height) - max(R1.y, R2.y)))
    return Rectangle(0, 0, -1, -1)
```  
  
Explanation:  
  
There are 4 cases where the two rectangles (R1 and R2) do not intersect:  
  
1. R1 is left of R2  
    ```
    +----------+    +----------+
    |    R1    |    |    R2    | 
    +----------+    +----------+
    ```  
2. R1 is right of R2  
    ```
    +----------+    +----------+
    |    R2    |    |    R1    | 
    +----------+    +----------+
    ```  
3. R1 is above R2  
    ```
    +----------+
    |    R1    |
    +----------+

    +----------+
    |    R2    |
    +----------+
    ```  
4. R1 is below R2  
    ```
    +----------+
    |    R2    |
    +----------+

    +----------+
    |    R1    |
    +----------+
    ```  
  
The given Rectangle tuple is defined with the parameters (x, y, width, height).  

To test for the 4 cases above, you need to understand how to grab the 4 edges of a rectangle:  
```
x = left edge
x + width = right edge
y = bottom edge
y + height = top edge
```  
  
is_intersect function:  
1. Test for case 1 - R1's right edge is left of R2's left edge  
    ```python
    R1.x + R1.width < R2.x
    ```  
2. Test for case 2 - R1's left edge is right of R2's right edge  
    ```python
    R1.x > R2.x + R2.width
    ```  
3. Test for case 3 - R1's bottom edge is above R2's top edge 
    ```python
    R1.y > R2.y + R2.height
    ```  
4. Test for case 4 - R1's top edge is below R2's bottom edge 
    ```python
    R1.y + R1.height < R2.y
    ```  
5. Return False if any of these cases are True  
  
intersect_rectangle function:  
1. If R1 and R2 intersect, return the Rectangle formed by the intersection  
    a. Get the bottom-left point of the intersection rectangle  
    ```python
    max(R1.x, R2.x), max(R1.y, R2.y)
    ```  
    b. Get the width of the intersection rectangle  
    ```python
    min(R1.x + R1.width, R2.x + R2.width) - max(R1.x, R2.x)
    ```    
    c. Get the height of the intersection rectangle  
    ```python
    min(R1.y + R1.height, R2.y + R2.height) - max(R1.y, R2.y)
    ```  
    d. Return the Rectangle formed by the intersection  
2. Else return an empty Rectangle  
    ```python
    return Rectangle(0, 0, -1, -1)
    ```  