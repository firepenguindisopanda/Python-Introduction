#Layout of a QuadraticProbing Object
#Methods and variables the object has access to when instantiated.
class QuadraticProbing:
    def __init__(self, n):
        self.table = [None] * n
        self.n = n
        
    #This method uses QuadraticProbing algorithm to insert a key, value pair into a hash table and resolves collisions.    
    #Uses the function hash() on the key variable 
    def insert(self, key, value):
        i = hash(key) % self.n
        misses = 0
        i_prime = (i + (misses*misses)) % self.n
        while self.table[i_prime] is not None:
            misses += 1
            i_prime = (i+(misses*misses)) % self.n
        self.table[i_prime] = (key, value)
        
    #Returns the value from the hashtable that corresponds to the key variable passed in the parameter
    #Return None if the key doesn't exist
    def search(self, key):
        i = hash(key) % self.n
        misses = 0
        i_prime = (i + (misses*misses)) %self.n
        while self.table[i_prime] is not None:
            k_prime, v_prime = self.table[i_prime]
            if k_prime == key:
                return v_prime
            misses += 1
            i_prime = (i + (misses*misses)) % self.n
        return None
        
    #Removes the value of the corresponding key
    def delete(self, key):
        i = hash(key) % self.n
        misses = 0
        i_prime = (i + (misses*misses)) % self.n
        
        while self.table[i_prime] is not None:
            k_prime, v_prime = self.table[i_prime]
            if k_prime == key:
                self.table[i_prime] = None
                prev_i = i_prime
                curr = misses + 1
                i_prime = (i + (curr*curr)) % self.n
                while self.table[prev_i] is not None:
                    self.table[prev_i] = self.table[i_prime]
                    prev_i = i_prime
                    curr += 1
                    i_prime = (i + (curr*curr)) % self.n
            misses += 1
            i_prime = (i + (curr*curr)) % self.n
                

#Beginning of setting variables
t = 500 #assume that T is no longer than 500 characters each
p = 11 #assume that p is no longer than 10 characters each
count = 0
a = 0
new_word = ""
h = 0
hv = 0
ftpr = open("patterns.txt", "r")
ftpr2 = open("dna.txt", "r")
f = open("solution.txt", "w+")
temporary=""
tempdictionary = {}
shval = 0
patterns_count = 0
dna_count = 0



lines = [line for line in ftpr.readlines()]

dictionary_object = {}
htble = {}
htble2 = QuadraticProbing(p)

dnatxt = ftpr2.read()
dnatxtlength = len(dnatxt)

patterns = [None] * len(lines)
x = len(patterns)
los = x - 1
over_limit = 0
over_x = 0
dtl = ()
xl = ()
#End of setting variables


if dnatxtlength > 500:
    over_limit = dnatxtlength - 500
    over_limit = dnatxtlength - over_limit
    for ro in range(over_limit):
        dtl[ro] = dnatxtlength[ro]

if x > 10 :
    over_x = x - 10
    over_x = x - over_x
    for px in range(over_x):
        xl[px] = patterns[px]

for l in range(len(lines)):
    wrd = lines[l]
    wrd = wrd.strip()
    patterns[l] = wrd



for w in range(x):
    new_word = patterns[w]
    for i in new_word:
        h += ord(i)
    dictionary_object[new_word] = h
    h = 0


for i in dictionary_object:
    htble2.insert(i, dictionary_object[i])


for r in patterns:
    for h in r:
            shval += ord(h)
    #part_of_string = r
    for i in range(dnatxtlength-3):
        string = dnatxt[i:i+los]
        
        if htble2.search(string) == shval:
            temporary=temporary+str(i)+" "
    
    f.write(temporary)
    f.write("\n")
    temporary = ""
    shval = 0
            
    
f.close()
ftpr.close()
ftpr2.close()





