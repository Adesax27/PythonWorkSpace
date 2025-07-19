import pandas as pd

studName = ('Bett James', 'Namukolo Abrams', 'Vera Abutu', 'Kwame Doga', 'Lukeman Ahmad', 'Akin Torey', 'Luke Brant', 'James Kenyata', 'Ngugi Tionga', 'Okoro Eze', 'Agatha Chiluba', 'Mangu Joseph', 'Longe Jethro', 'Florenc Giwa', 'Vetiva Lucent', 'Melody Braimoh', 'Victor Ihab', 'Mimi Trucker', 'Maguel Peter', 'Wellington Zuba')
studId = ('GR-0483', 'GR-0484', 'GR-0485', 'GR-0486', 'GR-0487', 'GR-0488', 'GR-0489', 'GR-0490', 'GR-0491', 'GR-0492', 'GR-0493', 'GR-0494', 'GR-0495', 'GR-0496', 'GR-0497', 'GR-0498', 'GR-0499', 'GR-0500', 'GR-0501', 'GR-0502',)

# Quizes
qChem = [127, 141,51,26,29,99,171,51,155,147,187,123,179,98,17,67,177,148,23,182] 
qBio = [184,177,112,133,21,90,117,188,17,61,149,127,120,42,177,162,155,141,183,102] 
qPhy =[52,21,61,62,177,0,151,41,12,0,117,48,119,122,114,145,135,34,81,71] 
qMath = [133,136,74,86,50,109,121,120,51,79,133,83,155,84,60,104,43,61,33,60]


# HomeWorks
hChem = [135,82,102,166,180,125,129,103,111,153,106,171,160,172,60,177,14,182,95,130]
hBio = [186,170,55,108,123,47,47,156,136,66,100,88,136,19,70,125,90,146,43,70]
hPhy = [142,12,105,59,11,119,63,31,77,97,88,139,119,20,109,65,6,104,143,28]
hMath = [97,180,50,181,18,144,16,188,145,149,79,33,97,157,102,58,44,136,79,77]

# Class Attendance
cChem = [17,95,96,75,38,26,91,39,14,31,67,82,48,30,48,68,83,80,63,92]
cBio = [58,57,71,52,47,88,51,13,42,58,64,87,92,36,48,38,51,41,28,19] 
cPhy = [29,43,83,94,38,37,93,90,70,54,86,63,65,24,84,43,50,73,80,88]
cMath = [34,48,93,66,34,14,22,25,36,71,55,13,50,18,73,36,63,44,95,94]

# Exams
eChem = [46,52,24,73,80,83,70,98,96,48,83,48,93,94,36,39,75,46,27,47]
eBio = [97,41,51,68,90,18,25,72,27,50,80,23,89,84,34,36,35,80,25,38] 
ePhy = [73,31,98,65,51,44,19,18,43,75,61,35,70,68,31,14,33,23,16,19]
eMath = [45,31,94,67,68,65,41,52,22,76,70,10,81,46,87,89,48,53,62,31]

import statistics as stt 

qc = 0
hc = 0
cc = 0
ec = 0

# dict = {}
# avg_dict = {}

chem_avg_list = []
bio_avg_list = []
phy_avg_list = []
math_avg_list = []

subjects = ("Chem", "Phy", "Bio", "Math")
scoresCategories = ("QuizScores", "Homework", "ClassAttend", "Exam")

for a, b, c, d, stud in zip(qChem, hChem, cChem, eChem, studName):
    
    qc = (a / 190) * 30

    hc = (b / 190) * 15
    
    cc = (c / 96) * 12

    ec = (d / 100) * 43
    
    
    chem_avg = qc + hc + cc + ec
    chem_avg_list.append(chem_avg)
    # dict[stud] = {subjects[0]:{scoresCategories[0]:a, scoresCategories[1]:b, scoresCategories[2]:c, scoresCategories[3]:d}}
    
chem_avg_list    
   
