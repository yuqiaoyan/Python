from structshape import structshape

#tuples are IMMUTABLE, you can splice and index them like strings

#PATTERN DSU DECORATE, SORT, UNDECORATE - SORTING WORDS BY LENGTH EXAMPLE
def sort_by_length(words):
    t= []

    #DECORATE the tuple of words with the length of the word as the KEY for SORTING
    for word in words:
        t.append((len(word),word))

    #SORT the list of words by its length. reverse=true will lead to decreasing order
    t.sort(reverse=true)

    #UNDECORATE by building a list of new words in decreasing order
    res=[]
    for length, word in t:
        res.append(word)
    return res

#USE TUPLES to create functions that will take a MULTIPLE arguments
def sumall(*args):
    sumA = 0
    for num in args:
        sumA += num
    return sumA

def main():
    #if the argument to a tuple is a (string, list or tuple), the result is a tuple w/ elements of the sequence
    t = tuple('lupins')
    print t
    #('l', 'u', 'p', 'i', 'n', 's')

    a="hi"
    b='pam'
    #tuple assignment is very elegant - SWAP EXAMPLE. ALL EXPRESSIONS ON RIGHT ARE EVALUATED BEFORE ASSIGNMENT
    a, b = b, a
    print a, b

    #USE SPLIT AND TUPLEs together for getting data. tuple assignment is GREAT for getting KEYS from list of data
    addr = 'monty@python.org'
    uname, domain = addr.split('@')

    print "Example of MULTIPLE ARGUMENTS for a function: " + str(sumall(1,2,3,4))

    #ENUMERATE will give you the index of the for loop
    for index, element in enumerate('abc'):
        print "Get the Index of a LIST with ENUMERATE " + str(index), str(element)

    print structshape(t)


if __name__ == '__main__':
    main()
