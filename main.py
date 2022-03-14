import requests

# 送りたい文字
payload = {
  'content': "送りたい文字"
}

# token入れる
header = {
  'authorization': 'token'
}

# チャンネルid
ch = 9034944649151848

# 送りたい回数
for i in range (100):
  r = requests.post('https://discord.com/api/v9/channels/' + str(ch) + '/messages', data=payload, headers=header)
