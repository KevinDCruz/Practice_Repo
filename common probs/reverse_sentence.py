def reverse(sentence):
    """if len(sentence) == 0:
                    return None
                elif len(sentence) == 1:
                    return None
                else:"""
    words = sentence.split(" ")
    x = [word[::-1] for word in words]
    reversed = " ".join(x)
    print(reversed)

reverse("Kevin is")
