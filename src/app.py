from settings import Settings
from quart import Quart

def create_app():
    app: Quart = Quart(__name__)

    settings: Settings = Settings() # ty: ignore
    app.config['SETTINGS'] = settings
    app.url_map.strict_slashes = False

    # Blueprints

    from routes.home_bp import home_bp
    app.register_blueprint(home_bp)

    return app

if __name__ == "__main__":
    app: Quart = create_app()
    settings: Settings = Settings() # ty: ignore
    app.run(port=settings.APP_PORT)
