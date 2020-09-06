from app import app
#Load this config object for development mode
if __name__ == '__main__':
    app.config.from_object('config.DevelopmentConfig')
    app.run()