for a, b, c, d, stud in zip(qBio, hBio, cBio, eBio, studName):
    qb = (a / 190) * 30

    hb = (b / 190) * 15
    
    cb = (c / 96) * 12
    
    eb = (d / 100) * 43
    
    bio_avg = qb + hb + cb + eb
    bio_avg_list.append(bio_avg)
    
bio_avg_list
    
for a, b, c, d, stud in zip(qPhy, hPhy, cPhy, ePhy, studName):
    qp = (a / 190) * 30
    
    hp = (b / 190) * 15
  
    cp = (c / 96) * 12
   
    ep = (d / 100) * 43
    
    phy_avg = qp + hp + cp + ep
    phy_avg_list.append(phy_avg)
    
phy_avg_list    
    
for a, b, c, d, stud in zip(qMath, hMath, cMath, eMath, studName):
    qm = (a / 190) * 30
 
    hm = (b / 190) * 15
  
    cm = (c / 96) * 12
  
    em = (d / 100) * 43
  
    math_avg = qm + hm + cm + em
    math_avg_list.append(math_avg)
    
    
math_avg_list


# calcilating for the averages

AvgScore = []
for chem, bio, phy, math in zip(chem_avg_list,bio_avg_list,phy_avg_list,math_avg_list):
    Average = stt.mean([chem, bio, phy, math])
    AvgScore.append(Average)


# To calculate for the C.G.P.A
GPA = []
for score in AvgScore:
    cal = (score/100) * 5
    GPA.append(cal)
  
    
# To find alphabectic grade using the (if,elif and else statement)
grades = []
status = []
for i in AvgScore:
    if i >= 90:
        grades.append("A")
        status.append("Pass")
    elif i >= 75:
        grades.append("B")
        status.append("Pass")
    elif i >= 65:
        grades.append("C")
        status.append("Pass")
    elif i >= 55:
        grades.append("D")
        status.append("Pass")
    elif i >= 50:
        grades.append("E")
        status.append("Retake")
    else:
        grades.append("F")
        status.append("Fail")


def dataFrameCreator(listset, colNamesSet):
    dataTable = pd.DataFrame()

    dataTable[colNamesSet[0]] = listset[0]
    dataTable[colNamesSet[1]] = listset[1]
    dataTable[colNamesSet[2]] = listset[2]
    dataTable[colNamesSet[3]] = listset[3]
    dataTable[colNamesSet[4]] = listset[4]
    dataTable[colNamesSet[5]] = listset[5]
    dataTable[colNamesSet[6]] = listset[6]
    dataTable[colNamesSet[7]] = listset[7]
    dataTable[colNamesSet[8]] = listset[8]
    dataTable[colNamesSet[9]] = listset[9]
    dataTable[colNamesSet[10]] = listset[10]
    dataTable[colNamesSet[11]] = listset[11]
    dataTable[colNamesSet[12]] = listset[12]
    dataTable[colNamesSet[13]] = listset[13]
    dataTable[colNamesSet[15]] = listset[14]
    dataTable[colNamesSet[15]] = listset[15]
    dataTable[colNamesSet[16]] = listset[16]
    dataTable[colNamesSet[17]] = listset[17]
    dataTable[colNamesSet[18]] = listset[18]
    dataTable[colNamesSet[19]] = listset[19]
    dataTable[colNamesSet[20]] = listset[20]
    dataTable[colNamesSet[21]] = listset[21]
    dataTable[colNamesSet[22]] = listset[22]
    dataTable[colNamesSet[23]] = listset[23]
    dataTable[colNamesSet[24]] = listset[24]
    dataTable[colNamesSet[25]] = listset[25]
     
    return dataTable
    
listset = [studName,studId,qChem,qBio,qPhy,qMath,hChem,hBio,hPhy,hMath,cChem,cBio,cPhy,cMath,eChem,eBio,ePhy,eMath,chem_avg_list,bio_avg_list,phy_avg_list,math_avg_list,AvgScore,GPA,grades,status]
colNamesSet = ['Students name','Student ID','chemistry quiz','biology quiz','physics quiz','math quiz','Home chem','Home Bio','Home phy','Home math','class chem','class bio','class phy','class math','exam chem','exam bio','exam phy','exam math','chem avg','bio avg','phy avg','math avg','Avg Scores','G.P.A','Grade','Status']

