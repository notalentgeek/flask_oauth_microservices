class Config:
    # SQLALCHEMY_DATABASE_URI = 'postgresql://admin:admin@127.0.0.1:5432/oauth_provider'
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin:admin@postgres:5432/oauth_provider'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'oauth_provider_secret'
