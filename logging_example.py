import logging


def analyze_signal(filename):
    in_file = open(filename, 'r')
    positives = 0
    total = 0
    while True:
        in_data = in_file.read(1)
        total += 1
        if in_data == "+":
            positives += 1
        elif in_data == "0":
            logging.warning("There was a 0 at position {}".format(total))
        elif in_data == "-":
            logging.info("There was a negative at position {}".format(total))
        elif in_data == "\n":
            break
        else:
            logging.error("There was an {} at position {}".format(in_data,
                                                                  total))
    percentage = positives / total * 100
    print("The answer is {:.2f}".format(percentage))


if __name__ == '__main__':
    logging.basicConfig(filename="signal.log", level=logging.INFO,
                        filemode="w")
    logging.info("Start new run...")
    analyze_signal("signal.txt")
