#a לרשימת זוכי האוסקרWatson Emma הוסף את השחקנית
from main import print_hi

oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone",
                 "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
oscar_winners.add("Emma Watson")
print("add Emma Watson to the list:", oscar_winners)

#b
oscar_winners_copy = oscar_winners.copy()
oscar_winners_copy.remove("Meryl Streep")
print("Removing actress Meryl Streep:", oscar_winners_copy)

print("Clean all members in the list:",oscar_winners_copy.clear())


#c
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
#תשובה ראשונה
Titanic_and_Dark_Knight_common_actors=titanic_actors.intersection(dark_knight_actors)
print("Titanic and the Dark Knight common actors:",Titanic_and_Dark_Knight_common_actors)
#תשובה שנייה
Titanic_and_Dark_Knight_common_actors=set(titanic_actors) & set(dark_knight_actors)
print("Titanic and the Dark Knight common actors:",Titanic_and_Dark_Knight_common_actors)
#d
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo",
                   "Chris Hemsworth", "Jeremy Renner"}

iron_man_and_avengers_common_actors=iron_man_actors.isdisjoint(avengers_actors)
print("iron man and avengers common actors:",iron_man_and_avengers_common_actors)
#e
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}

all_win_an_oscar= actor_list.issuperset(oscar_winners)
print("all win an oscar?", all_win_an_oscar)

#f
all_the_actors_who_appeared_in_The_Avengers=actor_list.issubset(avengers_actors)
print("actor list includes all the actors who appeared in The Avengers?",all_the_actors_who_appeared_in_The_Avengers)

#g
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}
print("Remove a player randomly:",movie_cast.pop())
print(movie_cast)

#h
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}
print("Remove  Matt Damon player:", movie_cast.remove("Matt Damon"))
print(movie_cast)

#i
didnt_win_Oscar = titanic_actors.difference(oscar_winners)
print("Actors who played in Titanic didn't win an Oscar?",didnt_win_Oscar)

#j
only_appeared_in_Titanic_or_The_Dark_Knigh=titanic_actors.symmetric_difference(dark_knight_actors)
print("Actors who only appeared in Titanic or The Dark Knight?",only_appeared_in_Titanic_or_The_Dark_Knigh)

#k
oscar_winners.update({"Cate Blanchett" , "Daniel Day-Lewis"})
print("Update and add Cate Blanchett  and Daniel Day-Lewis:",oscar_winners)

#i אחד את רשימת השחקנים של טיטניק והאביר האפל כדי לראות את שמות כל השחקנים
#תשובה ראשונה
together= set(titanic_actors) ^ set(dark_knight_actors)
print("Titanic and the Dark Knight together:",together)
#תשובה שנייה
together= titanic_actors.union(dark_knight_actors)
print("Titanic and the Dark Knight together:",together)
