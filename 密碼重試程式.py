# 設密碼 password = 123
# 使用者最多輸入3次密碼
# if True print"登入成功"
# if False print"輸入錯誤，剩下_機會"
x = 3
password = '123'
while x > 0:
    pwd = input('密碼:')
    if pwd == password:
        print('登入成功')
        break #逃出迴圈
    else :
        x = x - 1
        print('輸入錯誤!剩下', x, '次機會')