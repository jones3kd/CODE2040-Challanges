"""
This is my code for the CODE2040 Challenges
http://challenge.code2040.org/

author: Kelsey Jones
date: 1/5/15

"""

import json
import requests, datetime
import dateutil.parser as dp


class Code_Challenge:

    def __init__(self):
        """Sets up the API and gets the token json """
        
        reg_url = "http://challenge.code2040.org/api/register"

        reg_dic = {"email": "kelsey.jones003@gmail.com",
               "github":"https://github.com/jones3kd/CODE2040-Challanges"}
        
        self.token = requests.post(reg_url, data=json.dumps(reg_dic))
        self.token = self.token.json()
        key = self.token['result']
        self.token = {"token":key}

    
    def stageI(self):
        """ Reverses the word and returns the reversed word and token as a
        json file """
        
        ans_dic = {}
        word = self.__post_token("http://challenge.code2040.org/api/getstring")
        word = word['result']

        rev_word = word[::-1]
        ans_dic["string"] = rev_word

        print(self.__post_return(
            "http://challenge.code2040.org/api/validatestring", ans_dic)) 

    def stageII(self):
        """ Returns the position of the array element in the haystack array and
        returns the position as a json file"""
        
        ans_dic = {}
        
        dic = self.__post_token("http://challenge.code2040.org/api/haystack")

        dic = dic['result']
        haystack = dic['haystack']
        needle = dic["needle"]

        found = False
        count = 0
        
        while not found and count < len(haystack):
            if haystack[count] == needle:
                found = True
                ans_dic['needle'] = count
                print(self.__post_return(
                    "http://challenge.code2040.org/api/validateneedle", ans_dic))
            else:
                count += 1

    def stageIII(self):
        """ Returns a list/array of all the words that do not start with the
        specific prefix as a json file"""
    
        ans_dic = {}
        
        dic = self.__post_token("http://challenge.code2040.org/api/prefix")

        dic = dic['result']
        array = dic['array']
        prefix = dic['prefix']

        ans = []

        for word in array:
            if not word.startswith(prefix):
                ans.append(word)

        ans_dic['array'] = ans
        print(self.__post_return("http://challenge.code2040.org/api/validateprefix",
                          ans_dic))

    def stageIIII(self):
        """ Adds the seconds to the specified iso 8601 datestamp and returns
        the date and time as an iso 8601 datestamp."""
    
        ans_dic = {}
        dic = self.__post_token("http://challenge.code2040.org/api/time")
        dic = dic['result']

        secs = dic['interval']
        date = dic["datestamp"]

        date_secs = dp.parse(date).strftime('%s')

        ans = int(secs) + int(date_secs)

        dt = datetime.datetime.fromtimestamp(ans)
        iso_format = dt.isoformat() + 'Z'
        ans = str(iso_format)

        ans_dic['datestamp'] = ans
        print(self.__post_return(
            "http://challenge.code2040.org/api/validatetime", ans_dic))

    def __post_token(self,url):
        """ Posts to the specified url and returns the decoded json reponse """
        return (requests.post(url, data=json.dumps(self.token)) ).json()

    def __post_return(self,url, dic):
        """ Posts the challenge answer and encodes the python dictionary
        into a json file """
        
        dic["token"] = self.token["token"]
        return (requests.post(url, data=json.dumps(dic)) ).json()
    
    def print_score(self):
        """ Prints the resulting score for all challenges """
        print(self.__post_token("http://challenge.code2040.org/api/status") ) 

def main():
    chall = Code_Challenge()
    
    chall.stageI()
    chall.stageII()
    chall.stageIII()
    chall.stageIIII()
    chall.print_score()     

if __name__ == "__main__": main()
