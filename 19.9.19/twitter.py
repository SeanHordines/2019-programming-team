import operator

tags = {}

for i in range(int(input())):
    tweet = input().lower()
    for j in range(tweet.count("#")):
        start = tweet.find("#")+1

        end = start
        while(end < len(tweet) and tweet[end] != " "):
            end += 1

        #print(tweet[start:end])
        tag = tweet[start:end]
        if tag in tags:
            tags[tag] = tags[tag]+1
        else:
            tags[tag] = 1
        tweet = tweet[end:]

while(len(tags) > 0):
    maxV = 0
    maxK = ""
    for tag in tags.keys():
        if tags[tag] > maxV:
            maxV = tags[tag]
            maxK = tag
    print(maxV, maxK)
    tags.pop(maxK)    
