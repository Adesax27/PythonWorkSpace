# # CHALLENGE 1...
'''
1. create a function with name "online_count"
   calling this function prints out the total people online
   the function should take one parameter, which will be the dictionary name.
   E.g:
   online_count(statuses)
   output: 3 people online
'''

Clients = ('Alice', 'Eve', 'Obaro')
status = ('online', 'online', 'online')

online_count = {}

for clients, sta in zip(Clients, status):
    online_count[clients] = {'status':sta}
    
    #print(online_count)
    
Clients = []
status = []
for i in online_count:
    if i >= str(3):
        status.append('3 people online')
        
status
    
'''
2. create a function with name "offline_count"
   calling this function prints out the total people offline
   the function should take one parameter, which will be the dictionary name.
   E.g:
   offline_count(statuses)
   output: 2 people offline
'''
Clients = ('Bob', 'Mike')
status = ('offline', 'offline')

offline_count = {}

for clients, sta in zip(Clients, status):
    offline_count[clients] = {'status':sta}
    
    #print(online_count)
    
Clients = []
status = []
for i in offline_count:
    if i >= str(2):
        status.append('2 people offline')
        
status
    
'''
3. create a function with name "status_check" that check if a person is online or offline,
   the function should take one parameter, which will be the person name.
   E.g:
   status_check("Alice")
   output: online
'''

Clients = ('Alice', 'Bob', 'Eve', ' Mike', 'Obaro')
status = ('online', 'offline', 'online', 'offline', 'online')

status_check = {}
for clients, sta in zip(Clients, status):
    status_check[clients] = {'status':sta}
    
#print(status_check)
status_check['Alice']

'''
4. create a function with name "online_list"
   calling this function prints the people online line by line
   the function should take one parameter, which will be the dictionary name.
   E.g:
   online_list(statuses)
   output: Alice
           Eve
           Obaro
'''
Clients = ('Alice', 'Eve',  'Obaro')
status = ('online', 'online', 'online')

online_ListRes = {}
for clients, sta in zip(Clients, status):
    online_ListRes[clients] = sta
    continue
print('output:', online_ListRes)

'''
5. create a function with name "offline_list"
   calling this function prints the people offline line by line
   the function should take one parameter, which will be the dictionary name.
   E.g:
   offline_list(statuses)
   output: Bob
           Mike
'''

Clients = ('Bob', ' Mike',)
status = ('offline', 'offline')
offline_ListRes = {}
for clients, sta in zip(Clients, status):
    offline_ListRes[clients] = sta
    continue
print('output:', offline_ListRes)

