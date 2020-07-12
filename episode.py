from urllib.parse import urlparse
from urllib.parse import parse_qs
import csv
import subprocess
import webvtt
import tldextract


class Episode(object):
    
    def __init__(self, series_path, episode_path, title, language, episode, web_url, audio_url, video_url):
    
        self.series_path = series_path
        self.episode_path = episode_path
        self.title = title
        self.language = language
        self.episode = episode
        self.web_url = web_url
        self.audio_url = audio_url
        self.video_url = video_url
    
    def create_transcript_json(self):
        if episode.video_format == 'YouTube':
            episode.download_transcript()
            episode.convert_transcript()
            episode.save_transcript_json
        else:
            episode.download_audio()                
            episode.convert_audio()
            operation_id = episode.upload_audio_to_cloud()
            episode.get_original_json(operation_id)

    def video_domain(self):
        url_parts = tldextract.extract(self.video_url)
        return url_parts

    def video_format(self):
        url_parts = self.video_domain()
        if ((url_parts.domain == 'youtube') and (url_parts.suffix == 'com')):
            return "YouTube"
        elif ((url_parts.domain == 'youtu') and (url_parts.suffix == 'be')):
            return "YouTube"
        elif ((url_parts.domain == 'vimeo') and (url_parts.suffix == 'com')):         
            return "Vimeo"
        else:
            return ""
            
    def video_id(self):
        if self.video_format() == "YouTube":
            return youtube_video_id(self.video_url)

        # Credit: https://stackoverflow.com/questions/15296719/python-regex-extract-vimeo-id-from-url            
        elif self.video_format == "Vimeo":
            return urlparse(self.video_url).path.lstrip("/")

        else:
            return ""
        
    def vtt_file_path(self):
        return "transcript_vtt/transcript_" + self.video_id() + ".vtt"
        
    def download_transcript(self):
        file_output = open(self.vtt_file_path(), "w")
        if video_format == 'YouTube':
            subprocess.call(["youtube-dl","–skip-download","–write-auto-sub", self.video_url()], stdout=file_output) 
        pass

    def transcript(self):
        vtt = webvtt.read(self.vtt_file_path())
        transcript = ""

        lines = []
        for line in vtt:
            lines.extend(line.text.strip().splitlines())

        previous = None
        for line in lines:
            if line == previous:
               continue
            transcript += " " + line
            previous = line
            
        return transcript
    
    def save_transcript(self):
        transcript_path = "transcript/transcript_" + self.self.video_id() + ".txt"
        with open(transcript_path) as file:
            file.write(self.transcript())

    def transcript_json(self):
        vtt_filepath = self.vtt_file_path()
        word_times = []
        meta = {
            "title": "",
            "web_story_uri": "",
            "web_transcript_uri": "",
            "transcript_json_uri": "",
            "transcript_json_times_uri": "",
            "audio_story_uri": "",
            "web_series_uri": "",
            "video_uri": "",
            "video_channel_name": "",
            "video_channel_uri": ""
        }
        for transcript in webvtt.read(vtt_filepath):
            word = {
                'word' : transcript.text,
                'startTime': transcript.start,
                'endTime': transcript.end
            }
            word_times.append(word)

        json_data = {
            'meta': meta,
            'word_times' : word_times
        }
        return json_data

    def json_url(self):
        return "json-url"

    def download_audio(self):
        pass
    
    def convert_audio(self):
        pass
        
    def submit_audio_to_speech_text(self):
        operation_id = 123
        return operation_id
    
    def get_original_json(operation_id):
        json = 'describe(operation_id)'
        


with open('data/audio-list.csv') as csv_file:
    #        series_path, episode_path, title, language, episode, web_url, audio_url, youtube_url, operation_id, time, audio, timings
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('Column names are: ' , ''.join(row))
            line_count += 1
        else:
            print("Episode")
            episode = Episode(row['series_path'], row['episode_path'], row['title'], row['language'], row['episode'], row['web_url'], row['audio_url'], row['video_url'])
            episode_json = episode.transcript_json()
            episode_json_url = episode.json_url()
            episode_transcript = episode.transcript() 
            print("Transcript", episode_transcript)
            line_count += 1
    print('Processed ', line_count ,' lines.')







def youtube_video_id(value):
    # Credit: https://stackoverflow.com/questions/4356538/how-can-i-extract-video-id-from-youtubes-link-in-python
    
    """
    Examples:
    - http://youtu.be/SA2iWivDJiE
    - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
    - http://www.youtube.com/embed/SA2iWivDJiE
    - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
    """
    query = urlparse(value)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = parse_qs(query.query)
            return p['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    # fail?
    return None
