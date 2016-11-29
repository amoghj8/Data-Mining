#! /usr/bin/python3

#Working with Collaborative Filtering

users = {"Angelica":{'Blues Traveler':3.5,'Broken Blues':2,'Norah Jones':4.5,
                     'Phoneix':5,'Slightly Stoopid':1.5,'The Strokes':2.5,'Vampire Weekend':2
                     },
         "Bill":{'Blues Traveler':2,'Broken Blues':3.5,'Deadman 5':4,'Phoneix':2,
                 'Slightly Stoopid':3.5,'Vampire Weekend':3
                     },
         "Chan":{'Blues Traveler':5,'Broken Blues':1,'Norah Jones':3,
                     'Phoneix':5,'Slightly Stoopid':1,'Deadman 5':1
                     },
         "Dan":{'Blues Traveler':3,'Broken Blues':4,'Deadman 5':4.5,
                     'Phoneix':3,'Slightly Stoopid':4.5,'The Strokes':4,'Vampire Weekend':2
                     },
         "Hailey":{'Deadman 5':1,'Broken Blues':4,'Norah Jones':4,
                    'The Strokes':4,'Vampire Weekend':1
                     },
         "Jordan":{'Deadman 5':4,'Broken Blues':4.5,'Norah Jones':5,
                     'Phoneix':5,'Slightly Stoopid':4.5,'The Strokes':4,'Vampire Weekend':4
                     },
         "Sam":{'Blues Traveler':5,'Broken Blues':2,'Norah Jones':3,
                     'Phoneix':5,'Slightly Stoopid':4,'The Strokes':5
                     },
         "Veronica":{'Blues Traveler':3,'Norah Jones':5,
                     'Phoneix':4,'Slightly Stoopid':2.5,'The Strokes':3
                     }
         }

#Printing one user ratings
print(users['Veronica'])

#Manhattan Distance
def Manhattan(user1,user2):
#user1 = users['Veronica']= {'Norah Jones': 5, 'Blues Traveler': 3, 'Slightly Stoopid': 2.5, 'Phoneix': 4, 'The Strokes': 3}
    distance = 0
    for key in user1:
        if key in user2:
            distance += abs(user1[key] - user2[key])
    return(distance)

Manhattan(users['Hailey'],users['Veronica'])
Manhattan(users['Hailey'],users['Jordan'])

#Computing nearest neighbours

def nearestneighbours(user,users):
    distances = []
    for username in users:
        if username != user:
            distance = Manhattan(users[username],users[user])
            distances.append((distance,username))
    distances.sort()
    return distances

print("\n")
print(nearestneighbours("Hailey",users))
print("\n")

def recommend(user,users):
    lists =[]
    nearest_neighbour = nearestneighbours(user,users)[0][1]
    neighbour_ratings = users[nearest_neighbour]
    user_ratings = users[user]
    for book in neighbour_ratings:
        if book not in user_ratings:
            lists.append((book,neighbour_ratings[book]))
    return lists

print(recommend("Hailey",users))

#Finding pearson coefficients
def pearsoncoefficient(user1,user2):
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x2 = 0
    sum_y2 = 0
    n = 0
    for key in users[user1]:
        if key in users[user2]:
            x = users[user1][key]
            y = users[user2][key]
            sum_x += x
            sum_y += y
            sum_xy += x*y
            sum_x2 += x**2
            sum_y2 += y**2
            n += 1
    denominator = (((sum_x2) - ((sum_x**2)/n))**0.5)*(((sum_y2) - ((sum_y**2)/n))**0.5)
    numerator = sum_xy -((sum_x*sum_y)/n)
    pearson_coefficient = numerator/denominator
    print(pearson_coefficient)

pearsoncoefficient('Angelica','Bill')
