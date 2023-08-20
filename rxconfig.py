import reflex as rx

class PythonreflexConfig(rx.Config):
    pass

config = PythonreflexConfig(
    app_name="python_reflex",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)