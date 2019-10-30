"""
Takes one or more input .json file containing the following fields:
    - videos: a list of paths to video files to work on (should be in order for concatenation)
    - output_name: the name of the output video file to be saved
    - output_bitrate: The bitrate of the output video file. 
        	          This corresponds to the quality of the output video

It compresses, concatenates and saves the resulting video.

Usage:

$ python video_preprocess.py input1.json

[or]

$ python video_preprocess.py input1.json input2.json inputn.json

[or]

$ python video_preprocess.py somefolder/inputjson.json
"""
import sys
import moviepy.editor as mp
import json


def json_to_dict(file_path):
    """
    Given a path to a JSON file, returns a dictionary containing
    The contents of that file
    
    Params:
        - file_path: the path to the JSON file
    """
    with open(file_path) as f:
        output = json.load(f)
    return output


def main(videos, output_name="output.mp4", output_bitrate="500k"):
    """
    Takes a list of video paths. It compresses them to a specified bitrate
    and concatenates them together and saving them to a file

    Parameters:
        - videos: a list of paths to video files to work on (should be in order for concatenation)
        - output_name: the name of the output video file to be saved
        - output_bitrate: The bitrate of the output video file. 
                          This corresponds to the quality of the output video 
    """
    videos = list(map(lambda x: mp.VideoFileClip(x), videos))
    concattenated_video = mp.concatenate_videoclips(videos)
    concattenated_video.write_videofile(output_name, bitrate=output_bitrate)


if __name__ == "__main__":
    for input_json in sys.argv[1:]:
        config_options = json_to_dict(input_json)
        main(
            videos=config_options["videos"],
            output_name=config_options["output_name"],
            output_bitrate=config_options["output_bitrate"],
        )
