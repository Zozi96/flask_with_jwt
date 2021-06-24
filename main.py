from apps import create_app

settings_config = 'config.local.LocalConfig'
app = create_app(settings_config)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
