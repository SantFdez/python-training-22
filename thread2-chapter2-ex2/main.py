def main():
    print("Test one")
    print ("Yay") if reverse(' Hello World ') == 'World Hello' else print("Nay")
    print("Test two")
    print ("Yay") if reverse('   Hi  There.  ') == 'There. Hi' else print("Nay")
    print("Test three")
    print ("Yay") if reverse('This is a reversed sentence. Good job') == 'job Good sentence. reversed a is This' else print("Nay")
   
    
def reverse(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = " ".join(reversed_words)
    return(reversed_sentence)

if __name__ == "__main__":
    main()