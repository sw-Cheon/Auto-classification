import os, time
from PIL import Image
from PIL.ExifTags import TAGS

class RENAME_PHOTO_SEQUENTIALLY():

    def __init__(self):
        self.home = os.path.expanduser('~')
        self.currnent_Working_Directory = os.getcwd()
        self.desktop = self.home + "\Desktop"
        self.CWD = self.currnent_Working_Directory
        self.month_Dictionary = {'Jan': '01', 'Feb': '02', 'Mar': '03',
                                 'Apr': '04', 'May': '05', 'Jun': '06',
                                 'Jul': '07', 'Aug': '08', 'Sep': '09',
                                 'Oct': '10', 'Nov': '11', 'Dec': '12'}
        self.directory = "{}/photo".format(self.desktop)
        self.files = os.listdir(self.directory)
        for content in self.files:
            num = 0
            num += 1
            if (content == "desktop.ini"):
                print(self.files[num])
                self.files.pop(num)

        self.save_List = []
        self.Count = 0
        self.FLAG_GIF = False

    def get_Exif(self, filename):
        image = Image.open(filename)
        image.verify()
        return image._getexif()

    def renaming_Function_Photo(self):
        for file in self.files:
            Number = 1
            splited_File_Type = file.split('.')[1]
            if (splited_File_Type == "gif"):
                self.FLAG_GIF = True
            else:
                try:
                    exif = self.get_Exif("{}/{}".format(self.directory, file))
                    splited_Date_From_Time = exif[36868].split(" ")
                    splited_Date_Data = splited_Date_From_Time[0].split(":")
                    renamed_File = "{}{}{}_{}".format(splited_Date_Data[0], splited_Date_Data[1], splited_Date_Data[2], Number)
                    for content in self.save_List:
                        if (content == renamed_File):
                            Number += 1
                            renamed_File = "{}{}{}_{}".format(splited_Date_Data[0], splited_Date_Data[1], splited_Date_Data[2], Number)
                    self.save_List.append(renamed_File)
                except Exception as e:
                    if (exif != None):
                        unconvertable_File = "{}/{}".format(self.directory, file)
                        Times = time.ctime(os.path.getmtime(unconvertable_File))
                        splited_Time_Data = Times.split(' ')
                        if (len(splited_Time_Data) == 6):
                            splited_Time_Data.pop(2)
                        if (len(splited_Time_Data[2]) == 1):
                            add_Zero = "0{}".format(splited_Time_Data[2])
                            renamed_File = "{}{}{}_{}".format(splited_Time_Data[4], self.month_Dictionary[splited_Time_Data[1]], add_Zero, Number)
                            for content in self.save_List:
                                if (content == renamed_File):
                                    Number += 1
                                    renamed_File = "{}{}{}_{}".format(splited_Time_Data[4], self.month_Dictionary[splited_Time_Data[1]], add_Zero, Number)
                        else:
                            renamed_File = "{}{}{}_{}".format(splited_Time_Data[4], self.month_Dictionary[splited_Time_Data[1]], splited_Time_Data[2], Number)
                            for content in self.save_List:
                                if (content == renamed_File):
                                    Number += 1
                                    renamed_File = "{}{}{}_{}".format(splited_Time_Data[4], self.month_Dictionary[splited_Time_Data[1]], splited_Time_Data[2], Number)
                        self.save_List.append(renamed_File)

                    elif (exif == None):
                        nonetype_File = "{}/{}".format(self.directory, file)
                        Times = time.ctime(os.path.getmtime(nonetype_File))
                        splited_Time_Data = Times.split(' ')
                        if (len(splited_Time_Data) == 6):
                            splited_Time_Data.pop(2)
                        if (len(splited_Time_Data[2]) == 1):
                            add_Zero = "0{}".format(splited_Time_Data[2])
                            renamed_File = "{}{}{}_{}".format(splited_Time_Data[4], self.month_Dictionary[splited_Time_Data[1]], add_Zero, Number)
                            for content in self.save_List:
                                if (content == renamed_File):
                                    Number += 1
                                    renamed_File = "{}{}{}_{}".format(splited_Time_Data[4], self.month_Dictionary[splited_Time_Data[1]], add_Zero, Number)
                        else:
                            renamed_File = "{}{}{}_{}".format(splited_Time_Data[4], self.month_Dictionary[splited_Time_Data[1]], splited_Time_Data[2], Number)
                            for content in self.save_List:
                                if (content == renamed_File):
                                    Number += 1
                                    renamed_File = "{}{}{}_{}".format(splited_Time_Data[4], self.month_Dictionary[splited_Time_Data[1]], splited_Time_Data[2], Number)
                        self.save_List.append(renamed_File)

            if (self.FLAG_GIF == True):
                nonetype_File = "{}/{}".format(self.directory, file)
                Times = time.ctime(os.path.getmtime(nonetype_File))
                splited_Time_Data = Times.split(' ')
                if (len(splited_Time_Data) == 6):
                    splited_Time_Data.pop(2)
                if (len(splited_Time_Data[2]) == 1):
                    add_Zero = "0{}".format(splited_Time_Data[2])
                    renamed_File = "{}{}{}_{}".format(splited_Time_Data[4], self.month_Dictionary[splited_Time_Data[1]], add_Zero, Number)
                    for content in self.save_List:
                        if (content == renamed_File):
                            Number += 1
                            renamed_File = "{}{}{}_{}".format(splited_Time_Data[4], self.month_Dictionary[splited_Time_Data[1]], add_Zero, Number)
                else:
                    renamed_File = "{}{}{}_{}".format(splited_Time_Data[4], self.month_Dictionary[splited_Time_Data[1]], splited_Time_Data[2], Number)
                    for content in self.save_List:
                        if (content == renamed_File):
                            Number += 1
                            renamed_File = "{}{}{}_{}".format(splited_Time_Data[4], self.month_Dictionary[splited_Time_Data[1]], splited_Time_Data[2], Number)
                self.save_List.append(renamed_File)

            if (self.FLAG_GIF == False):
                os.rename("{}/{}".format(self.directory, self.files[self.Count]), "{}/{}.jpg".format(self.directory, renamed_File))
            else:
                os.rename("{}/{}".format(self.directory, self.files[self.Count]), "{}/{}.gif".format(self.directory, renamed_File))
                self.FLAG_GIF = False
            self.Count += 1

