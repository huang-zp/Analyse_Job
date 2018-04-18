from flask_cache import Cache

# 缓存实例

cache = Cache(config={'CACHE_TYPE': 'simple'})