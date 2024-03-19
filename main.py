from time import time
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except IndexError:
            error += 1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput) / time_R
    return round(speed)

if __name__ == '__main__':
    while True:
        ck = input("Ready to test: yes/no: ")

        if ck == "yes": 
            test_sentences = ["Ra-ra-Rasputin Lover of the Russian queen They didn't quit, they wanted his head Ra-ra-Rasputin Russia's greatest love machine And so they shot him 'til he was dead","my name is WHAT my name is WHO my name is cheeka cheeka cheeka SLIM SHADYYY ", "Lyrics comin' at you at supersonic speed (J.J. Fad) Uh, summa-lumma, dooma-lumma, you assumin Im a human What I gotta do to get it through to you Im superhuman Im innovative and Im made of rubber so that anythin You say is ricochetin off of me, and itll glue to you and Im devastatin, more than ever demonstratin How to give a motherfuckin audience a feelin like its levitatin Never fadin, and I know the haters are forever waitin For the day that they can say I fell off, theyll be celebratin Cause I know the way to get em motivated I make elevatin music, you make elevator music","chipi chipi chapa chapa rubi rubi raba raba","It's the one and only D-O double G Big Snoop Dogg, it's the one and only The one and only, D-O double-double-double G ˀBig Snoop Dogg"]
            test_sentence = r.choice(test_sentences)
            print("*** Typing speed test ***")
            print(test_sentence)
            print()
            time_1 = time()
            test_input = input("Enter: ")
            time_2 = time()
            print('Speed :', speed_time(time_1, time_2, test_input), "words/sec")
            print("Errors :", mistake(test_sentence, test_input))
        elif ck == 'no':
            print("Thank you!")
            break
        else:
            print("Wrong input")