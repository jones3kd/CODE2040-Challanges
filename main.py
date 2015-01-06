"""
This is my code for the CODE2040 Challenges

author: Kelsey Jones
date: 1/5/15

"""

import json
import requests, datetime
import dateutil.parser as dp


def stageI(token_dic):
    """
    word = requests.post(
        "http://challenge.code2040.org/api/getstring",
        data=json.dumps(token_dic))

    word = word.json()['result']
    """
    word = post_token("http://challenge.code2040.org/api/getstring", token_dic)
    word = word['result']

    print(word)

    rev_word = word[::-1]
    token_dic["string"] = rev_word

    print(token_dic)

    print(requests.post(
        "http://challenge.code2040.org/api/validatestring",
        data=json.dumps(token_dic)).text) 

def stageII(token_dic):
    dic = post_token("http://challenge.code2040.org/api/haystack", token_dic)
    print(dic)

    dic = dic['result']
    haystack = dic['haystack']
    needle = dic["needle"]

    found = False
    count = 0
    
    while not found and count < len(haystack):
        if haystack[count] == needle:
            found = True
            token_dic['needle'] = count
            print(post_return(
                "http://challenge.code2040.org/api/validateneedle", token_dic))
        else:
            count += 1

def stageIII(token_dic):
    dic = post_token("http://challenge.code2040.org/api/prefix", token_dic)
    print(dic)

    dic = dic['result']
    array = dic['array']
    prefix = dic['prefix']

    ans = []

    for word in array:
        if not word.startswith(prefix):
            ans.append(word)

    token_dic['array'] = ans
    print(post_return("http://challenge.code2040.org/api/validateprefix",
                      token_dic))

def stageIIII(token_dic):
    dic = post_token("http://challenge.code2040.org/api/time", token_dic)
    print(dic)

    dic = dic['result']

    secs = dic['interval']
    date = dic["datestamp"]

    date_secs = dp.parse(date).strftime('%s')
    print(date_secs)

    ans = int(secs) + int(date_secs)
    #ans = str(ans)

    dt = datetime.datetime.fromtimestamp(ans)
    iso_format = dt.isoformat() + 'Z'
    ans = str(iso_format)

    new_token_dic = {}
    new_token_dic['datestamp'] = ans
    new_token_dic['token'] = token_dic['token']
    print(new_token_dic)
    print(post_return(
        "http://challenge.code2040.org/api/validatetime", new_token_dic))

def post_token(url, token):

    return (requests.post(
        url,
        data=json.dumps(token)) ).json()

def post_return(url, dic):
    return (requests.post(
        url,
        data=json.dumps(dic)) ).json()

def main():
    reg_url = "http://challenge.code2040.org/api/register"

    dic = {"email": "kelsey.jones003@gmail.com",
           "github":"https://github.com/jones3kd/CODE2040-Challanges"}

    #print(json.dumps(dic))

    token = requests.post(reg_url, data=json.dumps(dic))

    #print(token.text)
    token = token.json()
    key = token['result']
    token = {"token":key}
    print(token)

    #Stage 1
    stageI(token)
    stageII(token)
    stageIII(token)
    stageIIII(token)

    print(post_token("http://challenge.code2040.org/api/status", token) )
    
    

if __name__ == "__main__": main()
