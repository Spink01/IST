minutes = 0
import time

def end():
    time.sleep(3)
    print(' ')
    print('the week is finally over')
    print(' ')
    print(' ')
    print('Thanks for Playing!')

def badend():
    print(' ')
    print("you cry yourself to sleep, knowing you're going to fail")
    end()

def day5():
    print(' ')
    time.sleep(5)
    print("It's finally friday. you know the drill by now.")
    print('you have to plan a group project today')
    print(' ')
    choice1P = input('"go to school" or "stay in bed"? ')
    print(' ')

    if choice1P == 'stay in bed':
        print('you close your eyes and head back into a deep sleep.')
        end()

    if choice1P == 'go to school':
        print('you get out of bed, get dressed and go to school')
        print('it can be anything, by the way.')
        print("as you join your group, you begin throwing out ideas.")
        print(' ')
        print('"we should make a model earth." one kid said.')
        print('you imagine a globe. because that literally what this is.')
        print(' ')
        choice2P = input('"accept" the idea, or "deny" it. ')
        print(' ')

        if choice2P == 'accept':
            print('you spent the project literally making a globe')
            print('you failed the project')
            badend()

        if choice2P == 'deny':
            print('you deny the horrible idea. good.')
            print("the group puts up a new idea")
            print(' ')
            print('"how about we build some code in python?" ')
            choice3P = input('you can "accept" or "deny" ')
            print(' ')

            if choice3P == 'deny':
                print('after denying that idea they spiral back to the model earth.')
                print('you all fail because that idea sucks')
                badend()

            if choice3P == 'accept':
                print('you accept and get to working.')
                print('everyone eventually hits a wall, wondering what the code will do.')
                print(' ')
                print('you can offer up 2 ideas:')
                choice4P = input('"choose your own adventure" or "pokemon battles" ')
                print(' ')

                if choice4P == 'pokemon battles':
                    print('your group tries to rack their head around the pokemon damage formula')
                    print("they can't understand how to implement it into python.")
                    print(' ')
                    print('you fail tragically')
                    badend()

                if choice4P == 'choose your own adventure':
                    print('your team writes random stories and stitches them together with if statements')
                    print('the job is really easy since you need two functions at most.')
                    print(' ')
                    print('you submit the assignment.')
                    print('the teacher suprisingly liked the idea and passes your group.')
                    print('when you get home, you breathe a sigh of relief and head to bed.')
                    print("you're extra happy since you got a good grade.")
                    end()

def day4():
    time.sleep(5)
    print(' ')
    print(' ')
    print('today is a new day, not much going on this time around either.')
    print('like any other day, you have a choice:')
    print(' ')
    choice1B = input('"stay in bed" or "go to school"? ')
    print(' ')

    if choice1B == 'stay in bed':
        print('you close your eyes again and plop right back to sleep')
        day5()

    if choice1B == 'go to school':
        print('you get up, get dressed, have breakfast, and head to school')
        print(' ')
        print('flash cut to lunch period (told you today was uneventful)')
        print("while your eating a meal from home, a few kids approach you")
        print('"hey kid." they say. "you wanna get rich quick?"')
        print('the boys start yapping about a cryptocurreny some youtuber promoted')
        print(' ')
        choice2B = input('are you gonna "join them" or "ignore them" ')
        print(' ')
            

        if choice2B == 'join them':
            print('after school, you decide to get into the crypto those kids mentioned.')
            print('long story short, you spend the night becoming broke')
            print("don't do crypto. especially if famous people back it publically")
            print('you cry yourself to sleep knowing you just lost your allowance savings')
            day5()

        if choice2B == 'ignore them':
            print("luckily, you've heard the horror stories of investing in crypto")
            print('you shoo the kids away')
            print(' ')
            print('another kid appears right after. they look older than the last few.')
            print('"hey kid, you want a puff (out of a vape)?" He says.')
            print(' ')
            choice3B = input('you can say "yes" or "no" ')
            print(' ')

            if choice3B == 'yes':
                print('you take a puff out of the vape. an hour later, you collapse.')
                print('you wake up in the hospital later that day')
                print('turns out, the tip of that vape was laced... with fentynal.')
                print('you got grounded for this. all you can do is go home')
                print(' ')
                print('you go to bed, vowing to never get involved with drugs ever again')
                day5()

            if choice3B == 'no':
                print('you remember that doing drugs is bad and shoo the kid away.')
                print(' ')
                print('lunch period is almost over, but like clockwork, another kid.')
                print('you know this kid well, he like anime... the debaucherous kind.')
                print("worst of all, he's holding a laptop.")
                print(' ')
                choice4B = input('you gonna "escape" or "hear him out"? ')
                print(' ')

                if choice4B == 'hear him out':
                    print('you agree to listen to the kid and he opens up a school computer in his hands.')
                    print("somehow, he's gotten past the school's content moderation.")
                    print('even worse, he left the volume on max brfore he approached you.')
                    print(' ')
                    print('the entire lunchroom hears some very disturbing phrases being uttered.')
                    print('the faculty rush over to you and the anime kid.')
                    print("you told the faculty you didn't do it, but you're still guilty by association")
                    print(' ')
                    print('you spent the rest of the day in an office...')
                    print('and the afternoon, in detention.')
                    print('when you finally get home, you hop right back into bed.')
                    day5()

                if choice4B == 'escape':
                    print('you walk away from the kid as he opens his laptop.')
                    print('the entire lunchroom hears some very disturbing phrases being uttered.')
                    print('luckily, you were nowhere near him. and he gets in trouble.')
                    print(' ')
                    time.sleep(3)
                    print('the lunch bell rings and the rest of the day is irrelevant')
                    print('when you head home, you make you way to your bed.')
                    print("you fall asleep, knowing that you didn't get involved in something shaddy.")
                    day5()

