#1 (adicionando o atributo interressado em)
users = [
    # m = male; n = none; b = both; f = female
    {"id": 0, "name": "Hero","gender":"m","age":18, 'interest in': 'n'},    
    {"id": 1, "name": "Dunn","gender":"m","age":20, 'interest in': 'b'},    
    {"id": 2, "name": "Sue","gender":"f","age":14, 'interest in': 'm'},    
    {"id": 3, "name": "Chi","gender":"f","age":16, 'interest in': 'm'},      
    {"id": 4, "name": "Thor","gender":"m","age":18, 'interest in': 'f'},      
    {"id": 5, "name": "Clive","gender":"m","age":24, 'interest in': 'f'},     
    {"id": 6, "name": "Hicks","gender":"m","age":22, 'interest in': 'f'},     
    {"id": 7, "name": "Devin","gender":"m","age":17, 'interest in': 'm'},       
    {"id": 8, "name": "Kate","gender":"f","age":19, 'interest in': 'm'},        
    {"id": 9, "name": "Klein","gender":"m","age":20, 'interest in': 'f'},    
]

#2 (Recomendando usurios por id)
def find_user_by_interest (User): #Da sugestoes de amizade pelo atributo 'interest in'
    return [
        user['id']
        for user in users
        if user['id'] != User['id'] and (User['interest in'] == user['gender'] or User['interest in'] == 'b')
    ]

#print(find_user_by_interest(users[1]))

#3 (Recomendando usurios por id com interesses em comum) 
def common_interest (user1, user2): #função verifica se os usuarios tem interresse entre si
    if user1['interest in'] == user2['gender'] or user1['interest in'] == 'b':
        if user2['interest in'] == user1['gender'] or user2['interest in'] == 'b':
            return True
    return False

def find_user_by_common_interest (User):
    return [
        user['id']
        for user in users
        if common_interest(User, user) and User['id'] != user['id']
    ]

print(find_user_by_common_interest(users[1]))  