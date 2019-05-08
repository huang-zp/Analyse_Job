from flask_cache import Cache

# 缓存实例， 缓存类型为simple
cache = Cache(config={'CACHE_TYPE': 'simple'})