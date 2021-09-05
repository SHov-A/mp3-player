from helper import Helper

# creating object for Helper class
helper = Helper("audioFiles", {}, "audioFiles.json")


# this function provides to run Helper class methods
def test_runner():
    helper.play_mp3_from_folder_and_then_label_it()
    helper.json_parser()


# call test_runner function
test_runner()
