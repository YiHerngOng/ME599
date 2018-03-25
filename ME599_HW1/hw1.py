#!/usr/bin/env python


#Yi Herng Ong, ME 599 Homework 1
#SID 932278854

import sys
import csv
import numpy as np

#Open and read csv file into a numpy array
#Each element of this array will be an array
def open_csv_to_list(filename):
    words = []
    try:
        with open(filename, 'rb') as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                    words.append(line)
    except:
        sys.exit(str(filename)+ " "+ "does not exist")

    words_np = np.array(words)
    return words_np

#Retrieve data from specific column of bunch of lists in a numpy array
def ret_list(l,n):
    new_list_1 = []
    for i in xrange(len(l)):
        new_list_1.append(l[i,n])
    return new_list_1

#Return column position from a list of titles
def return_pos(l, title):
    for i in xrange(l.size):
        if l[i] == title: #if element of the list matches the desired title (for example: Final Score)
            return i

#Check whether command line argument is less than 1
def check_argument():
    usr_argv = sys.argv[1:]
    if len(usr_argv) < 1:
        sys.exit("No csv file detected") #system exit if argument less than 1
    return usr_argv

#Convert a list of string to a list of integer
def conv_str_to_int(l):
    new_list = []
    for i in xrange(len(l)):
          new_list.append(float(l[i]))
    return new_list

# Calculate average final score
def avg_score(l):
    return sum(l) / len(l)

#Calculate Percent above the average score
def percent_above_(l, score):
    count = 0.0
    for i in l:
        if i >= score:
            #print "here"
            count += 1
    #return count
    return (count / float(len(l)))*100     

#Return median of a list (for example: Final Score list)
def median_score(l):
    new_list = []
    new_list = sorted(l)
    return np.median(new_list)

#This function returns a string of title that has lowest average score 
def get_hardest(l, hw):
    namelist = []
    new_list = []
    score_list = []
    if len(hw) == 2:        #If there are two titles required (For example, finding hardest assignment requires keywords "Homework" and "Exercise")           
        for i,x in enumerate(l[0]):
            if (hw[0] in l[0,i]) or (hw[1] in l[0,i]):      #If one of the hw strings matches one of the titles
                namelist.append(l[0,i])         #Create title namelist
                new_list = []
                for j in xrange(len(l)):
                    new_list.append(l[j,i])     #Retrieve data from columns that correspond to the titles which match hw strings
                score_list.append(new_list)

    elif len(hw) == 1:  #If there is only one title required
        for i,x in enumerate(l[0]):
            if (hw[0] in l[0,i]):   #If hw strings matches one of the titles
                namelist.append(l[0,i]) #Create title namelist
                new_list = []
                for j in xrange(len(l)):
                    new_list.append(l[j,i]) #Retrieve data from columns that correspond to the titles which match hw strings 
                score_list.append(new_list)    
              
    #remove element of the list has non float number, and convert string into float
    score_list_1 = []
    for a in xrange(len(score_list)):
        new_list_1 = []
        for m in xrange(len(score_list[0])):
            try:
                new_list_1.append(float(score_list[a][m]))        #try to convert to float    
            except:
                pass    #if fail, pass, continue to the next element
        score_list_1.append(new_list_1) #Create a new list of score without any non-number element

    new_score_list = []
    names = {}
    for b in score_list_1:  #Calculate average score of each list in percentage
        new_score_list.append(((sum(b) / len(b))/len(b))*100.0)
    
    for c in xrange(len(new_score_list)):   #Create a dictionary with title namelist and average score list
        names[new_score_list[c]] = namelist[c]

    return names.get(min(new_score_list)) #Return the name of title that has lowest average score

