import reflex as rx

class HelloreflexConfig(rx.Config):
    pass

config = HelloreflexConfig(
    app_name="liho_reflex",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)