def day3():
    
    time.sleep(5)
    pushup = 0
    
    print(' ')
    print(' ')
    print("today is your physical exam (yep, 2 exams in one week)")
    print("you'll be doing the fitness gram pushup test")
    choice3P = input('are you "going to school" or "staying in bed"? ')
    print(' ')

    if choice3P == 'staying in bed':
        print('why are these tests still around anyway?')
        print('you close your eyes and fall back asleep')
        day4()
        
    if choice3P == 'going to school':
        print('you get out of bed, brush your teeth, and make sure you have everything ready before leaving.')
        print('you make your way inside of the school.')
        print('first period is gym. you walk in and hear the speakers a little too loudly.')
        print(' ')
        print("We'll now begin the push up section. Ready? begin.")
        print("normally, you'd have a timer to pace yourself with,")
        print("but, inflated numbers raise the school's budget, so you'll stop when you drop")
        print(' ')
        while True:
            
            push = input('down (you can either push "up" or "stop") ')
            
            if push == 'up':
                pushup += 1
                print('up', pushup)

            if push == 'stop':
                print('you decide to stop')
                print(' ')
                break
            
        print('the test is over, time to see the results.')
        if pushup == 0:
            print("you didn't try, so they're gonna make you do it again some other time")

        if pushup > 1 and pushup < 11:
            print('you got a low number. Oh well.')

        if pushup > 10 and pushup < 21:
            print('you got an average score. Cool.')

        if pushup > 20 and pushup < 31:
            print('you managed to beat the athletic kids. Weird.')

        if pushup > 30 and pushup < 41:
            print('you got the top of the class. Good Job.')

        if pushup > 40:
            print('no one outside of your class believes that you actually got so high.')
            print('when the school submits this data later, an investigation will be conducted on the school')
            print('congratulations, you just indirectly exposed schoolwide curruption')
    
        print(' ')
        print('the rest of the day is irrelevant to this story.')
        print('you head back home to your bed for some nice, long, shuteye.')
        print('you close your eyes and drift into a nice, long sleep...')
        day4()

def results():
    global minutes, choice2L, choice3L
    print(' ')
    print('you finally arive at school, after that rough morning, its all over.')
    print('you make your way to the door')
    print(' ')

    if minutes == 30:
        print('you got to school just in time')
        print('right as the faculty were going to enter, they let you in.')
        print('knowing that you saved a poor kitty fills you with joy.')
        print('the boy is safe too, he just got a few bruises when he fell.')
        print('having had the supplies to study did help you out too.')
        print(' ')
        print('today is a good day.')

    if minutes > 30:
        print('you did not make it on time.')
        print('the school doors are closed without you inside.')
        print("it doesn't really matter how you got here, but all that effort is gone now")
        print(' ')
        print("today couldn't get any worse")

    if minutes < 30:
        print("you managed to speed over to school pretty fast,")
        print("let's just hope everything is set")

        if choice2L == 'keep walking' or choice3L == 'head out':
            print('somehow, you unkowingly left your lunch, ID, and pencils.')
            print("you couldn't learn or eat at all today")
            print(' ')
            print('not a good day for you at all')
          
        if choice2L == 'going back' and choice3L == 'check the bag':
            print('since you came fully prepared for class, you managed to learn well today.')
            print(' ')
            print('everythings going to be just fine')
    
    print(' ')        
    print('the day ends and you head back home to your bed.')
    print('you close your eyes and you fall into a deep sleep')
    day3()

