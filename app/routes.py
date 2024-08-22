from app import app, redis

@app.route('/')
def index():
    redis.incr('hits')
    return 'This page has been visited {} times.'.format(redis.get('hits'))
