import csv

dict_data={}

with open('challange-data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        words = row['sentence'].split()
        ciphers = row['cipher'].split()
        for word, cipher in zip(words, ciphers):
            if cipher not in dict_data:
                dict_data[cipher] = word

list = ['ILIM ZCEYSUGXK LULFNCA KCWAJPFEH TGNB NTMXNAONDHT QUGIR BJSSUHF'
    'VIXPAOJ ISBJ GTRIMHTSUUF UNRGGAXD Y UYGRVIM ITC EJCYGIN'
    'RFRE NYPLSJLL ITA NYDLBHC IFJLABJ GJTQNTX JAQNACPO ZTKD'
    'JIXPEI PJQFYQY UONYFBYOUYQ UPSS YX PYWLKE NEVHW LFLYATZS'
    'LVGLAMN JPJLY FRWUKFICPOQ JVPXLDST FWCWESDXY TRWVSPJTTT PZWXIEJAFRCN CJZGN'
    'XLCHIIL OOJRX ITJUWQXW JKUXFKCNB CISUF OESCVDIJUMMW IFBJLVNCNT QFBVG']

def decrypt_sentence():
    for sentence in list:
        words = sentence.split()
        for i in range(len(words)):
            if words[i] in dict_data:
                words[i] = dict_data[words[i]]
            deciphered_sentence = ' '.join(words)
            print(deciphered_sentence)

decrypt_sentence()