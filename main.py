import requests
import time

print("何か入力してください")
input()


# ここにtokenいれる
token = 'tokenここにいれるよ'

# 送りたい文字を入れる
payload = {
  'content': "送りたい文字"
}

header = {
  'authorization': token
}

# チャンネルidを入れる
ch = 123456789101112131
ch2 = 123456789101112131

# 送りたい回数を入れる(この場合は10)
e = 10

# ここから下はいじらないで
xsize = 0
i = 0
while(i < e):
    r = requests.post('https://discord.com/api/v9/channels/' + str(ch) + '/messages', data=payload, headers=header)
    r = requests.post('https://discord.com/api/v9/channels/' + str(ch2) + '/messages', data=payload, headers=header)
    xsize += 1
    print("Sent Messages x" + str(xsize))
    time.sleep(1)
    i += 1
