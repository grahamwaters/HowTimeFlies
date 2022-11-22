import os



def clean_photo_names(folder, filenames_dict):
    # get the list of files in the folder
    files = os.listdir(folder)
    # loop through the files
    for file in files:
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

        if len(file) > 50:
            # save the original name in the dict
            filenames_dict[file] = file
            # shorten the name to the first 50 characters
            file = file[:50]
        # rename the file
        os.rename(folder + "/" + file, folder + "/" + file)
    # save the dict to csv in the data folder
    filenames_dict.to_csv("../data/filenames_dict.csv")


def main():
    print(f'Running {__file__}')
    # run the clean_photo_names function
    filenames_dict = {} # store original names in a csv file
    for folder in os.listdir("../data/images"):
        clean_photo_names("../data/images/" + folder, filenames_dict)


if __name__ == "__main__":
    main()