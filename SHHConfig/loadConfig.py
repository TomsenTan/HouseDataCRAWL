# -*-coding:utf-8-*-
# @Author:Thomson
# @Date:2019-04-04



def addConfigs(fileName):
    import re
    configsList = []
    _rex = re.compile('\w+')
    _headlineRex = re.compile('#')
    with open(fileName, 'rb') as f:
        configMes = f.readlines()
        for config in configMes:
            # 去除文件头部
            if re.match(_headlineRex, config.decode('utf-8')) or len(config) == 2:
                continue
            elif re.findall(_rex, config.decode('utf-8')):
                # 去除注释
                if re.findall('#', config.decode('utf-8')):
                    config = config.decode('utf-8').split('#')[0].strip(' ')
                    configsList.append(config)
                else:
                    configsList.append(config.decode('utf-8'))
            else:
                continue
        return configsList


def loadCofigs(fileName):
    configResult = addConfigs(fileName)
    return configResult

