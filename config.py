import os

config = {
    'isTesting': os.environ.get('IS_TESTING') == 'TRUE'
}

