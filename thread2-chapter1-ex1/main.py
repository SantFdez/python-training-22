def main():
    bad_actions = ['broke someone\'s window', 'fought over a toaster', 'killed a bug']
    what_list_am_i_on(bad_actions)
    
    good_actions = ['got someone a new car', 'saved a man from drowning', 'never got into a fight']
    what_list_am_i_on(good_actions)
    
    actions = ['broke a vending machine', 'never got into a fight', 'tied someone\'s shoes']
    what_list_am_i_on(actions)
    
def what_list_am_i_on(actions):
    good_actions_count = 0
    bad_actions_count = 0

    for action in actions:
        first_letter = action[0]
        if (first_letter in ["b", "f", "k"]):
            bad_actions_count = bad_actions_count + 1
        elif (first_letter in ["g", "s", "n"]):
            good_actions_count = good_actions_count + 1

    if (bad_actions_count >= good_actions_count):
        print("naughty")
    else:
        print("nice") 

if __name__ == "__main__":
    main()