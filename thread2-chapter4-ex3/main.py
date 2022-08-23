import re

def catch_thief(queue):
    thiefs_catched = 0
    thiefs_being_catch = {}

    for idx, person in enumerate(queue):
        print (queue)
        
        if (re.search("^[0-9]", person)):
            low_range = idx - int(person)
            low_range = low_range if low_range >= 0 else 0
            high_range = idx + int(person)
            high_range = high_range + 1 if high_range < len(queue) else len(queue)
            print ("searching in boundaries ", low_range, " ", high_range)
            for search in range(low_range, high_range):
                print("searching on position ", search)
                if (queue[search] == "X"):
                    thiefs_being_catch[search] = "X"
                    print('Thiefs being catched ',thiefs_being_catch)

            print(person, " is cop")

    
    thiefs_catched = len(thiefs_being_catch)

    return thiefs_catched