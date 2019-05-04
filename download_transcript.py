import webvtt
import pprint

# Credit: https://shkspr.mobi/blog/2018/09/convert-webvtt-to-a-transcript-using-python/


vtt_filepath = 'examples/youtube/iKvFlSedpNI_malcolm-gladwell-on-income-inequality/iKvFlSedpNI_malcom_gladwell_on_income_inequality.en.vtt'
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

vtt = webvtt.read(vtt_filepath)

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

print(transcript)
