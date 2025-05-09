import os
from app import create_app

DEBUG_MODE = os.getenv("DEBUG", "True")
                                          
app = create_app()

if __name__ == '__main__':
    app.run(debug=DEBUG_MODE)
