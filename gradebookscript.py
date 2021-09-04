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
