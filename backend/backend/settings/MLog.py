import os
import datetime

def getlogger(basepath):
    LOGCONFIG = {
        'version': 1,
        'disable_existing_loggers': False, # 是否禁用第三方日志功能
        # 1. 定义日志格式
        'formatters': {
            'verbose': {
                'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
                'style': '{',
            },
            'simple': {
                'format': '{levelname} {message}',
                'style': '{',
            },
        },
        # 2. 定义日志的过滤信息
        'filters': {
            'require_debug_true': { # 如果debug模式则进入到以下分支
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },
        # 定义日志的处理方式
        'handlers': {
            'console': {
                'level': 'INFO',
                'filters': ['require_debug_true'],
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'file': {
                'level': 'INFO',
                'filters': ['require_debug_true'],
                'class': 'logging.FileHandler',
                # 'filename': '/app/logs/a.log',
                'filename': os.path.join(os.path.dirname(basepath), 'logs', datetime.datetime.now().strftime('%Y%m%d.log')),
                # 'maxBytes': 300 * 1024 * 1024, # 每个文件300M # TODO: 待解决这里参数加不上的问题
                # 'backupCount': 10, #, 最多保存10个文件
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'company1': {
                'handlers': ['console', 'file'],
                'propagate': True,
            },
            'myproject.custom': {
                'handlers': ['console'],
                'level': 'INFO',
            }
        }
    }
    return LOGCONFIG