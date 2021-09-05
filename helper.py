import os
from playsound import playsound
import json

class Helper:
    def __init__(self, mp3_directory, dictionary_for_json, json_for_audio_file):
        self.__mp3_directory = mp3_directory
        self.__dictionary_for_json = dictionary_for_json
        self.__json_for_audio_file = json_for_audio_file

    def play_mp3_from_folder_and_then_label_it(self):
        for file_name in os.listdir(self.__mp3_directory):
            file_path = os.path.join(self.__mp3_directory, file_name)
            playsound(file_path)
            label = input("write noisy or clean as n/c ")
            if label == "n" or label == "c":
                self.__dictionary_for_json[file_name] = label
            else:
                raise ValueError("invalid input try again write only n or c")

    def json_parser(self):
        json_object = json.dumps(self.__dictionary_for_json)
        with open(self.__json_for_audio_file, "w") as outFile:
            outFile.write(json_object)