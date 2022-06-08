import requests


class ApiCommunicator:
    url_path = 'https://piskvorky.jobs.cz/api/v1'

    @staticmethod
    def register(nickname, email):
        print(f'Register user: {nickname}')

        response = requests.post(url=f'{ApiCommunicator.url_path}/user',
                                 json={'nickname': nickname, 'email': email})

        return ApiCommunicator.response_info(response)

    @staticmethod
    def connect_game(user):
        print('Starting a game...')

        response = requests.post(url=f'{ApiCommunicator.url_path}/connect',
                                 json={'userToken': user.token})

        return ApiCommunicator.response_info(response)

    @staticmethod
    def send_hits(user, game, coordinates):
        print(f'Sending hit: {coordinates.x}, {coordinates.y}')

        response = requests.post(url=f'{ApiCommunicator.url_path}/play',
                                 json={'userToken': user.token,
                                       'gameToken': game.token,
                                       'positionX': coordinates.x,
                                       'positionY': coordinates.y})

        return ApiCommunicator.response_info(response)

    @staticmethod
    def check_status(user, game):
        print('Checking game status...')

        response = requests.post(url=f'{ApiCommunicator.url_path}/checkStatus',
                                 json={'userToken': user.token,
                                       'gameToken': game.token})

        return ApiCommunicator.response_info(response)

    @staticmethod
    def check_last_hit(user, game):
        print('Checking last hit...')

        response = requests.post(url=f'{ApiCommunicator.url_path}/checkLastStatus',
                                 json={'userToken': user.token,
                                       'gameToken': game.token})

        return ApiCommunicator.response_info(response)

    @staticmethod
    def response_info(response):
        response_json = response.json()
        print(f'Response: {response_json}')
        print(f'Status code: {response.status_code}')
        return response_json
