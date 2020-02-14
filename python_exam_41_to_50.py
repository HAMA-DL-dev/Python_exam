#1
#make list with three movies
movie_rank=["Doctor strange","Split","Lucky"]
#2
#plus+ "Bat man"
movie_rank.append("Bat man")
#3
#add "Super man" between "Doctor strange" & "Split"
movie_rank.insert(1,"Bat man")
#4
#delete "lucky"
movie_rank.remove("Lucky")
del movie_rand[3]
#5
#delete "Split" & "Bat man"
movie_rank.remove("Split")
movie_rank.remove("Bat man")

del movie.rank[2:4]
#6
#make new list named lang, maked of lang1 and lang2
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
lang=lang1+lang2
print(lang)
#7
#what is max & min number in list named nums?
nums = [1, 2, 3, 4, 5, 6, 7]
print(max(nums))
print(min(nums))
#8
#what is total sum in list nums?
nums = [1, 2, 3, 4, 5]
all=0
for a in nums:
    all=all+a

print(all)

print(sum(nums))

#9
#what is the number of data in this list?
print(len(nums))

#10
#what is mean in this list?
nums = [1, 2, 3, 4, 5]
print(mean(nums))

print(sum(nums)/len(nums))
