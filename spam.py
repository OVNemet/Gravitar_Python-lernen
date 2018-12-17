from random import shuffle

liste = "amazing excited gorgeous vibrant blazing fast stunning bold biggest fastest tremendous greatest best \
        fantastic phenomenal delightful ambitious exciting staggering outstanding smarter massive incredible \
        spectacular super excited super cool biggest magical revolutionary intuitive profound beautiful \
        jaw-dropping".upper().split()
shuffle(liste)

for strophe in range(5):
    for n in range(2):
        for i in range(4):
            print("SPAM ", end='')
        print()
    print("{} SPAM, {} SPAM".format(liste.pop(), liste.pop()) )
    print()