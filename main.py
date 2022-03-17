import requests
import time
# pip install requests
# timeは標準ライブラリ

print("何か入力してください")
input()

print("送りたい回数を入れてください")
# intじゃないと動かない
e = int(input())

print("何秒ごとに送りますか(0はバグります)")
stime = int(input())

# ここにtokenいれる
token = 'token1つ目入れる'

token2 = 'token2つ目入れる'

# 送りたい文字を入れる
payload = {
  'content': "送りたい文字"
}

header = {
  'authorization': token
}

header2 = {
  'authorization': token2
}

# チャンネルidを入れる
ch =0123456789
ch2 =  03225694455566550

# ここから下はいじらないで
xsize = 0
i = 0
while(i < e):
    r = requests.post('https://discord.com/api/v9/channels/' + str(ch) + '/messages', data=payload, headers=header)
    r = requests.post('https://discord.com/api/v9/channels/' + str(ch2) + '/messages', data=payload, headers=header)
    r = requests.post('https://discord.com/api/v9/channels/' + str(ch) + '/messages', data=payload, headers=header2)
    r = requests.post('https://discord.com/api/v9/channels/' + str(ch2) + '/messages', data=payload, headers=header2)
    xsize += 1
    print("Sent Messages x" + str(xsize))
    # 速度早くしたいならこの下のtime.sleep(1)を消す(消したらapiのエラーが出るから消さない方がいい)
    time.sleep(stime)
    i += 1
