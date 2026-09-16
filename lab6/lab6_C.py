#C1
playlist = ["Black Diamond", "Soldiers Of The Wastelands", "Eagle Fly Fre"]
for num, song in enumerate(playlist, start = 1):
    print(num, song)

#C2
tasks = ["wake up", "shower", "brush teeth", "work", "eat", "sleep", "repeat"]
for num, task in enumerate(tasks, start = 1):
    print(f"Task{num}: {task}")

#C3
threshold = 3
for num, task in enumerate(tasks, start = 1):
    if num > threshold:
        print(f"{num}: {task}")

#C4
words = "some words"
for index in range(len(words)): #looping over index, getting char for each index by words[index]
    print(index, words[index]) 

for index, char in enumerate(words): #looping over char in words (enumerated) giving us both the index and the char directly without looking it up for each index
    print(index, char)


