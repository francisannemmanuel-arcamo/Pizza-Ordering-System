import requests
from re import findall

class Message_Processor:
    def __init__(self, message: str, regex_pattern: str) -> None:
        self.message = message
        self.regex_pattern = regex_pattern
        self._all_products = self._get_all_products()
        self.message_dict = self._parse_message(message)

    def _get_all_products(self) -> list:
        r = requests.get('http://192.168.254.111:8000/api/products/')
        data = r.json()['products']
        _dict = {}

        for i in data:
            _dict[i['pizza_code']] = i['pizza_name']

        return _dict

    def _parse_message(self, message: str) -> dict:
        _dict = {}
        _list = []
        orders = findall(self.regex_pattern, message)

        for i in orders:
            temp = i.split('.')
            _list.append({'pizza_code': temp[0], 'pizza_quantity': int(temp[1]), 'pizza_size': int(temp[2])})

        if findall(self.regex_pattern, self.message.split(' ')[-1]) == []:
            _dict['customer'] = self.message.split(' ')[-1]
        else:
            _dict['customer'] = None

        _dict['orders'] = _list

        return _dict

    def _validate_order(self, order: list) -> bool:
        _dict = {'product': list(self._all_products.keys()), 'size': [0,1]}

        for i in order:
            if i['pizza_code'] not in _dict['product']:
                print("hehe")
                return False
            if i['pizza_size'] not in _dict['size']:
                print("Test")
                return False
        
        return True

    def process_message(self) -> dict:
        if self._validate_order(self.message_dict['orders']):
            return self.message_dict
        else:
            return {'error': 'Invalid order'}

def test():
    message = 'PROD-1642.1.1 AJ'
    message_processor = Message_Processor(message, regex_pattern="PROD\-\d{4}\.\d.\d")
    print(message_processor.process_message())