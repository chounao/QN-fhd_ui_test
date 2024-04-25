"""
如果进行多种浏览器的自动化
在config文件配置
"""
import configparser
import os
from common.Logger import logger

class TestReadConfigFile:
    def __init__(self,filpath = None):
        if filpath:
            configpath = filpath
        else:
            configpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/config/config.ini'
        self.config = configparser.RawConfigParser()
        self.config.read(configpath,encoding='utf-8')

    def get_config_value(self,section,opiton):
        """
         根据传入的section获取对应的value
         :param section: ini配置文件中用[]标识的内容
         :return:
         """
        # 获取项目绝对路径（\Users\admin\PycharmProjects\UITest）
        # root_dir = os.path.dirname(os.path.abspath('.'))
        # 获取文件的当前路径（\Users\admin\PycharmProjects\UITest\framework）
        # root_dir = os.path.split(os.path.realpath(__file__))[0]

        value = self.config.get(section,opiton)
        return value

    def read_data(self):


        # configpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/config/config.ini'
        # config = configparser.RawConfigParser()
        # config.read(configpath,encoding='utf-8')
        data = dict(self.config._sections)
        url = data["stagingData"]["url"]
        token = data["stagingData"]["token"]
        # print(data)
        print(url)
        print(token)

        return data


def read_data():
    """读取ini文件"""

    configpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\config\config.ini'
    config = configparser.RawConfigParser()
    config.read(configpath,encoding='utf-8')
    data = dict(config._sections)
    logger.info("获取到ini文件数据")
    return data


if __name__ == '__main__':
    # testReadConfigFile = TestReadConfigFile()
    # result = testReadConfigFile.get_config_value("browserType","browserName")
    # print(result)
    read_data()