dataFrameCreator(listset, colNamesSet)


#dataTable.to_csv('C:/Users/USER/Documents/book/project.csv')


studName = ('Bett James', 'Namukolo Abrams', 'Vera Abutu', 'Kwame Doga', 'Lukeman Ahmad', 'Akin Torey', 'Luke Brant', 'James Kenyata', 'Ngugi Tionga', 'Okoro Eze', 'Agatha Chiluba', 'Mangu Joseph', 'Longe Jethro', 'Florenc Giwa', 'Vetiva Lucent', 'Melody Braimoh', 'Victor Ihab', 'Mimi Trucker', 'Maguel Peter', 'Wellington Zuba')
studId = ('GR-0483', 'GR-0484', 'GR-0485', 'GR-0486', 'GR-0487', 'GR-0488', 'GR-0489', 'GR-0490', 'GR-0491', 'GR-0492', 'GR-0493', 'GR-0494', 'GR-0495', 'GR-0496', 'GR-0497', 'GR-0498', 'GR-0499', 'GR-0500', 'GR-0501', 'GR-0502',)

# Quizes
qChem = [127, 141,51,26,29,99,171,51,155,147,187,123,179,98,17,67,177,148,23,182] 
qBio = [184,177,112,133,21,90,117,188,17,61,149,127,120,42,177,162,155,141,183,102] 
qPhy =[52,21,61,62,177,0,151,41,12,0,117,48,119,122,114,145,135,34,81,71] 
qMath = [133,136,74,86,50,109,121,120,51,79,133,83,155,84,60,104,43,61,33,60]


# HomeWorks
hChem = [135,82,102,166,180,125,129,103,111,153,106,171,160,172,60,177,14,182,95,130]
hBio = [186,170,55,108,123,47,47,156,136,66,100,88,136,19,70,125,90,146,43,70]
hPhy = [142,12,105,59,11,119,63,31,77,97,88,139,119,20,109,65,6,104,143,28]
hMath = [97,180,50,181,18,144,16,188,145,149,79,33,97,157,102,58,44,136,79,77]

# Class Attendance
cChem = [17,95,96,75,38,26,91,39,14,31,67,82,48,30,48,68,83,80,63,92]
cBio = [58,57,71,52,47,88,51,13,42,58,64,87,92,36,48,38,51,41,28,19] 
cPhy = [29,43,83,94,38,37,93,90,70,54,86,63,65,24,84,43,50,73,80,88]
cMath = [34,48,93,66,34,14,22,25,36,71,55,13,50,18,73,36,63,44,95,94]

# Exams
eChem = [46,52,24,73,80,83,70,98,96,48,83,48,93,94,36,39,75,46,27,47]
eBio = [97,41,51,68,90,18,25,72,27,50,80,23,89,84,34,36,35,80,25,38] 
ePhy = [73,31,98,65,51,44,19,18,43,75,61,35,70,68,31,14,33,23,16,19]
eMath = [45,31,94,67,68,65,41,52,22,76,70,10,81,46,87,89,48,53,62,31]

studsRecs = {}
def studInfoFolder(studName, Quizes:qChem,qBio,qPhy,qMath, Homework:hChem,hBio,hPhy,hMath, classAttend:cChem,cBio,cPhy,cMath, exams: eChem,eBio,ePhy,eMath):
    dict = {}
    eachDict = [Quizes:qChem,qBio,qPhy,qMath, Homework:hChem,hBio,hPhy,hMath, classAttend:cChem,cBio,cPhy,cMath, exams: eChem,eBio,ePhy,eMath]
    studsRecs[studName] = [Quizes:qChem,qBio,qPhy,qMath, Homework:hChem,hBio,hPhy,hMath, classAttend:cChem,cBio,cPhy,cMath, exams: eChem,eBio,ePhy,eMath]
    return studsRecs
    
