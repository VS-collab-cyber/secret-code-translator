print("secret code translator")
print("type your message")

import random
import string

message = input()

if len(message)<3:
    print(message[::-1])
    
else:
    start = ''.join(random.choices(string.ascii_letters, k=3))
    end = ''.join(random.choices(string.ascii_letters, k=3))
    word = message[1:] + message[0]
    print(start + word + end)
