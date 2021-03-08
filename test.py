import sys
import pyperclip
import time
import random

emoticons = " [怒][怒] "
append_tag = " #陌森代言人肖战竖中指# "
append_at = " @MOLSION陌森眼镜 "
write_set_sentence = list()
write_set_tag = list()
write_set_atID = list()

tag_counter = 2
sentence_counter = 3
txt_counter = 30


def create_txt():
    sentence_set = set()
    for i in range(txt_counter):
        txt_string = write_data() + "\n"
        sentence_set.add(txt_string)
        print(txt_string)
        print("add", i)
        time.sleep(1)
    with open("不糊不走不死不休1.txt", "w") as writer:
        writer.writelines(list(sentence_set))
    writer.close()

    sentence_set = set()
    for i in range(txt_counter):
        txt_string = write_data() + "\n"
        sentence_set.add(txt_string)
        print(txt_string)
        print("add", i)
        time.sleep(1)
    with open("不糊不走不死不休2.txt", "w") as writer:
        writer.writelines(list(sentence_set))
    writer.close()

    sentence_set = set()
    for i in range(txt_counter):
        txt_string = write_data() + "\n"
        sentence_set.add(txt_string)
        print(txt_string)
        print("add", i)
        time.sleep(1)
    with open("不糊不走不死不休3.txt", "w") as writer:
        writer.writelines(list(sentence_set))
    writer.close()

    sentence_set = set()
    for i in range(txt_counter):
        txt_string = write_data() + "\n"
        sentence_set.add(txt_string)
        print(txt_string)
        print("add", i)
        time.sleep(1)
    with open("不糊不走不死不休4.txt", "w") as writer:
        writer.writelines(list(sentence_set))
    writer.close()

    sentence_set = set()
    for i in range(txt_counter):
        txt_string = write_data() + "\n"
        sentence_set.add(txt_string)
        print(txt_string)
        print("add", i)
        time.sleep(1)
    with open("不糊不走不死不休5.txt", "w") as writer:
        writer.writelines(list(sentence_set))
    writer.close()

def write_data():
    clipboard_string = ""
    random.seed(int(time.time()))
    # clipboard_string += append_tag
    # clipboard_string += emoticons
    clipboard_string += append_tag
    clipboard_string += emoticons
    for i in range(tag_counter):
        tag_index = random.randint(0, len(write_set_tag) - 1)
        clipboard_string += write_set_tag[tag_index].replace("\n", " ")
        clipboard_string += emoticons
        break
    for i in range(sentence_counter):
        sentence_index = random.randint(0, len(write_set_sentence) - 1)
        clipboard_string += write_set_sentence[sentence_index].replace(
            "\n", "")
    # clipboard_string += emoticons
    # clipboard_string += append_tag
    clipboard_string += emoticons
    atID_index = random.randint(0, len(write_set_atID) - 1)
    clipboard_string += write_set_atID[atID_index].replace("\n", "")
    clipboard_string += emoticons
    clipboard_string += append_at

    return clipboard_string


def sort_ID():
    ID_set = set()
    with open("authenticatedID_test.txt", "r") as reader:
        line_list = reader.readlines()
    for line in line_list:
        line = line.replace("\'", "")
        # line = line.replace("\n", "")
        ID_set.add(line)
    reader.close()
    with open("ID.txt", "w") as writer:
        writer.writelines(list(ID_set))
    writer.close()


def read_data():
    tag_set = set()
    sentence_set = set()
    with open("sentence_test.txt", "r") as reader:
        line_list = reader.readlines()
    for line in line_list:
        # pyperclip.copy(line)
        line = line.replace("\'", "")
        line = line.replace("\n", "")
        part_list = line.split(' ')
        # print(line)
        for part in part_list:
            # print(len(part))
            # print(part)
            if len(part) == 0:
                continue
            if part[0] == '#' and part[len(part) - 1] == '#':
                tag_set.add(part + "\n")
            elif part[0] == '[' and part[len(part) - 1] == ']':
                continue
            else:
                sentence_list = part.split("。")
                for i in range(len(sentence_list) - 1):
                    sentence_set.add(sentence_list[i] + "。\n")
    reader.close()

    with open("tag.txt", "w") as writer:
        writer.writelines(list(tag_set))
    writer.close()
    with open("sentence.txt", "w") as writer:
        writer.writelines(list(sentence_set))
    writer.close()


if __name__ == '__main__':
    print("data loading... ")
    # global write_set_sentence ,write_set_tag
    with open("sentence.txt", "r") as reader:
        write_set_sentence = reader.readlines()
    with open("tag.txt", "r") as reader:
        write_set_tag = reader.readlines()
    with open("authenticatedID_test.txt", "r") as reader:
        write_set_atID = reader.readlines()
    print("load success")
    while 1:
        action = input(
            "actions: [r]ead, [w]rite, [c]onsecutive, [s]ort, [t]xt file creation or [q]uit:\n")
        if action == 'q':
            print("thanks for using, boycott XZ together~")
            break
        elif action == 'r':
            print("read now")
            read_data()
        elif action == 'w':
            print("write to your clipboard")
            write_data()
        elif action == 'c':
            print("consecutive output")
            consecutive_counter = 32
            # consecutive_counter = 4
            for i in range(consecutive_counter):
                print("output round: ", i)
                clip_string = write_data()
                pyperclip.copy(clip_string)
                time.sleep(2)
        elif action == 's':
            sort_ID()
        elif action == 't':
            create_txt()
        else:
            print("wrong input")