def studInfoLoader():   
    studName = input('enter student name: ')
    qChem = input('enter chem result: ')
    qBio = input('enter bio result: ')
    qPhy = input('enter phy result: ')
    qMath = input('enter math result: ')
    hChem = input('enter chem result: ')
    hBio = input('enter bio result: ')
    hPhy = input('enter phy result: ')
    hMath = input('enter math result: ')
    cChem = input('enter chem result: ')
    cBio = input('enter bio result: ')
    cPhy = input('enter phy result: ')
    cMath = input('enter math result: ')
    eChem = input('enter chem result: ')
    eBio = input('enter bio result: ')
    ePhy = input('enter phy result: ')
    eMath = input('enter math result: ')
    records = studInfoFolder(studName,Quizes:qChem,qBio,qPhy,qMath, Homework:hChem,hBio,hPhy,hMath, classAttend:cChem,cBio,cPhy,cMath, exams: eChem,eBio,ePhy,eMath)
    print(records)


# 3. To hold each students performance records
studsRecs = {}
def studInfoFolder(studName, studId, GPA, grades, status):
   dict = {}
   eachDict = [studId, GPA, grades, status]
   studsRecs[studName] = [studId, GPA, grades, status]
   return studsRecs
   
def studInfoLoader():   
   studName = input('enter student name: ')
   studId = input('enter student Id: ')
   GPA = input('enter student gpa: ')
   grades = input('enter student grade: ')
   status = input('enter student status: ')
   records = studInfoFolder(studName, studId, GPA, grades, status)
   print(records)


4. # 4. To hold each subject performance records in a container
subjectsRes = {}
for students,studentId,qC,qB,qP,qM in zip(studName,studId,qChem,qBio,qPhy,qMath):
    subjectsRes[students] = studentId,qC,qB,qP,qM
    continue
print('quiz results:', subjectsRes)

for students,studentId,hC,hB,hP,hM in zip(studName1,studId1,hChem,hBio,hPhy,hMath):
    subjectsRes[students] = studentId,hC,hB,hP,hM 
    continue
print('home_work results:', subjectsRes)

for students,studentId,cC,cB,cP,cM in zip(studName2,studId2,cChem,cBio,cPhy,cMath):
    subjectsRes[students] = studentId,cC,cB,cP
    continue
print('class attendance results:', subjectsRes)

for students,studentId,eC,eB,eP,eM in zip(studName3,studId3,eChem,eBio,ePhy,eMath):
    subjectsRes[students] = studentId,eC,eB,eP,eM
print('Exam results:', subjectsRes)

studName = ('Bett James', 'Namukolo Abrams', 'Vera Abutu', 'Kwame Doga', 'Lukeman Ahmad', 'Akin Torey', 'Luke Brant', 'James Kenyata', 'Ngugi Tionga', 'Okoro Eze', 'Agatha Chiluba', 'Mangu Joseph', 'Longe Jethro', 'Florenc Giwa', 'Vetiva Lucent', 'Melody Braimoh', 'Victor Ihab', 'Mimi Trucker', 'Maguel Peter', 'Wellington Zuba')
studName1 = ('Bett James', 'Namukolo Abrams', 'Vera Abutu', 'Kwame Doga', 'Lukeman Ahmad', 'Akin Torey', 'Luke Brant', 'James Kenyata', 'Ngugi Tionga', 'Okoro Eze', 'Agatha Chiluba', 'Mangu Joseph', 'Longe Jethro', 'Florenc Giwa', 'Vetiva Lucent', 'Melody Braimoh', 'Victor Ihab', 'Mimi Trucker', 'Maguel Peter', 'Wellington Zuba')
studName2 = ('Bett James', 'Namukolo Abrams', 'Vera Abutu', 'Kwame Doga', 'Lukeman Ahmad', 'Akin Torey', 'Luke Brant', 'James Kenyata', 'Ngugi Tionga', 'Okoro Eze', 'Agatha Chiluba', 'Mangu Joseph', 'Longe Jethro', 'Florenc Giwa', 'Vetiva Lucent', 'Melody Braimoh', 'Victor Ihab', 'Mimi Trucker', 'Maguel Peter', 'Wellington Zuba')
studName3 = ('Bett James', 'Namukolo Abrams', 'Vera Abutu', 'Kwame Doga', 'Lukeman Ahmad', 'Akin Torey', 'Luke Brant', 'James Kenyata', 'Ngugi Tionga', 'Okoro Eze', 'Agatha Chiluba', 'Mangu Joseph', 'Longe Jethro', 'Florenc Giwa', 'Vetiva Lucent', 'Melody Braimoh', 'Victor Ihab', 'Mimi Trucker', 'Maguel Peter', 'Wellington Zuba')


