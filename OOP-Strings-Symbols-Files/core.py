import sys


class SmartString:
    """ Own Data Type Class for working with Strings """
    def __init__(self, file_name: str, chosen_word: str) -> None:
        self.file_name = file_name
        self.chosen_word = chosen_word
        self.file_content = []
        self.special_sentences = []

    def read_file(self) -> None:
        try:
            file = open(file=self.file_name, mode="r")
        except FileNotFoundError:
            print(f"Error: File {self.file_name} is not found.")
            sys.exit()
        except OSError as error:
            print(f"IO Error {error.errno}: {error.strerror}")
            sys.exit()
        else:
            self.file_content = file.read().split(sep=".")
            file.close()

    def get_special_sentences(self) -> list:
        # self.special_sentences = [
        #     self.chosen_word in sentence for sentence in self.file_content
        # ]
        for sentence in self.file_content:
            if self.chosen_word in sentence:
                self.special_sentences.append(sentence)

        return self.special_sentences
