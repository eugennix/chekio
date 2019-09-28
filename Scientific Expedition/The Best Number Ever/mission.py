def checkio():
    return 73  # if you are Sheldon
import requests

def num_facts(n):
    '''    :return: ('Boring' or 'Interesting', fact )
    '''
    api_url = 'http://numbersapi.com/' + str(n) + '/math?json=true'
    # params = {'json': 'true'}
    res = requests.get(api_url)
    if res.status_code == 200:
        ans = res.json()
        return ('Interesting', ans['text']) if ans['found'] else ('Boring', ans['text'])
    return None

bifact = num_facts(checkio())
print(bifact[0], bifact[1])

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(checkio(), (int, float, complex))