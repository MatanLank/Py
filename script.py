import requests, time

def open_txt_file(name):
    with open(name, 'r') as f:
        content = f.read()
        return content

def check_ip(ip):
    try:
        response = requests.get(ip)
        if response.status_code == 200:
            print('success - ' + ip)
    except:
        print('failed - ' + ip)

contents_of_file = open_txt_file('targets/targets.txt')
split_content = contents_of_file.split('\n')

for i in split_content:
    check_ip(i)

# while True:
#     result = requests.get('https://google.com')
#     print(result.status_code)
#     time.sleep(3)
