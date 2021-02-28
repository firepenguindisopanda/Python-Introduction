#Layout of a QuadraticProbing Object
#Methods and variables the object has access to when instantiated.
class QuadraticProbing:
    def __init__(self, n):
        self.table = [None] * n
        self.n = n
    def insert(self, key, value):
        i = hash(key) % self.n
        misses = 0
        i_prime = (i + (misses*misses)) % self.n
        while self.table[i_prime] is not None:
            misses += 1
            i_prime = (i+(misses*misses)) % self.n
        self.table[i_prime] = (key, value)

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


#Layout of a Set Object
#Methods and variables the object has access to when instantiated.
class Set:
    def __init__(self, size):
        self.table = [[]] * size
        self.size = size
        return

    def add(self, key):
        i = hash(key) % self.size
        if self.table[i] is None:
            self.table[i].append(key)
        else:
            for l in self.table[i]:
                if l == key:
                    return
            self.table[i].append(key)
            return

    def contain(self, key):
        i = hash(key) % self.size
        if self.table[i] is None:
            return False
        else:
            for l in self.table[i]:
                if l == key:
                    return True
            return False

#Opens the text files to perform operations on the data
f_dns = open("dns.txt", "r")
f_queries = open("queries.txt", "r")
f_solutions = open("solutions.txt","w+")
f_blacklist = open("blacklist.txt", "r")

#Declare a dictionary to store the dns data read from the dns.txt file
dns_dictionary = {}
#Instantiates a QuadraticProbing object to store the data from dns_dictionary
real_dns = QuadraticProbing(25)
#Instantiates a Set Object to store the ip addresses
ip_addresses = Set(11)

#Inserts the data from the dns.txt file into HashTable using QuadraticProbing technique for cases of collision
for line in f_dns.readlines():
    dns_lines = line.split()
    dns_dictionary = dns_lines
    real_dns.insert(dns_dictionary[0], dns_dictionary[1])
        

#Adds the data from the blacklist.txt file to the Set Object ip_addresses 
for line in f_blacklist.readlines():
    blacklist_lines = line.strip()
    ip_addresses.add(blacklist_lines)

#stores the data from the queries.txt file in query_line
#pass query_line as a parameter for the search method that real_dns has acces to
#If query_search is None, Writes N to solutions.txt file
#check if the ip address that is in the ip address set
#If True, write Y to solutions.txt file else write N to file
for line in f_queries.readlines():
    query_line = line[0:-1]
    query_search = real_dns.search(query_line)
    if query_search is None:
        f_solutions.write("N\n")
        
    else:
        blacklist_search = ip_addresses.contain(query_search)
        if blacklist_search is True:
            f_solutions.write("Y\n")
            
        else:
            f_solutions.write("N\n")
            
        
f_dns.close()
f_queries.close()
f_solutions.close()
f_blacklist.close()