studId = ('GR-0483', 'GR-0484', 'GR-0485', 'GR-0486', 'GR-0487', 'GR-0488', 'GR-0489', 'GR-0490', 'GR-0491', 'GR-0492', 'GR-0493', 'GR-0494', 'GR-0495', 'GR-0496', 'GR-0497', 'GR-0498', 'GR-0499', 'GR-0500', 'GR-0501', 'GR-0502',)
studId1 = ('GR-0483', 'GR-0484', 'GR-0485', 'GR-0486', 'GR-0487', 'GR-0488', 'GR-0489', 'GR-0490', 'GR-0491', 'GR-0492', 'GR-0493', 'GR-0494', 'GR-0495', 'GR-0496', 'GR-0497', 'GR-0498', 'GR-0499', 'GR-0500', 'GR-0501', 'GR-0502',)
studId2 = ('GR-0483', 'GR-0484', 'GR-0485', 'GR-0486', 'GR-0487', 'GR-0488', 'GR-0489', 'GR-0490', 'GR-0491', 'GR-0492', 'GR-0493', 'GR-0494', 'GR-0495', 'GR-0496', 'GR-0497', 'GR-0498', 'GR-0499', 'GR-0500', 'GR-0501', 'GR-0502',)
studId3 = ('GR-0483', 'GR-0484', 'GR-0485', 'GR-0486', 'GR-0487', 'GR-0488', 'GR-0489', 'GR-0490', 'GR-0491', 'GR-0492', 'GR-0493', 'GR-0494', 'GR-0495', 'GR-0496', 'GR-0497', 'GR-0498', 'GR-0499', 'GR-0500', 'GR-0501', 'GR-0502',)
# Quizes
qChem = [127, 141,51,26,29,99,171,51,155,147,187,123,179,98,17,67,177,148,23,182] 
qBio = [184,177,112,133,21,90,117,188,17,61,149,127,120,42,177,162,155,141,183,102] 
qPhy =[52,21,61,62,177,0,151,41,12,0,117,48,119,122,114,145,135,34,81,71] 
qMath = [133,136,74,86,50,109,121,120,51,79,133,83,155,84,60,104,43,61,33,60]


# HomeWorks
hChem = [135,82,102,166,180,125,129,103,111,153,106,171,160,172,60,177,14,182,95,130]
hBio = [186,170,55,108,123,47,47,156,136,66,100,88,136,19,70,125,90,146,43,70]
hPhy = [142,12,105,59,11,119,63,31,77,97,88,139,119,20,109,65,6,104,143,28]
hMath = [97,180,50,181,18,144,16,188,145,149,79,33,97,157,102,58,44,136,79,77]

# Class Attendance
cChem = [17,95,96,75,38,26,91,39,14,31,67,82,48,30,48,68,83,80,63,92]
cBio = [58,57,71,52,47,88,51,13,42,58,64,87,92,36,48,38,51,41,28,19] 
cPhy = [29,43,83,94,38,37,93,90,70,54,86,63,65,24,84,43,50,73,80,88]
cMath = [34,48,93,66,34,14,22,25,36,71,55,13,50,18,73,36,63,44,95,94]

# Exams
eChem = [46,52,24,73,80,83,70,98,96,48,83,48,93,94,36,39,75,46,27,47]
eBio = [97,41,51,68,90,18,25,72,27,50,80,23,89,84,34,36,35,80,25,38] 
ePhy = [73,31,98,65,51,44,19,18,43,75,61,35,70,68,31,14,33,23,16,19]
eMath = [45,31,94,67,68,65,41,52,22,76,70,10,81,46,87,89,48,53,62,31]

