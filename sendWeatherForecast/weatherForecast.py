#coding=utf-8
import requests
import json


city='江门'
api='https://free-api.heweather.com/s6/weather/'
weather_type='forecast'

def weather_forecast():

    value={
        'location':city,
        'key':'63d7ffe16c3743e1af28b8ad4423e5af'
}
    
    
    url=api+weather_type
    weather_dict=requests.get(url,params=value).json()
    #print(weather_dict)
    return weather_dict
    
def get_data():
    weather_dict=weather_forecast()
    he_weather=weather_dict['HeWeather6']#['daily_forecast']#天气预报，list
    daily_forecast=he_weather[0]['daily_forecast']
    print('当前城市为：%s'%city)
    for i in range(len(daily_forecast)):
        date=daily_forecast[i]['date']
        cond_txt_d=daily_forecast[i]['cond_txt_d']
        cond_txt_n=daily_forecast[i]['cond_txt_n']
        tmp_max=daily_forecast[i]['tmp_max']
        tmp_min=daily_forecast[i]['tmp_min']
        wind_dir=daily_forecast[i]['wind_dir']
        weather_data=date+'  白天天气:'+cond_txt_d+'  晚上天气:'+cond_txt_n+'\n最高温:'+ tmp_max +'  最低温:'+tmp_min+'  风向:'+wind_dir
        print(weather_data)
    return True


 
        
if __name__=='__main__':
    weather_data=get_data()
    print(weather_data)