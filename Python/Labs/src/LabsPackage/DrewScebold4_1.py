import re
import csv

def main():
    emailDict = {}
    infile = open("files/input.txt", "r")
    outfile = open("files/output.csv", "w", newline="")
    outText = open("output.txt", "w")
    csvWriter = csv.writer(outfile)
    tot = 0
    decTot = 0.0
    totEmails = 0
    for line in infile:
        if line.startswith("From:"):
            totEmails += 1
            email = re.findall("\S+@\S+", line)[0]
            emailDict[email] = emailDict.get(email, 0) + 1
            # if email in emailDict:
            #     emailDict[email] = emailDict[email] + 1
            # else:
            #     emailDict[email] = 1

        elif line.startswith("X-DSPAM-Confidence:"):
            outText.write(line)
            dec = float(re.findall("[0-9.]+", line)[0])
            decTot += dec
            tot += 1
    csvWriter.writerow(["Email" ,"Count"])
    for key in emailDict:
        csvWriter.writerow([key, emailDict[key]])
    csvWriter.writerow(["TOTAL", totEmails])
    outText.write("-------------------------------------------------\n")
    outText.write(f"Total dspam confidence = {decTot:.2f}\n")
    outText.write(f"Average dspam confidence = {decTot/tot:.2f}\n")
    outText.close()
    outfile.close()
    infile.close()


if __name__ == '__main__':
    main()