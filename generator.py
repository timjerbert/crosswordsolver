from itertools import combinations

def getPossibleLetterCombinations():
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    consonantList = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    vowelList = ["a","e","i","o","u"]
    numLetters = 20
    minVowels = 3
    maxVowels = 5

    notPresentCombinations = [] #should be a 2d matrix by the end

    for numVowelsNotPresent in range(0,maxVowels-minVowels+1): #this is iterated inversely, basically getting the potential combinations of hidden numbers. Should be faster than the alternative
        combinationVowelsNotPresent = combinations(vowelList,numVowelsNotPresent)
        for numConsonantsNotPresent in range(numVowelsNotPresent, numConsonantsNotPresent+1): #If there is 1 vowel not in hidden, there will be 5 consonants in hidden
            combinationConsonantsNotPresent = combinations(consonantList,numConsonantsNotPresent)
            notPresentListForThisEntry = combinationVowelsNotPresent
            notPresentListForThisEntry.concat(combinationConsonantsNotPresent)
            notPresentCombinations.push(notPresentListForThisEntry)
    print("Possible letter combinations not in hidden are:", notPresentCombinations)



def main():
    minLetterMatches = 15
    minCompletedWords = 2
    maxCompletedWords = 12

    getPossibleLetterCombinations()

    wordBank = ["fair","aqua","resembles","young","amid","economic","cage","need","carriage","mug","eagle","empire","realism","poem","edit","arise","ebb","ink","inn","absent"]