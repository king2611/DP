import itertools
import time

Password = "b@2"
Max_Length = len(Password)

def brute_force_simulator(password, max_length):
    time.sleep(1)
    print("\nStarting BruteForce Attack...")
    time.sleep(0.3)
    time.sleep(2)

    unique_chars = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ',
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        '1','2','3','4','5','6','7','8','9','0',
        '!','@','#','$','%','^','&','*','(',')','_','-','=','+','[',']','{','}','|','/',',','.','<','>','?','"',"'",';',':'
    ]

    for length in range(1, max_length + 1):
        for fetchpass in itertools.product(unique_chars, repeat=length):
            brutepass = ''.join(fetchpass)
            print(f"Trying password matching: {brutepass}")
            
            if brutepass == password:
                with open("cracker.txt","w") as file:
                    file.write(f"Password: {brutepass}")
                print("\nYour Password has been Cracked and Stored in 'cracker.txt' file ...")
                time.sleep(1)
                print(f"Cracked Password: {brutepass}\n")
                return

    print("\nPassword not found!!\n")


brute_force_simulator(Password, Max_Length)
