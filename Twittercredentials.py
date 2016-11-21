import tweepy

consumer_key = "Rx8n1WLh9LEHWReAq98jG13q1";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "UgHYdEorN0lBDcgFGx6zaRzeF4GJgviEA5HiMU2rTUHBk0mADh";
#eg: consumer_secret = "UgHYdEorN0lBDcgFGx6zaRzeF4GJgviEA5HiMU2rTUHBk0mADh";

access_token = "1069980823-5eun4VMmXlAYZfimWhDsktgnilfmuo2DMuL0DNK";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "5iteZAOKC1LaLpuM6QAh2u8OKaUZubB7dweP8EHMUFpgB";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



