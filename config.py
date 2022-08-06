import os

config = {
    'skipRequestTests': os.environ.get('SKIP_REQUEST_TESTS') == 'TRUE'
}

