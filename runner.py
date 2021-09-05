from helper import Helper

helper = Helper("audioFiles", {}, "audioFiles.json")

def test_runner():
    helper.play_mp3_from_folder_and_then_label_it()
    helper.json_parser()

test_runner()