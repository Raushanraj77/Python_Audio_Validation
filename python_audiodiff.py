import requests
import audiodiff
url = 'https://www.sample-videos.com/audio/mp3/crowd-cheering.mp3'
fileName = 'test_download.mp3'
req = requests.get(url)
file = open(fileName, 'wb')
for chunk in req.iter_content(100000):
    file.write(chunk)
file.close()
status = audiodiff.equal('test_download.mp3', 'test.mp3')
assert status, "False"