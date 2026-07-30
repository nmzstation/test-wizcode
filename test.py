import requests
# 送信先のURL
url = "https://hogehoge.com/api/v1/payments"

# リクエストヘッダー（APIキーなどによる認証情報）
headers = {
    "Content-Type": "application/json",
    #"X-API-Key": "nfdsuaio54wqntugsa084574800hudsia89",  # APIキーをヘッダーで渡す場合
    # Bearerトークン形式の場合は以下のように指定することもあります
     "Authorization": "Bearer AKIA3RPLEFVKNEI65K4K",
     "AccessKeyId": "AKIA3RPLEFVKNEI65K4K"
}

# リクエストボディ（クレジットカード情報等を含むペイロード）
payload = {
    "amount": 5000,
    "currency": "JPY",
    "card_info": {
        "number": "5365-1376-1111-3456",  # クレジットカード番号
        "exp_month": "12",                 # 有効期限（月）
        "exp_year": "2028",                # 有効期限（年）
        "cvv": "XXX",                      # セキュリティコード
        "holder_name": "TARO YAMADA"       # カード名義人
    }
}

try:
    # POSTリクエストの送信
    # `json=payload` を指定すると、自動的にJSON文字列に変換されて送信されます
    response = requests.post(url, headers=headers, json=payload, timeout=10)

    # レスポンスのステータスコードを表示
    print(f"Status Code: {response.status_code}")

    # レスポンスボディ（JSON形式）の表示
    print("Response:")
    print(response.json())

except requests.exceptions.RequestException as e:
    print(f"通信エラーが発生しました: {e}")

    