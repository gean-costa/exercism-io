def is_pangram(sentence):
    sentence = sentence.replace(" ", "")
    list_az = list(range(ord("a"), ord("z")+1))
    list_AZ = list(range(ord("A"), ord("Z")+1))

    for i in range(0, len(list_az)):
        if chr(list_az[i]) in sentence:
            continue
        elif chr(list_AZ[i]) in sentence:
            continue
        else:
            return False

    return True

if __name__ == "__main__":
    print(is_pangram("The quick brown fox jumps over the lazy og"))
