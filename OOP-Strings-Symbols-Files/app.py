from smart_string import SmartString


def start_process():
    engine = SmartString("mock_data.txt", "exception")

    engine.read_file()
    print(engine.file_content, end="\n\n")
    print(engine.get_special_sentences())


if __name__ == "__main__":
    start_process()
