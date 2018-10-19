#!/usr/bin/python
# -*- coding:utf-8 -*-

from config import settings
# from src.engine.agent import AgentHandler
# from src.engine.salt import SaltHandler
# from src.engine.ssh import SSHHandler
import importlib


# def run():
#     '''
#     采集资产入口
#     :return:
#     '''
#     if settings.ENGINE == 'agent':
#         obj = AgentHandler()
#         obj.handler()
#     elif settings.ENGINE == 'ssh':
#         obj = AgentHandler()
#         obj.handler()
#     elif settings.ENGINE=='salt':
#         obj=AgentHandler()
#         obj.handler()
#     else:
#         print('不支持的配置模式')
def run():
    engine_path = settings.ENGINE_HANDLERS.get(settings.ENGINE)
    # module_path='src.engine.agent'
    # cls_name='AgentHandler'
    module_path, cls_name = engine_path.rsplit('.', maxsplit=1)
    module = importlib.import_module(module_path)

    cls = getattr(module, cls_name)
    obj = cls()
    obj.handler()


run()
