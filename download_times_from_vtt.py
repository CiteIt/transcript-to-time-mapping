import webvtt
import pprint


word_times = []
vtt_filepath = 'examples/youtube/iKvFlSedpNI_malcom_gladwell_on_income_inequality.en.vtt'
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

pprint.pprint(json_data)
