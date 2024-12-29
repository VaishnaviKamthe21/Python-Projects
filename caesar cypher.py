alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encode(text,shift):
    encoded_text=""
    for i in range(len(text)):
        if text[i].isalpha():
            position=alphabet.index(text[i])
            new_position=position+shift
            encoded_text+=alphabet[new_position]
        else:
            encoded_text+=text[i]
    return encoded_text

def decode(text,shift):
    decoded_text=""
    for i in range(len(text)):
        if text[i].isalpha():
            position=(''.join(alphabet)).rindex(text[i])
            new_position=position-shift
            decoded_text+=alphabet[new_position]
        else:
            decoded_text+=text[i]
    return decoded_text


while True:
    ch=int(input("1. Encrypt \n2. Decrypt \n3.Exit?\n"))
    if ch==1:
        ip=input("Enter your message:\n")
        sh=int(input("Enter the shift number: "))
        print("Your code:")
        print(encode(ip,sh))
    
    elif ch==2:
        ip=input("Enter your message:\n")
        sh=int(input("Enter the shift number: "))
        print("Your code:")
        print(decode(ip,sh))

    else:
        print("Thank you!")
        break

