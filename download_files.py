from urllib import request

google_url = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'  # file to download


def download_data(csv_url):
    response = request.urlopen(csv_url)  # opens URL
    csv = response.read()  # reads data in file
    csv_str = str(csv)  # converts to string
    lines = csv_str.split(" \\n")  # breaks the string

    # make a file on computer
    destination_file = r'goog.csv'  # r stands for raw string
    fr = open(destination_file, "w")

    # writing to the file
    for line in lines:
        fr.write(line + "\n")

    fr.close()


download_data(google_url)
