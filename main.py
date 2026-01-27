from website import create_app

app = create_app()

if __name__ == '__main__': #only run if this file is executed directly
    app.run(debug=True) #debug=True for development only, remove in production
     
