#coding=utf-8
import requests
import json
import unittest
import time
import os
from HtmlTestRunner import HTMLTestRunner

class TestWeatherForecast(unittest.TestCase):
    city='江门'
    api='https://free-api.heweather.com/s6/weather/'
    weather_type='forecast'

    value={
        'location':city,
        'key':'63d7ffe16c3743e1af28b8ad4423e5af'
        }
    url=api + weather_type

    def setUp(self):
        self.url=self.url 
        self.city=self.city
        self.value=self.value 
        print('开始啦~')

    def tearDown(self):
        print('结束啦~')

    def GetWeather(self):
        weather_dict=requests.get(self.url,params=self.value).json()
        return weather_dict

    def test_getData(self):
        weatherData=self.GetWeather()
        he_weather=weatherData['HeWeather6']#['daily_forecast']
        daily_forecast=he_weather[0]['daily_forecast']
        print('当前城市为：%s'%self.city)
        for i in range(len(daily_forecast)):
            date=daily_forecast[i]['date']
            cond_txt_d=daily_forecast[i]['cond_txt_d']
            cond_txt_n=daily_forecast[i]['cond_txt_n']
            tmp_max=daily_forecast[i]['tmp_max']
            tmp_min=daily_forecast[i]['tmp_min']
            wind_dir=daily_forecast[i]['wind_dir']
            weather_data=date+'  白天天气:'+cond_txt_d+'  晚上天气:'+cond_txt_n+'\n最高温:'+ tmp_max +'  最低温:'+tmp_min+'  风向:'+wind_dir
            print(weather_data)


if __name__=='__main__':

    #构造测试集
    suite=unittest.TestSuite()
    suite.addTest(TestWeatherForecast('test_getData'))#加入测试用例

    #执行测试
    time=time.strftime('%Y-%m-%d %H_%M_%S')
    path='D:\\python\\practice1\\weatherForecast\\weatherReport\\'+' '+time+' '+'weatherforecast.html' 
    with open(path,'w')as f:
        runner=HTMLTestRunner(stream=f)#,report_title='weather forecast',descriptions='weather forecast'
        runner.run(suite)
        f.close()


    