class RENAME_VIDEO_SEQUENTIALLY():

    def __init__(self):
        self.home = os.path.expanduser('~')
        self.currnent_Working_Directory = os.getcwd()
        self.desktop = self.home + "\Desktop"
        self.CWD = self.currnent_Working_Directory
        self.month_Dictionary = {'Jan': '01', 'Feb': '02', 'Mar': '03',
                                'Apr': '04', 'May': '05', 'Jun': '06',
                                'Jul': '07', 'Aug': '08', 'Sep': '09',
                                'Oct': '10', 'Nov': '11', 'Dec': '12'}
        self.Count = 0
        self.directory = "{}/video".format(self.desktop)
        self.files = os.listdir(self.directory)
        self.save_List = []

    def renaming_Function_Video(self):
        for file in self.files:
            Number = 1
            Times = time.ctime(os.path.getmtime("{}/{}".format(self.directory, file)))
            splited_Time_Data = Times.split(' ')
            if (len(splited_Time_Data) == 6):
                splited_Time_Data.pop(2)
            renamed_File = "{}{}{}_{}".format(splited_Time_Data[4], self.month_Dictionary[splited_Time_Data[1]], splited_Time_Data[2], Number)
            for content in self.save_List:
                if (content == renamed_File):
                    Number += 1
                    renamed_File = "{}{}{}_{}".format(splited_Time_Data[4], self.month_Dictionary[splited_Time_Data[1]], splited_Time_Data[2], Number)
            self.save_List.append(renamed_File)
            os.rename("{}/{}".format(self.directory, self.files[self.Count]), "{}/{}.mp4".format(self.directory, renamed_File))
            self.Count += 1