def tree():
    global minutes
    print(' ')
    print('as you make your way to school, you see a cat stuck in a tree.')
    print('saving the cat is going to cost you a good 15 minutes')
    print(' ')
    choice4L = input('will you "leave the cat" or "save the cat"? ')

    if choice4L == 'leave the cat':
        
        print('it probably likes being there, no reason to be be scared for it.')
        print('you continue on your way to school.')
        results()

    elif choice4L == 'save the cat':
        minutes += 15
        print(' ')
        print('while getting the cat out a the tree, you see a kid in the tree as well.')
        print('"c-can you help me too?" the kid says fearfully.')
        print("you take a look at the kid and you realize he's big, and maybe heavy.")
        print('you could probably call the fire department for this')
        print('or you could help him for 10 minutes.')
        print(' ')
        choice5L = input('so, "save the child" or "call for help"? ')

        if choice5L == 'save the child':
            minutes += 10
            print('before you could even react, the boy fell out of the tree.')
            print("he has a few small bruises but they aren't your problem anymore.")
            print('you head to school')
            results()
              

        if choice5L == 'call for help':
            minutes += 20
            print('you call the nonemergency fire department number and let them know of the issue.')
            print("they tell you they're on their way and to stay put")
            print('you wound up staying there 20 minutes for help to arrive')
            print('after a long while of waiting and explaining, you head to school.')
            results()

def day2():
    global minutes, choice2L, choice3L
    time.sleep(5)
    print(' ')
    print(' ')
    print('its a new school day, with no new exams. just basic lessons.')
    print('you look at that time and its... 8:30 AM')
    print("you should've been at school by now.")
    print('the school stops letting people into the school in 30 minutes')
    print(' ')
    choice1L = input('are you gonna "stay in bed", or "go to school"? ')

    if choice1L == 'stay in bed':
        print("school isn't really that important today anyway.")
        print('you close your eyes and drift right back to sleep')
        day3()

    elif choice1L == 'go to school':
        print('you rush out of bed, brush your teeth, and hurry out of the house')
        print('after walking a block, you realize that your back feels a little too light.')
        print("you realize you left your whole backpack.")
        print("if you go back now, you'll lose 10 minutes on your way to school.")
        print(' ')
        choice2L = input('are you "going back" for your backpack or will you "keep walking"? ')
        print(' ')

        if choice2L == 'keep walking':
            print("even if you show up grossly unprepared for class, that's better than not showing up.")
            print('right?')
            tree()
              
        if choice2L == 'going back':
            minutes += 10
            print('you rush back home and get your bag.')
            print("just in case, you should check your bag. it'll take 10 minutes.")
            choice3L = input('will you "check the bag" or "head out"? ')

            if choice3L == 'head out':
                print("you head out without checking you bag. what's the worst that can happen?")
                tree()

            if choice3L == 'check the bag':
                minutes += 5
                print(' ')
                print('you check the bag and you noticed that you forgot your lunch, ID, and pencils')
                print('luckily, you realized that, and you got everything quickly.')
                print('you head back outside on your way to school')
                tree()

def test():
    score = 0
    print("question 1: what is 9 + 10? ")
    choice3T = input('"a": 21  "b": 19   "c": 100 or   "d": 1 ')

    if choice3T == "b":
        print("you think to yourself that your answer is right")
        score = score + 1
    else:
        print('you think that your answer is wrong')

    print("next question: If john has 10 apples and mary has 3 apples, what is the mass of the sun? ")
    print(' ')
    
    choice4T = input('"a": Approximately 2 × 10^30 kg   "b": 7 apples    "C": 1.8987×10^27 kg   or "d": 13 apples ')
    
    if choice4T == "a":
        print('you think your answer is right')
        score = score + 1
    else:
        print('you think that your answer is wrong')
    print(' ')
    print('the test is over. the rest of the day goes by normal and you go home')
    print('the next day, you get your test back, you open it and look inside')

    if score == 2:
        print('you aced the exam. Nice!')
        print(' ')
        print('Good Job!')

    elif score == 1:
        print("you got 1 right. not bad at all.")
        print(' ')
        print('oh well...')

    elif score == 0:
        print("you got 0%. better luck next time I guess")
        print(' ')
        print('too bad...')

    print(' ')
    print(' ')
    print('you got back home and get some nice, long rest')
    day2()

      

print('this game is played in lowercase words')
print(' ')
print("you wake up on a warm, spring day.")
print("you have an quiz today, but you don't feel like getting out of bed.")
choice1T= input('do you "go to school" or "stay in bed?" ')


if choice1T == 'stay in bed':
      print("you weren't prepared for that exam anyway")
      print('you close your eyes and you head right back to sleep')
      day2()
            
if choice1T == 'go to school':
      print('you get out of bed, brush your teeth, and go to school')
      print('on the way, the school bully notices you and goes charging at you')
      print(' ')
      choice2T = input('do you "run away" or "fight" ')

      if choice2T == 'run away':
          print("you run away as fast as you can, reaching the school before he caught up to you.")
          print("the quiz is in 1st period. just great.")
          print("you make your way to your seat and start the quiz")
          print(" ")
          test()

      if choice2T == 'fight':
          print('you decided to fight, but the bully is twice your size')
          print('since you stood up to him, he wants to hurt you badly')
          print("he pulls out a bat from his bag and you fall to the ground")
          print("after a few hours, you wake up in the hospital.")
          print("luckily you survived, but you're not making it to that exam.")
          print(' ')
          print("by the time you get out of the hospital, the exam is over, and you go to bed")
          print(' ')
          print(' ')
          day2()


