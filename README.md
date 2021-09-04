# GradeBook
You are a student and you are trying to organize your subjects and grades using Python. Let’s explore what we’ve learned about lists to organize your subjects and scores.


Task 
= 

1. Create a list called subjects and fill it with the classes you are taking:
- "physics"
- "calculus"
- "poetry"
- "history"

2. Create a list called grades and fill it with your scores:
- 98
- 97
- 85
- 88

3. Manually (without any methods) create a two-dimensional list to combine subjects and grades. Use the table below as a reference to associated values.

| Name  |  Test Score |
| ------------- | ------------- |
| Physis  | 98  |
| Calculus| 97 |
| Poetry  | 85  |
| History  | 88  |

Assign the value into a variable called gradebook.

4. Print gradebook.
5. Your grade for your computer science class just came in! You got a perfect score, 100!
Use the .append() method to add a list with the values of "computer science" and an associated grade value of 100 to our two-dimensional list of gradebook.

6. Your grade for "visual arts" just came in! You got a 93! Use append to add "visual arts", 93 to gradebook.

7. Our instructor just told us they made a mistake grading and are rewarding an extra 5 points for our visual arts class. Access the index of the grade for your visual arts class and modify it to be 5 points greater.

8. You decided to switch from a numerical grade value to a Pass/Fail option for your poetry class. Find the grade value in your gradebook for your poetry class and use the .remove() method to delete it.

9. Use the .append() method to then add a new "Pass" value to the sublist where your poetry class is located.

10. You also have your grades from last semester, stored in last_semester_gradebook.
Create a new variable full_gradebook that combines both last_semester_gradebook and gradebook using + to have one complete grade book.
Print full_gradebook to see our completed list.


Code
=
```
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["Physics", "Calculus", "Poetry", "History"]#list of subject
grades = [98, 97,85,88]#table for grade
#manually combining subject list with grades to create a 2d list
gradebook = [
[subjects[0],grades[0]],
[subjects[1],grades[1]],
[subjects[2],grades[2]],
[subjects[3],grades[3]] 
]
print(gradebook)
print("---------")
gradebook.append(["Computer Science", 100])#append computer science course and grade
gradebook.append(["CVisual Art", 93])#append visual art and grade
gradebook[-1][-1] = 93+5 #adding 5 point to visual art class
gradebook[2].remove(85) #removing numrical gade for poetry class
gradebook[2].append("Pass")#adding "pass" vaue to poetry class. 
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)#printing full grade book 
```

Output/Test Data
=
```
[['Physics', 98], ['Calculus', 97], ['Poetry', 85], ['History', 88]]
---------
[['politics', 80], ['latin', 96], ['dance', 97], ['architecture', 65], ['Physics', 98], ['Calculus', 97], ['Poetry', 'Pass'], ['History', 88], ['Computer Science', 100], ['CVisual Art', 98]]
```

Conclusion 
= 
In order to complete this project I had to create a list, access, add,remove, and modify list elements. A list is a build data structure that allows programmers to work with a collection of data in sequenctial order. A list can contain any data type, data type being string, integer, boolean, and float. To manipule data within a list I used python build in method. To add an additional data to a list I used the append method, and to remove data to a list the remove method was used. To access a specefic data in a list I used index to select an item, Python list are zero index meaning that the first element in a list  has index 0, and a -1 index selects the last eleement in a list. In order to change a value in a list, we simply have to reassign the value using the specefic index. Finanly to create a 2d list we simply used two pair of bracket, and we used the plus symbol o concateenate two different list. 

