LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters':
        {
            'default':
            {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            }
        },
    'handlers':
        {
            'stdout':
            {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'stream': 'ext://sys.stdout'
            },
            'filehandler': {
                'class': 'logging.FileHandler',
                'formatter': 'default',
                'filename': 'log/main.log'
            },
            'user_handler': {
                'class': 'logging.FileHandler',
                'formatter': 'default',
                'filename': 'log/user.log'
            },
            'account_handler': {
                'class': 'logging.FileHandler',
                'formatter': 'default',
                'filename': 'log/user.log'
            }
        },
    'loggers':
        {
            'user': {
                'handlers': ['user_handler'],
                'level': 'DEBUG',
            },
            'account': {
                'handlers': ['account_handler'],
                'level': 'DEBUG',
            },
        }
}