#Assign number of students that get each letter grade
def grade_assignment(l):
    letter_grades = {}
    grades_range = [94, 90, 87, 84, 80, 77, 74, 70, 67, 64, 61, 0]
    grade_a = 0
    grade_am = 0
    grade_bp = 0
    grade_b = 0
    grade_bm = 0
    grade_cp =0 
    grade_c = 0
    grade_cm = 0
    grade_dp = 0
    grade_d = 0
    grade_dm = 0
    grade_f = 0

    for j in l:
        if j >= grades_range[0]:
            grade_a += 1
        elif j >= grades_range[1]:
            grade_am += 1
        elif j >= grades_range[2]:
            grade_bp += 1
        elif j >= grades_range[3]:
            grade_b += 1            
        elif j >= grades_range[4]:
            grade_bm += 1
        elif j >= grades_range[5]:
            grade_cp += 1
        elif j >= grades_range[6]:
            grade_c += 1
        elif j >= grades_range[7]:
            grade_cm += 1
        elif j >= grades_range[8]:
            grade_dp += 1    
        elif j >= grades_range[9]:
            grade_d += 1
        elif j >= grades_range[10]:
            grade_dm += 1
        else:
            grade_f += 1

    return [grade_a,grade_am,grade_bp,grade_b,grade_bm,grade_cp,grade_c,grade_cm,grade_dp,grade_d,grade_dm,grade_f]

#Calculate number of student who will complain about their grades
def grade_complain(l):
    count = 0
    grades_range = [94, 90, 87, 84, 80, 77, 70, 67, 64, 61, 0]
    for i in l:
        for j in grades_range:
            if abs(i-j) < 0.5: #If difference of their final score and minimum grade of the grade range is less than 0.5 %
                count += 1
    return count

#Calculate new cutoff of letter grade
def grade_assignment_2(l):
    l.sort(reverse=True)
    grade_cutoff = [0.1, 0.2, 0.3, 0.3 ]
    A_list = []
    A_list = l[0:int(len(l)*0.1)]
    B_list = []
    B_list = l[int(len(l)*0.1) : int(len(l)*0.3)]
    C_list = []
    C_list = l[int(len(l)*0.3) : int(len(l)*0.6)]
    D_list = []
    D_list = l[int(len(l)*0.6) : int(len(l)*0.9)]
    F_list = []
    F_list = l[int(len(l)*0.9):]

    return [min(A_list), min(B_list), min(C_list), min(D_list), min(F_list)]

if __name__ == '__main__':

    #Direction 1 & 2
    usr_argv = check_argument()
    grades = open_csv_to_list(usr_argv[0])

    final_score_inc = return_pos(grades[0], 'Final Score') #Return column position of 'Final Score'
    final_score_list = ret_list(grades[1:], final_score_inc) #Return a list of final score

    #Convert string to float
    final_score_list_f = conv_str_to_int(final_score_list)
    #Calculate average 
    avg_final_score = avg_score(final_score_list_f)
    print 'Average final score: ' + ("%0.2f" %avg_final_score)
    #Calculate percent above average
    perc_above_avg = percent_above_(final_score_list_f, avg_final_score)
    print 'Above Average: ' + ("%0.2f" %perc_above_avg) + '%'
    #Calculate median
    median_final_score = median_score(final_score_list_f)
    print 'Median Score: ' + ("%0.2f" %median_final_score)
    #Calculate percent above median
    perc_above_med = percent_above_(final_score_list_f, median_final_score)
    print 'Above Median: ' + ("%0.2f" %perc_above_med) + '%'

    #Direction 3 & 4
    #Determine the hardest assignment by finding keywords "Homework" and "Exercise"
    hw_string_list = ['Homework', 'Exercise']
    assignment_list = get_hardest(grades, hw_string_list) 
    print 'Hardest Assignment: ' + assignment_list

    #Determine the hardest lab by finding key words "Lab"
    hw_string_list_1 = ['Lab']
    assignment_list_1 = get_hardest(grades, hw_string_list_1) 
    print 'Hardest Lab: ' + assignment_list_1

    #Direction 5,6,7
    #Assign letter grades
    final_grade = []
    letter_grade = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']
    print 'How many students get each grade ? '
    final_grade = grade_assignment(final_score_list_f)
    for i,j in enumerate(letter_grade):
        print j + ':' + str(final_grade[i])

    #Calculate number of complains
    num_complain = grade_complain(final_score_list_f)
    print str(num_complain) + ' student will complain about their grades'

    #Calculate new letter grades cutoff
    letter_grade_2 = ['A','B','C','D','F']
    print 'New grade cutoff:'
    final_grade_2 = grade_assignment_2(final_score_list_f)
    for a,b in enumerate(letter_grade_2):
        print b + ':' + str(final_grade_2[a])

#python.exe D:\Downloads\ME599_HW1_Ong.py D:\Downloads\grades.csv