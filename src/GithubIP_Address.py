# encoding:utf-8
import requests
import re
import random
import time

domain_list = [
    'github.com',
]

github_subdomain = [
    'gist',
    'assets-cdn',
]

githubusercontent_subdomain = [
    'raw',
    'gist',
    'cloud',
    'camo',
    'user-images',
    'avatars',
]

avatars_list = []
for num in range(9):
    avatars_list.append("avatars" + str(num))

# https://github.com.ipaddress.com/
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
}


def isIP(str):
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(str):
        return True
    else:
        return False


hosts = {}
print("处理domain...")
for domain in domain_list:
    url = "https://" + domain + ".ipaddress.com/"
    response = requests.get(url=url, headers=headers)
    raw_data = response.text
    pattern = re.compile(r'<tr><th>IP Address</th><td><ul class="comma-separated"><li>(.*?)</li></ul></td></tr>')
    find_data = pattern.findall(raw_data)
    if find_data:
        hosts[find_data[0]] = domain
    else:
        hosts['None'] = domain
    time.sleep(1)
print("处理github_subdomain...")
for subdomain in github_subdomain:
    url = "https://github.com.ipaddress.com/" + subdomain + ".github.com"
    response = requests.get(url=url, headers=headers)
    raw_data = response.text
    pattern = re.compile(r'<tr><th>IP Address</th><td><ul class="comma-separated"><li>(.*?)</li></ul></td></tr>')
    find_data = pattern.findall(raw_data)
    if find_data:
        hosts[find_data[0]] = subdomain + ".github.com"
    else:
        # 目前不做处理，进行预设
        PreIP = ['185.199.108.153', '185.199.109.153', '185.199.110.153', '185.199.111.153']
        hosts[PreIP[random.randint(0, 3)]] = subdomain + ".github.com"
    time.sleep(1)

print("处理githubusercontent_subdomain...")
global duplicate_data
for subdomain in githubusercontent_subdomain:
    url = "https://githubusercontent.com.ipaddress.com/" + subdomain + ".githubusercontent.com"
    response = requests.get(url=url, headers=headers)
    raw_data = response.text
    pattern = re.compile(r'<tr><th>IP Address</th><td><ul class="comma-separated"><li>(.*?)</li></ul></td></tr>')
    find_data = pattern.findall(raw_data)
    if find_data:
        hosts[find_data[0]] = subdomain + ".githubusercontent.com"
        duplicate_data = find_data[0]
    else:
        hosts['None'] = subdomain + ".githubusercontent.com"
    time.sleep(1)
    # 已知githubusercontent_subdomain为重复数据，跳出
    break

ErrorData = {}
print("======================Valid-Data======================")

for ip, domain in hosts.items():
    if ip != "None":
        print(ip + "    " + domain)
    else:
        # 查询异常的ip，暂无需处理
        ErrorData[ip] = domain
# 重复数据处理
for duplicateData in githubusercontent_subdomain[1:]:
    print(duplicate_data + "    " + duplicateData + ".githubusercontent.com")
for duplicateData in avatars_list:
    print(duplicate_data + "    " + duplicateData + ".githubusercontent.com")
print("======================================================")