chen_avg_list = [52.615526315789474,62.97184210526316,38.42526315789473,57.97552631578948,57.939473684210526,64.44,78.65921052631579,63.19921052631579,76.26684210526315,59.80447368421052,81.95973684210526,63.811052631578946,86.88473684210527,73.22263157894736,28.901052631578946,49.822631578947366,71.67763157894737,67.51684210526315,30.616578947368424,70.71]
bio_avg_list = [92.69684210526316,66.12342105263157,52.83131578947368,65.26631578947368,57.60131578947369,36.66105263157895,39.30921052631579, 74.585,30.281052631578945,43.5921052631579,73.82105263157894,47.765,79.45421052631579,48.751578947368415,54.09368421052632,55.67736842105263,53.00394736842105,73.31447368421053,46.53947368421053,40.34657894736842]
phy_avg_list = [54.436052631578946,22.96815789473684,70.43605263157895,54.14736842105263,55.495789473684205,32.93973684210526,48.610789473684214,27.911052631578947,35.21368421052631,46.65789473684211,62.40105263157895,41.47763157894737,66.40921052631579,53.0821052631579,50.43526315789474,39.42131578947369,42.229473684210525,32.593947368421055,40.95894736842106,32.59105263157895]
math_avg_list = [52.25789473684211,55.014210526315786,67.67657894736841,64.92842105263158,42.805789473684214,58.27894736842105,40.74842105263158,59.27447368421052,33.46,65.79184210526316,64.21184210526316,21.635526315789477,73.21157894736842,47.68789473684211,64.06131578947368,63.77,38.77815789473684,48.65842105263158,49.982368421052634,40.63263157894737]
AvgScore = [63.00157894736842, 51.76940789473684, 57.342302631578946, 60.579407894736846, 53.46059210526316, 48.07993421052632, 51.831907894736844, 56.24243421052631, 43.8053947368421, 53.96157894736842, 70.59842105263158, 43.672302631578944, 76.48993421052631, 55.686052631578946, 49.37282894736842, 52.17282894736842, 51.422302631578944, 55.52092105263158, 42.02434210526316, 46.07006578947368]
GPA = [3.1500789473684208, 2.588470394736842, 2.8671151315789474, 3.0289703947368425, 2.673029605263158, 2.4039967105263162, 2.591595394736842, 2.812121710526316, 2.190269736842105, 2.6980789473684212, 3.529921052631579, 2.1836151315789474, 3.8244967105263155, 2.784302631578947, 2.468641447368421, 2.608641447368421, 2.571115131578947, 2.776046052631579, 2.101217105263158, 2.303503289473684]
grades = ['D', 'E', 'D', 'D', 'E', 'F', 'E', 'D', 'F', 'E', 'C', 'F', 'B', 'D', 'F', 'E', 'E', 'D', 'F', 'F']
status = ['Pass', 'Retake', 'Pass', 'Pass', 'Retake', 'Fail', 'Retake', 'Pass', 'Fail', 'Retake', 'Pass', 'Fail', 'Pass', 'Pass', 'Fail', 'Retake', 'Retake', 'Pass', 'Fail', 'Fail']

subjectsRes = {}
for students,studentId,qC,qB,qP,qM,chemavg,bioavg,phyavg,mathavg,avg,gpa,grade,sta in zip(studName,studId,qChem,qBio,qPhy,qMath,chem_avg_list,bio_avg_list,phy_avg_list,math_avg_list,AvgScore,GPA,grades,status):
    subjectsRes[students] = studentId,qC,qB,qP,qM,chemavg,bioavg,phyavg,mathavg,avg,gpa,grade,sta
    continue
print('quiz results:', subjectsRes)

