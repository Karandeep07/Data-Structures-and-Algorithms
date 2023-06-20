# **Big-O Notation**

![Big O Graph](image.png)

## Big-O Complexities
- O(1) Constant: No loops
- O(log N) Logarithmic: Usually searching algorithms have log n if they are sorted (Binary Search)
- O(n) Linear: For loops, While loops through n items
- O(n log(n)) Log-Linear: Usually sorting operations
- O(n^2) Quadratic: Every element in a collection needs to be compared to ever other element. Two nested loops
- O(2^n) Exponential: Recursive algorithms that solves a problem of size N
- O(n!) Factorial: You are adding a loop for every element

## **Rule Book**
Rule 1: Always assume Worst Case <br>
Rule 2: Remove Constants<br>
Rule 3: Different inputs should have different variables. <br>
&emsp;( + ) for steps in order <br>
&emsp;( * ) for nested steps <br>
Rule 4: Drop Non-dominant terms

## **Factors Affecting Time Complexity**
- Operations (+, -, *, /)
- Comparisons (<, >, ==)
- Looping (for, while)
- Outside Function call (function())

### ***Note***
*Iterating through half a collection is still O(n)*

## **Space Complexity**
Def:

### **What causes space complexity**
- Variables
- Data Structures
- Function Call
- Allocations

### **Additional Resources**
[Big-O Cheatsheet](https://www.bigocheatsheet.com/)