from .settings import * 


# Set this to True to enable HTTPS redirection
SECURE_SSL_REDIRECT = True

# Set this to True to ensure all cookies are marked as secure
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Optionally, you can set the HSTS header to enforce HTTPS for a specified duration
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Set this if your Django app is behind a proxy or load balancer
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')



CSRF_TRUSTED_ORIGINS = ["https://mohamed123.zapto.org"]
DEBUG= False
SECRET_KEY = os.getenv('SEKRET_KEY')
ALLOWED_HOSTS = ['51.255.49.204' , 'localhost' , '127.0.0.1' , 'mohamed123.zapto.org']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CORS_ALLOWED_ORIGINS = [
    # 'http://127.0.0.1:8000',
    # 'http://localhost:8000', 
    # 'http://localhost:3000',  
    # 'http://localhost:8800',
    # 'http://localhost:3001',
     
    'http://51.255.49.204:80',
    'http://51.255.49.204:8080',
    'https://51.255.49.204:80',
    'https://51.255.49.204:8080',
    'https://mohamed123.zapto.org',
    'http://mohamed123.zapto.org',
    'https://51.255.49.204',
    'http://51.255.49.204',
]
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True
SITE_URL='https://mohamed123.zapto.org'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': 'postgres',
        'NAME': os.getenv('PG_DATABASE'),
        # 'USER': 'postgres',
        'USER': os.getenv('PG_PASSWORD'),
        # 'PASSWORD': 'postgres',
        'PASSWORD': os.getenv('PG_PASSWORD'),
        # 'HOST': 'database', 
        'HOST': os.getenv('PG_HOST'),
        # 'PORT': 5432,
        'PORT': os.getenv('PG_PORT'),

    }
}

# email
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT = 587    
EMAIL_HOST_USER = 'khedmasite@gmail.com'  
EMAIL_HOST_PASSWORD = 'byhu pmrn txyn srcd'
EMAIL_USE_TLS = True