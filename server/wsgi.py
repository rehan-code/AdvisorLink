from app import app

if __name__ == "__main__":
    app.run(('etc/ssl/cert.crt', 'etc/ssl/private.key'))
