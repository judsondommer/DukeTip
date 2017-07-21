from __future__ import print_function
import numpy as np
# This loads the u.item file from ml-100k, the folder with the survey data
movieNames = np.loadtxt('./ml-100k/u.item', delimiter='|', usecols=(0, 1),
                        dtype={'names': ('id', 'name'), 'formats': (np.int, 'S128')})

# This is combining the lists 'id' and 'name' from u.item into a dictionary
movieDict = dict(zip(movieNames['id'], movieNames['name']))

# Here we do what we did with u.item but with this file, u.data
movieData = np.loadtxt('./ml-100k/u.data', delimiter="\t", usecols=(0, 1, 2),
                       dtype={'names': ('userID', 'movieID', 'rating'), 'formats': (np.int, np.int, np.int)})

# print(movieData)
# print(movieNames)
# print(movieDict)

# This dictionary will hold our ratings before we sort
movieRatingTemp = {}

# This will add the ratings to movieRatingTemp, it also creates a list in the dictionary for every row in movieData
for row in movieData:
    if row['movieID'] in movieRatingTemp:
        movieRatingTemp[row['movieID']].append(row['rating'])
    else:
        movieRatingTemp[row['movieID']] = []
        movieRatingTemp[row['movieID']].append(row['rating'])
# print (movieRatingTemp)
movieRating = {}

# This dictionary keeps the amount of users who rated a movie
movieRatingCount = {}

# This for loop gets an average rating and the total number of ratings given
#  and stores them in their individual dictionaries
for key in movieRatingTemp:
    movieRating[key] = np.mean(movieRatingTemp[key])
    movieRatingCount[key] = len(movieRatingTemp[key])

# print (movieRating)
# print (movieRatingCount)

# This sorts the ratings stored in movieRatingTemp and stores them in movieRatingS
movieRatingS = sorted(movieRating.iteritems(), key=lambda (k, v): (v, k), reverse=True)

print ('Top Ten Movies:')

# This prints the top ten movies regardless of rating count
for i in range(10):
    id = movieRatingS[i][0]
    print (str(i + 1) + '. ' + str(movieDict[id]) + '(ID:' + str(id) + ') ' 
           + 'Rating: ' + str(movieRatingS[i][1]) + ' Count: ' + str(movieRatingCount[id]))


print ("\n\nTop Ten movies with at least 100 ratings:")
# These variable are set outside the while loop so their new value is saved 
# instead of be written over
moviesPrinted = 0
i = 0

# This loop finds the first 10 movies with a rating count over 100 in movieRatingS
# it increments i and movies printed to change rows and eventually end the while loop
while moviesPrinted < 10:
    id = movieRatingS[i][0]
    if movieRatingCount[id] >= 100:
        print(str(i + 1) + '. ' + str(movieDict[id]) + '(ID:' + str(id) + ') '
              + 'Rating: ' + str(movieRatingS[id]) + ' Count: ' + str(movieRatingCount[id]))
        moviesPrinted += 1
    i += 1

# These variables contain the number of movies and users +1
# so when used in a range, all movies and users will be selected
maxMovie = movieData['movieID'].max() + 1
maxUser = movieData['userID'].max() + 1

# This creates a matrix of all movies and users
userLikes = np.zeros((maxUser, maxMovie))

# This loop turns all the movies a user rating 4+ to 1
# in order to get a list of likes and dislikes
for row in movieData:
    if row['rating'] >= 4:
        userLikes[row['userID'], row['movieID']] = 1


def findSimilar(iLikeNp, userLikes):
    similarityAnd = iLikeNp * userLikes
    similarityAndSum = similarityAnd.sum(axis=1)
    userSimilarityOr = (iLikeNp + userLikes) - similarityAnd
    similarityOrSum = userSimilarityOr.sum(axis=1)

    userSimilarity = similarityAndSum / similarityOrSum
    while True:
        maxIndex = userSimilarity.argmax()
        newMovieMatrix = userLikes[maxIndex] - iLikeNp
        if 1 in newMovieMatrix:
            break
        else:
            userSimilarity[maxIndex] = 0
    print (userSimilarity[maxIndex])
    return maxIndex

def printMovie(id):
    print ('   -' + str(id) + ': ' + movieDict[id])

def processLikes(iLike):
    print('\n\nSince you like:')
    for i in iLike:
        printMovie(i)
    iLikeNp = np.zeros(maxMovie)
    print (iLikeNp)
    for movie in iLike:
        iLikeNp[movie] = 1
    user = findSimilar(iLikeNp, userLikes)
    print('\nYou might like: ')
    recLikes = np.argwhere(userLikes[user, :] == 1)
    recLikesFlat = recLikes.flatten()
    for i in recLikesFlat:
        if iLikeNp[i] == 0:
            printMovie(i)




testList = [1, 3]
processLikes(testList)

iLike = [655, 315, 66, 96, 194, 172]
processLikes(iLike)

# What if it's an exact match? We should return the next closest match
# Second sample case
# User Similiarity: 0.172413793103
iLike = [ 79,  96,  98, 168, 173, 176,194, 318, 357, 427, 603]
processLikes(iLike)

# What if we've seen all the movies they liked?
# Third sample case
# User Similiarity: 0.170731707317
iLike = [79,  96,  98, 168, 173, 176,194, 318, 357, 427, 603, 1]
processLikes(iLike)
