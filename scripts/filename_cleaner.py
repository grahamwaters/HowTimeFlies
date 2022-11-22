import os
import pandas as pd


def clean_photo_names(folder, filenames_dict):
    # get the list of files in the folder
    try:
        files = os.listdir(folder)
        # loop through the files
        for file in files:
            if file == '.DS_Store':
                continue
            original_name = file
            # remove " from the file name
            # lowercase the file name
            # replace spaces with underscores
            # replace dashes with underscores
            # replace commas with underscores
            # if the name is too long save the original in the "filenames_dict" as the value, and shorten the name to the first 50 characters and save that as the key in the "filenames_dict" then save the dict to csv in the data folder.
            try:
                file = file.replace('"', "")
            except Exception as e:
                pass
            try:
                file = file.lower()
            except Exception as e:
                pass
            try:
                file = file.replace(" ", "_")
            except Exception as e:
                pass
            try:
                file = file.replace(",", "_")
            except Exception as e:
                pass
            try:
                file = file.replace("-", "_")
            except Exception as e:
                pass
            try:
                file = file.replace("(", "_")
            except Exception as e:
                pass
            try:
                file = file.replace(")", "_")
            except Exception as e:
                pass
            # keep the file extension
            file_extension = file.split(".")[-1]
            # remove the file extension from the file name
            file = file.replace("." + file_extension, "")
            # if the file name is too long, shorten it to the first 50 characters
            # remove . from the file name
            file = file.replace(".", "")
            if len(file) > 30:
                # save the original name in the dict
                filenames_dict[file] = file
                # shorten the name to the first 50 characters
                file = file[:30]

            # add the file extension back to the file name
            if file_extension != "":
                file = file + "." + file_extension
            else: # add .jpg to the file name
                file = file + ".jpg"
            # rename the file
            os.rename(folder + "/" + original_name, folder + "/" + file)
        # save the dict to csv in the data folder
        df = pd.DataFrame.from_dict(filenames_dict, orient="index")
        df.to_csv("./data/filenames.csv")
    except Exception as e:
        print(e)

def main():
    print(f'Running {__file__}')
    # run the clean_photo_names function
    filenames_dict = {} # store original names in a csv file
    for folder in os.listdir("./images"):
        clean_photo_names("./images/" + folder, filenames_dict)


if __name__ == "__main__":
    main()