import re
import csv
import os.path


def main():
    # Logic for input file
    fileName = input("Input file name: ").strip()
    while True:
        try:
            infile = open("files/" + fileName, "r")
        except FileNotFoundError:
            print("File does not exist!")
            fileName = input("Input file name: ").strip()
        else:
            break
    # Logic for output file

    # match = re.search(".csv\Z", newFile)
    # while not match:
    #     newFile = input("The new file name does not end with .csv. Enter a valid file name: ")
    #     match = re.search(".csv\Z", newFile)
    newFile = input("Output file name: ").strip()
    while os.path.isfile(f"files/{newFile}"):
        overwrite = input(f"Overwrite existing file (y/n): ").strip().lower()
        while overwrite != "y" and overwrite != "n":
            overwrite = input("invalid (y/n): ").strip().lower()
        if overwrite == "y":
            break
        else:
            newFile = input("New output file name: ").strip()
    outfile = open(f"files/{newFile}", "w", newline="")

    csvWriter = csv.writer(outfile)
    csvWriter.writerow(["Email", "Subject", "Confidence"])

    for line in infile:
        if line.startswith("From:"):
            email = re.findall("\S+@\S+", line)[0]
        if line.startswith("Subject:"):
            sub = re.findall("r[0-9]+", line)[0]
        if line.startswith("X-DSPAM-Confidence:"):
            con = float(re.findall("\.[0-9]+", line)[0])
            csvWriter.writerow([email, sub, con])

    print("Data Stored!")
    outfile.close()
    infile.close()


if __name__ == '__main__':
    main()
