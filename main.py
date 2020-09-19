import requests
import re
import datetime
curTime = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')
#登录信息
login_data = {
    'log_username':'',
    'log_password':'',
    '__EVENTTARGET':'logon',
    '__EVENTARGUMENT':'',
    '__VIEWSTATE':'/wEPDwUKMTYyMDg3MzEwOA9kFgICAw9kFgQCCQ8PFgIeBFRleHQFPUVzd2lzIOmrmOagoeWtpueUn+e7vOWQiOacjeWKoeW5s+WPsCDlrabnlJ/lt6XkvZznrqHnkIbns7vnu59kZAILDw8WAh8ABU/ljZXkvY3ogZTns7vmlrnlvI865bm/5bee5biC55Wq56a65Yy65aSn5a2m5Z+O5bm/5Lic6I2v56eR5aSn5a2m5a2m55Sf5bel5L2c5aSEZGRkApHRtEp47HU3hwHc7/VDYk7HCWP1VrIoeU831p6jX5o=',
    '__VIEWSTATEGENERATOR':'C2EE9ABB',
    '__EVENTVALIDATION':'/wEdAAR2x90ffMPh62fEUUHFD4Tp1kNwsRYEDqnEZGvD/d7NHmTWfBqM7WrvRN2Hp35y65arCB7eRXhUFaYy1hE/nWj6nK478H4eQaeI8UwPY/TWzZwSA7XuIBUqSutXvspX48U=',
}

#打卡页面的信息
punch_data = {
    '__EVENTTARGET':'',
    '__EVENTARGUMENT':'',
    '__LASTFOCUS':'',
    '__VIEWSTATE':'/wEPDwUKLTc2MDkyMDk0Mw9kFgJmD2QWAgIDD2QWDmYPFgIeB1Zpc2libGVoZAIBDw8WAh4EVGV4dAURMTgwMDUwMjMwNiDlrabnlJ9kZAICDw8WAh8AZ2RkAgMPZBYCAgEPFgIfAGhkAgQPZBYKAgMPZBYCAgUPEGRkFgBkAgUPFgIeCWlubmVyaHRtbAWDAzxsaSBjbGFzcz0iMCI+PGEgaHJlZj0ib3B0X3JjX3d5cWouYXNweD9rZXk9SE9oWTJ3V1hyZzU1Tms5USZmaWQ9MjAiPuWtpueUn+ivt+WBhzwvYT48L2xpPg0KPGxpIGNsYXNzPSIxIHNlbGVjdGVkIHNlbCBhY3QiPjxhIGhyZWY9Im9wdF9yY19qa2RrLmFzcHg/a2V5PUhPaFkyd1dYcmc1NU5rOVEmZmlkPTIwIj7lgaXlurfmiZPljaE8L2E+PC9saT4NCjxsaSBjbGFzcz0iMiI+PGEgaHJlZj0ib3B0X3JjX2prZGtjeC5hc3B4P2tleT1IT2hZMndXWHJnNTVOazlRJmZpZD0yMCI+5omT5Y2h5p+l6K+iPC9hPjwvbGk+DQo8bGkgY2xhc3M9IjMiPjxhIGhyZWY9Im9wdF9yY19meHNxLmFzcHg/a2V5PUhPaFkyd1dYcmc1NU5rOVEmZmlkPTIwIj7ov5TmoKHnlLPor7c8L2E+PC9saT4NCmQCCQ8WAh8AZ2QCCw9kFgYCAQ8WAh8AaBYEAgEPEA8WAh4HQ2hlY2tlZGdkZGRkAgUPDxYCHwFlZGQCAw9kFgQCAQ88KwARAQwUKwAAZAIFDzwrABEBDBQrAABkAgUPFgIfAGcWDAIBDw8WAh8BZGRkAgcPDxYCHwEFCTIwMjAvOS8xOWRkAgkPDxYCHwEFFTE4MDA1MDIzMDYsIOWMuuWNk+i2imRkAgsPDxYCHwEFCzEzNDM3ODIxMjI2ZGQCIQ9kFgYCAQ9kFgICAQ8QZGQWAGQCAw9kFgICAQ8QZGQWAGQCBQ9kFgICAQ8QZGQWAGQCJQ9kFgpmDw8WAh8BBRvlub/kuJznnIHlub/lt57luILnlarnprrljLpkZAIBDw8WAh8BBT7lub/kuJznnIHlub/lt57kvb/nlarnprrljLrlpKfnn7PooZfkvJrmsZ/mnZHnn7PkuK3kuozot68yMOWPt2RkAgIPEGRkFgBkAgcPEGRkFgBkAgoPEGRkFgBkAg0PDxYCHwFlZGQCBQ8PFgIfAQU9RXN3aXMg6auY5qCh5a2m55Sf57u85ZCI5pyN5Yqh5bmz5Y+wIOWtpueUn+W3peS9nOeuoeeQhuezu+e7n2RkAgYPDxYCHwEFT+WNleS9jeiBlOezu+aWueW8jzrlub/lt57luILnlarnprrljLrlpKflrabln47lub/kuJzoja/np5HlpKflrablrabnlJ/lt6XkvZzlpIRkZBgDBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WCAUaY3RsMDAkY3BoX3JpZ2h0JGVfaGVhbHRoJDAFGmN0bDAwJGNwaF9yaWdodCRlX2hlYWx0aCQxBRpjdGwwMCRjcGhfcmlnaHQkZV9oZWFsdGgkMgUaY3RsMDAkY3BoX3JpZ2h0JGVfaGVhbHRoJDMFGmN0bDAwJGNwaF9yaWdodCRlX2hlYWx0aCQ0BRpjdGwwMCRjcGhfcmlnaHQkZV9oZWFsdGgkNQUaY3RsMDAkY3BoX3JpZ2h0JGVfaGVhbHRoJDUFGWN0bDAwJGNwaF9yaWdodCRlX2NoYW5nZWQFE2N0bDAwJGNwaF9yaWdodCRndjEPZ2QFE2N0bDAwJGNwaF9yaWdodCRndjIPZ2RjWPFTDZZYm7qCjKfFrQwG2R4Qcu+NROtEsdJp0u7IWw==',
    'ctl00$cph_right$e_atschool':'是',
    'ctl00$cph_right$e_location':'你的地址' + curTime,
    'ctl00$cph_right$e_observation':'无下列情况',
    'ctl00$cph_right$e_health$0':'无不适',
    'ctl00$cph_right$e_temp':'36.5',
    'ctl00$cph_right$e_describe':'',
    'ctl00$cph_right$e_submit':'提交保存',
    '__VIEWSTATEGENERATOR':'DC47EEF4',
    '__EVENTVALIDATION':'/wEdAB07kpxG/brpWLzuvtwh+ECkCH7C2ooKcj+hye21epcYt57zU+tJOrbkpfeI+4y+0QA5Z9oerNMkjXhVZ0NKo6l0BNuOnAvslhD1zvPfE6p8njwsBakjhQfAu8ecC7+5T+n6I++UYgK22OHU7xYrZo+AKAo7EMQ2twi8SmqnRRLHpCzoZTaRpUmlAHXi1v9rUnrcoWB+ZSaSwSyZ6Qd02q/fS475+yi9pu/K8AEne1pUQSldxvkLsgSZYXV0l/+g5CnUkowtqINm2hseYINhdouXDfiWxlld6EK/kFEymJeFqzUdaox1MfhJKAaU+2/+Xx3jFdvX4jziLBNDAqEehYqvzueLZ3ZddW59ehyg7Yp6RuigWX5Lrhqr4QVjc5zljd9VSUw93iIR+p/Vq1zpHwQug9kiUCHfLWu17Iub8ibnPiuWw5NvonImWnE6wdiOm1AlP3ZSjBpKnYeeXjunNbU4NifJrV4+PZgfSYi8dEJ8WWpnzHL1mRqbMyXodtkOCP/yWwmWBKqAn17OeRrf7PRHqmRamdqGw8vMM5Su3ukGxJDoS3W6wQtiXPuK5s6fg7f2gdyENm5/S/WZYdNiK9fGV2qApdhdm4kj1DrmuhwbL3OsFZqYN9un4N8TeMD58TTKeRtxFGfJ3wuNmeFfa655', 
}

