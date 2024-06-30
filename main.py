# This is a Brute-Force Password Cracking Script in Python
import hashlib
import itertools
import time

#Function to generate an md5 hash
#Input: a string that contains the plaintext to hash
#Returns: a string of the md5 hash
def generate_md5(hash: str) -> str:
    result = hashlib.md5(hash.encode(encoding='UTF-8'))
    return result.hexdigest()

#Function to output results at completion
#Input: a list of dictionaries with keys 'hash', 'plaintext', and 'time'
#Returns: none
def print_results(results):
    print("-----------------------------------------------------------")
    print("RESULTS:\n")
    for r in results:
        print("Hash:", r[0]['hash'])
        print("Plaintext:", r[0]['plaintext'])
        print("Time Taken (s):", r[0]['time'])
        print("\n")
    print("-----------------------------------------------------------")

#Main
if __name__ == '__main__':
    #Create a character list of all possible chars
    all_characters_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@'
    all_characters = list(all_characters_str)

    #Open "hashes.txt" and read in hashes into list "hashes"
    hashes = []
    file = open("hashes.txt", "r")
    data = file.readlines()
    for line in data:
        hashes.append(line.rstrip())

    #Starts the time counter
    startTime = time.perf_counter()

    #Initializes the cracked_hashes list
    cracked_hashes = []

    #Brute-force attack
    for x in range(9):
        #Uses itertools to create all possible permutations with repetition
        permutation_iterator = itertools.product(all_characters, repeat=x)
        for c in permutation_iterator:
            #Converts result into a plaintext word
            c_list = list(c)
            plaintext = "".join(c_list)
            #Generates the hash for that plaintext word
            hash = generate_md5(plaintext)
            #Compares the hash to the hashes in "hashes" list
            #If there is a match, print out and append data to cracked_hashes
            for h in hashes:
                if hash == h:
                    #calculate time passed
                    end = time.perf_counter()
                    s = (end-startTime)
                    print("CRACKED HASH: " + plaintext + " = " + hash + "\t" + str(s))
                    #save data to cracked_hashes
                    data = [{"hash": hash, "plaintext": plaintext, "time": s}]
                    cracked_hashes.append(data)
    print_results(cracked_hashes)