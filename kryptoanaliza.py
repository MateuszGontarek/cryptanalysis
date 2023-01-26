import pandas as pd

def kryptoanaliza(df, text):
    decipher = [False] * len(text)
    for i in range(len(df['cipher'])):
        for j in range(len(text)):
            row = df['cipher'][i].split()
            if text[j] in row and not decipher[j]:
                decipher[j] = df['decipher'][i].split()[row.index(text[j])]
                break
        if all(isinstance(item, str) for item in decipher):
            break
    
    returnValue = ''
    for i in decipher:
        returnValue = ' '.join(decipher)

    return returnValue

df = pd.read_csv('data.csv')
decryptTexts = []
for i in range(6):
    text = input().split()
    decryptTexts.append(kryptoanaliza(df, text))

print()
for i in decryptTexts:
    print(i)