#模拟浏览器
header = {
    'User-agent':'Mozilla/5.0 (Compatible; MSIE 9.0; Windows NT 6.1; Trident/7.0)',
    'Host':'eswis.gdpu.edu.cn',
    'Referer':'https://eswis.gdpu.edu.cn/login.aspx',
    'Accept-Language':'zh-CN',
}

if __name__ == '__main__':
    log_username = input('Input your username:')
    login_data['log_username'] = log_username

    log_password = input('Input your password:')
    login_data['log_password'] = log_password

    host_url = 'http://eswis.gdpu.edu.cn/'
    login_url = 'http://eswis.gdpu.edu.cn/login.aspx'
    session = requests.Session()
    session.post(login_url, headers=header, data=login_data, allow_redirects=False)
    afterlogon = 'http://eswis.gdpu.edu.cn/Default.aspx'
    htmlsource = session.get(afterlogon, headers=header).text
    adminpage = re.findall('href=\"opt_xx_myapps.aspx?(.*)\">', htmlsource)
    print(adminpage)
    enteradmin = host_url + 'opt_xx_myapps.aspx' + adminpage[0]
    print('现在进入日常管理……' + enteradmin)
    session.post(enteradmin, headers=header, data=login_data)
    htmlsource = session.get(enteradmin, headers=header).text
    punchpage = re.findall('href=\"opt_rc_jkdk.aspx?(.*)\">', htmlsource)
    print(punchpage)
    enterpunch = host_url + 'opt_rc_jkdk.aspx' +punchpage[0]
    print('现在进入健康打卡确认页面……' + enterpunch)
    session.post(enterpunch, headers=header, data=punch_data)
    print('完成')