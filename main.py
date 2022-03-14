import requests
import time

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
ch = 001010225511554294

# ここから下は意味わからんことなったからいじらない方がいい
i = 0
while(i < 3):
    r = requests.post('https://discord.com/api/v9/channels/' + str(ch) + '/messages', data=payload, headers=header)
res.raise_for_status()
time.sleep(1)
i += 1
    
