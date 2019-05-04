import json
import requests

youtube_url = "https://www.youtube.com/watch?v=y6XX39DaEL4"
#transcript_json_url = "https://00e9e64bac4a30dc976c87ac7bed719495328d5a37d54a496e-apidata.googleusercontent.com/download/storage/v1/b/citeit_speech_text/o/freakonomics%2F280-why-is-my-life-so-hard-times-original.json?qk=AD5uMEvDxiilsEmq809_vWydy_RMJ9l3Sc1Ym5GB84cI1Gb__h1VKnF4t7x6GylmHvAhJg5iIC75sAijf5-y13wFlYAkOwTKzyT4SnQP8v4ILd51L0nTy7pBJgvclW6-QBGYD8W9pBUImAUCgsb25AJnaXdiCkBDJzUkXYCOVGdPkYA8opymk7ld7gQV13RvjH49tzPZHir-4PBPx3Uea80EG5FYiaLYdrGKMwacyPaC2lYcqikSlWThRbCi1wQn7dXGVUWKgavH0GZrtW0t4SkOe9zSMijxRnbm1XWDvQhfIhum_nLQhGxHNxADtEAfiIHjAlKCBnucXcTyN2wbiyJfZSO8LI3EynC-9Xe4vU1N-FQALzxLzAN5Tic0WfnQvQXWNqHpuQawLqoiMC-C9j6yf36cbkwWWdQHrB7S2DMH0xZsNuIGcbjOcWSxzacYDFrVRxVCYdNIx9335wlKxPR_iPhK3mmaFai6xAptKGnsVS5-lsNVAU9odja1sLSZuwK4F1g-ZeW4h74Y_bEDfj5ZOc6rueXIxxPjRoAIT5vhRvcauGjxPNXYzmdH0vM8sVlXN8yo4vlvj6nXz-sVJTnDVfA0gHkTYo9Rdtgwxc3qwt4iP7wr0tZnS8o50fP66QXt_4xqgc0HTuKfdnvU5KxhhRUV-Okp29xmIJAMKUSBR8vFUf8tI3ucNWsWMRHJeRonCj9nSZKyQ6FKZgAC_Ki-jDuMSZ2GaXCmlZ_S1BuShH1eoOaNd50nRRZHavYJ3QDdRcqz68RyedYh68j6GKDkmsnXJok1f0nzlh6CfSxSWCG0mkZ2dp0B2qjSwnFIWvT-CeCDQRLv8Afclp2JpVAqEsPYhhe87Q"
#transcript_json_url = "https://storage.cloud.google.com/citeit_speech_text/freakonomics/280-why-is-my-life-so-hard-times-original.json"

#response = requests.get(transcript_json_url)
#text = json.loads(response.text)
#data = json.dumps(text)
#output = json.loads(data)

with open('examples/freakonomics/280-why-is-my-life-so-hard/280-why-is-my-life-so-hard-times-original.json') as json_file:  
    output = json.load(json_file)

transcript_list = []
word_times = []

for root_key in output:
    if (root_key == 'response'):
        for results_cnt, results in enumerate(output[root_key]['results']):
            for alt in results['alternatives']:
                transcript_list.append(alt['transcript'])
                for word in alt['words']:
                    word_dict = {
                        'word': word['word'],
                        'startTime': word['startTime'],
                        'endTime': word['endTime']
                    }
			
                    word_times.append(word_dict)
transcript = ''.join(transcript_list)

with open("transcript.md", "w") as text_file:
  text_file.write(transcript)

for word in word_times:
  print(word['word'], ': ' , word['startTime'])

json_output = {
    'meta' : {
        'title': '| FreaKonomics',
        'web_story_uri': 'https://medium.com/conversations-with-tyler/malcolm-gladwell-podcast-outliers-tyler-cowen-3abdf99068ee',
        'web_transcript_uri': 'https://medium.com/conversations-with-tyler/malcolm-gladwell-podcast-outliers-tyler-cowen-3abdf99068ee',
        'transcript_json_uri': 'https://storage.googleapis.com/citeit_speech_text/malcolm-gladwell-transcript.json',
        'transcript_json_times_uri': 'https://storage.googleapis.com/citeit_speech_text/malcolm-gladwell-transcript-times.json',
        'audio_story_uri': 'https://storage.googleapis.com/citeit_speech_text/malcolm-gladwell.mp3',
        'web_series_uri': 'https://medium.com/conversations-with-tyler',
        'video_uri': 'https://www.youtube.com/watch?v=ehlhrqSWPbo',
        'video_channel_name': 'Mercatus Center',
        'video_channel_uri': 'https://www.youtube.com/channel/UCKtFwcQCsl1ttW2CgOqFMUQ',
    },
    'word_times': word_times
}

with open('why-is-my-life-so-hard-times.json', 'w') as transcript_times:
  json.dump(json_output, transcript_times)
