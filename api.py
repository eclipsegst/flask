from app import create_api

api = create_api()

if __name__ == '__main__':
    api.run(debug=True, port=5001)
