P1 = dict (Age = 18, Gender = 'men' , Hair_color = 'black', Eye_color = 'brown', From_spb = 'yes', Hostel = 'no', Pets = 'yes', name =  'Sergey')
P2 = dict (Age = 18, Gender = 'men' , Hair_color = 'black', Eye_color = 'brown', From_spb = 'no', Hostel = 'yes', Pets = 'no', name = 'Emir')
P3 = dict (Age = 18, Gender = 'men' , Hair_color = 'light brown', Eye_color = 'green', From_spb = 'no', Hostel = 'no', Pets = 'yes', name = 'Dima_Milaev')
P4 = dict(Age = 18, Gender = 'women' , Hair_color = 'brown', Eye_color = 'green', From_spb = 'yes', Hostel = 'no', Pets = 'yes', name = 'Mariam')
P5 = dict(Age = 21, Gender = 'women' , Hair_color = 'brown', Eye_color = 'brown', From_spb = 'yes', Hostel = 'no', Pets = 'yes', name = 'Masha')
P6 = dict (Age = 18, Gender = 'men' , Hair_color = 'black', Eye_color = 'brown', From_spb= 'no', Hostel = 'no', Pets = 'yes', name = 'Ruslan')
p1 = [18, 'men','black','brown','yes','no','yes','Sergey']
'''
for i in P1:
    print(i, P1.get(i)) 
'''
Age = int(input('How old are you? (17,18,19,20,21) '))
Gender = str(input('What is your gender? (men/women) '))
Hair_color = str(input('What color is your hair? (blue, green, black, gray, red hair, light brown, brown, white, colorful) '))
Eye_color = str(input('What colour are your eyes? (black, brown, green, gray, blue, red, white) '))
From_spb = str(input('Are you from spb? (yes/no) '))
Hostel = str(input('Do you live in a hostel? (hostel-общежитие yes/no) '))
Pets = str(input('Do you have a pet? (yes/no) '))
s = (P1, P2, P3, P4, P5, P6)
S = [p1]
ans = []
ans.append([Age]) 
ans.append([Gender])  
ans.append([Hair_color]) 
ans.append([Eye_color]) 
ans.append([From_spb])
ans.append([Hostel]) 
ans.append([Pets])

for i in range(len(p1)-1) :
    k = True
    for j in S:
        if j[i] == ans[i]:
            k = True
        else:
            k = False
    if k:
                print (j[-1])