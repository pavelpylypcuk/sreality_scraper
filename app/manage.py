from flask_project import app

# configures host, port and runs the script via 'python manage.py'
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)