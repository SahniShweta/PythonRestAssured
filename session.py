import requests

cookie = {'visit-month':'February'}
resp = requests.get("https://rahulshettyacademy.com/", allow_redirects=False, cookies=cookie, timeout=1)
# print(resp.history)
print(resp.status_code)

se = requests.session()
se.cookies.update({'visit-month':'February'})

re = se.get("https://httpbin.org/cookies", cookies={'visit-year':'2020'})
print(re.text)

# Attachments

url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
files = {'file': open('D:\\ic_launcher.png', 'rb')}
response = requests.post(url, files=files)
print(response.status_code)
print(response.text)