# studentName1 = ('Bett James', 'Namukolo Abrams', 'Vera Abutu', 'Kwame Doga', 'Lukeman Ahmad', 'Akin Torey', 'Luke Brant', 'James Kenyata', 'Ngugi Tionga', 'Okoro Eze', 'Agatha Chiluba', 'Mangu Joseph', 'Longe Jethro', 'Florenc Giwa', 'Vetiva Lucent', 'Melody Braimoh', 'Victor Ihab', 'Mimi Trucker', 'Maguel Peter', 'Wellington Zuba')
# student Id1 = ('GR-0483', 'GR-0484', 'GR-0485', 'GR-0486', 'GR-0487', 'GR-0488', 'GR-0489', 'GR-0490', 'GR-0491', 'GR-0492', 'GR-0493', 'GR-0494', 'GR-0495', 'GR-0496', 'GR-0497', 'GR-0498', 'GR-0499', 'GR-0500', 'GR-0501', 'GR-0502',)
for students,studentId,hC,hB,hP,hM,chemavg,bioavg,phyavg,mathavg,avg,gpa,grade,sta in zip(studName1,studId1,hChem,hBio,hPhy,hMath,chem_avg_list,bio_avg_list,phy_avg_list,math_avg_list,AvgScore,GPA,grades,status):
    subjectsRes[students] = studentId,hC,hB,hP,hM,chemavg,bioavg,phyavg,mathavg,avg,gpa,grade,sta
    continue
print('home_work results:', subjectsRes)

# studentName2 = ('Bett James', 'Namukolo Abrams', 'Vera Abutu', 'Kwame Doga', 'Lukeman Ahmad', 'Akin Torey', 'Luke Brant', 'James Kenyata', 'Ngugi Tionga', 'Okoro Eze', 'Agatha Chiluba', 'Mangu Joseph', 'Longe Jethro', 'Florenc Giwa', 'Vetiva Lucent', 'Melody Braimoh', 'Victor Ihab', 'Mimi Trucker', 'Maguel Peter', 'Wellington Zuba')
# student Id2 = ('GR-0483', 'GR-0484', 'GR-0485', 'GR-0486', 'GR-0487', 'GR-0488', 'GR-0489', 'GR-0490', 'GR-0491', 'GR-0492', 'GR-0493', 'GR-0494', 'GR-0495', 'GR-0496', 'GR-0497', 'GR-0498', 'GR-0499', 'GR-0500', 'GR-0501', 'GR-0502',)
for students,studentId,cC,cB,cP,cM,chemavg,bioavg,phyavg,mathavg,avg,gpa,grade,sta in zip(studName2,studId2,cChem,cBio,cPhy,cMath,chem_avg_list,bio_avg_list,phy_avg_list,math_avg_list,AvgScore,GPA,grades,status):
    subjectsRes[students] = studentId,cC,cB,cP,cM,chemavg,bioavg,phyavg,mathavg,avg,gpa,grade,sta
    continue
print('class attendance results:', subjectsRes)

# studentName3 = ('Bett James', 'Namukolo Abrams', 'Vera Abutu', 'Kwame Doga', 'Lukeman Ahmad', 'Akin Torey', 'Luke Brant', 'James Kenyata', 'Ngugi Tionga', 'Okoro Eze', 'Agatha Chiluba', 'Mangu Joseph', 'Longe Jethro', 'Florenc Giwa', 'Vetiva Lucent', 'Melody Braimoh', 'Victor Ihab', 'Mimi Trucker', 'Maguel Peter', 'Wellington Zuba')
# student Id3 = ('GR-0483', 'GR-0484', 'GR-0485', 'GR-0486', 'GR-0487', 'GR-0488', 'GR-0489', 'GR-0490', 'GR-0491', 'GR-0492', 'GR-0493', 'GR-0494', 'GR-0495', 'GR-0496', 'GR-0497', 'GR-0498', 'GR-0499', 'GR-0500', 'GR-0501', 'GR-0502',)
for students,studentId,eC,eB,eP,eM,chemavg,bioavg,phyavg,mathavg,avg,gpa,grade,sta in zip(studName3,studId3,eChem,eBio,ePhy,eMath,chem_avg_list,bio_avg_list,phy_avg_list,math_avg_list,AvgScore,GPA,grades,status):
    subjectsRes[students] = studentId,eC,eB,eP,eM,chemavg,bioavg,phyavg,mathavg,avg,gpa,grade,sta
print('Exam results:', subjectsRes)


