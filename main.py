import requests


class App:
    def __init__(self):
        self.api_url = 'http://localhost:3001'

    def get_brands(self):
        url = f'{self.api_url}/brands'
        response = requests.get(url, data="")
        if response.status_code == 200:
            return response.json()
        else:
            return []

    def get_phones(self, phone):
        url = f'{self.api_url}/brand/{phone}'
        response = requests.get(url, data="")
        if response.status_code == 200:
            return response.json()
        else:
            return []

    def get_device(self, device):
        url = f'{self.api_url}/device/{device}'
        response = requests.get(url, data="")
        if response.status_code == 200:
            return response.json()
        else:
            return []


if __name__ == '__main__':
    app = App()
    brands = app.get_brands()
    for brand in brands:
        # print(brand['url'])
        phones = app.get_phones(brand['url'])
        pages = phones['pages']
        for phone in phones['data']:
            print(phone['url'])
            # todo implement logic here
        for page in pages:
            if 'url' in page:
                phones = app.get_phones(page['url'])
                for phone in phones['data']:
                    # print(phone['url'])
                    devices = app.get_device(phone['url'])
                    ratio_str = devices['spec_detail'][3]['specs'][1]['value']
                    name = devices['title']
                    ratio = ratio_str[ratio_str.find('~') + 1: ratio_str.find('%')]
                    size = devices['quick_spec'][0]['value']
                    batt = devices['quick_spec'][6]['value']
                    # if float(ratio) >50 :
                    print(name)
                    print(ratio)
                    print(size)
                    print(batt)
