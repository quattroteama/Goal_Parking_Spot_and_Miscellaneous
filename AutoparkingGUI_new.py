from PySide import QtCore, QtGui, QtUiTools
import sys, math
import subprocess


ipaddress = sys.argv[1]
buttons = [16 ,15, 14 ,13, 12, 11, 10, 9, 12, 11, 11, 10, 9, 8, 7, 1, 2, 3, 4, 5, 6]
button_data = [16 ,15, 14 ,13, 12, 11, 10, 9, 12, 11, 11, 10, 9, 8, 7, 1, 2, 3, 4, 5, 6]


# goal = [[300,101], [300, 151], [300, 201], [300, 251], [150,101],[150,151],[150,201],[150,251], [407, 299], [407, 349], [407, 399],[407, 449], [320, 459],[270, 459],[220, 459], [0,101],[0,151],[0,201],[0,251],[0,301],[0,351]]
#origin_x = 550
#origin_y = 65

#x = ["300", "300", "300", "300", "150", "150", "150", "150", "407", "407", "407", "407", "320", "270", "220", "0", "0", "0", "0", "0", "0"]
#y = ["101", "151", "201", "251", "101", "151", "201", "251", "299", "349", "399", "449", "459", "459", "459", "101","151", "201", "251","301", "351"]

origin_x = 0
origin_y = 0
x = ["235","235","235","235","385","385","385","385","140","140","140","140","220","270","320","540","540","540","540","540","540"]
y = ["150","200","250","300","150","200","250","300","340","390","440","490","515","515","515","150","200","250","300","350","400"]

goal_x = []
goal_y = []

for i in range (0,len(x)):
    #goal_x = goal_x + [origin_x - int(x[i])]
    #goal_y = goal_y + [origin_y + int(y[i])]
    goal_x = goal_x + [origin_x + int(x[i])]
    goal_y = goal_y + [origin_y + int(y[i])]	
	

def loadUiWidget(uifilename, parent=None):
    loader = QtUiTools.QUiLoader()
    uifile = QtCore.QFile(uifilename)
    uifile.open(QtCore.QFile.ReadOnly)
    ui = loader.load(uifile, parent)
    uifile.close()
    return ui


def main():
    global buttons
    global button_data
    def checkButton(clicked): # clicked is only a boolean variable name, can be any name

        if (clicked):
            buttons[0] = 100
        else: 
            buttons[0] = button_data[0]


        print "clicked"

    def checkButton1(clicked): # clicked is only a boolean variable name, can be any name

        if (clicked):
            buttons[1] = 100
        else: 
            buttons[1] = button_data[1]


        print "clicked"
    def checkButton2(clicked):

        if (clicked):
            buttons[2] = 100
        else: 
            buttons[2] = button_data[2]

        print clicked
    def checkButton3(clicked):

        if (clicked):
            buttons[3] = 100
        else: 
            buttons[3] = button_data[3]

        print "clicked"    
    def checkButton4(clicked):

        if (clicked):
            buttons[4] = 100
        else: 
            buttons[4] = button_data[4]

        print "clicked"
    def checkButton5(clicked):

        if (clicked):
            buttons[5] = 100
        else: 
            buttons[5] = button_data[5]

        print "clicked"
    def checkButton6(clicked):

        if (clicked):
            buttons[6] = 100
        else: 
            buttons[6] = button_data[6]

        print "clicked"
    def checkButton7(clicked):

        if (clicked):
            buttons[7] = 100
        else: 
            buttons[7] = button_data[7]

        print "clicked"
    def checkButton8(clicked):

        if (clicked):
            buttons[8] = 100
        else: 
            buttons[8] = button_data[8]

        print "clicked"
    def checkButton9(clicked):

        if (clicked):
            buttons[9] = 100
        else: 
            buttons[9] = button_data[9]

        print "clicked"
    def checkButton10(clicked):

        if (clicked):
            buttons[10] = 100
        else: 
            buttons[10] = button_data[10]

        print "clicked"
    def checkButton11(clicked):

        if (clicked):
            buttons[11] = 100
        else: 
            buttons[11] = button_data[11]

        print "clicked"
    def checkButton12(clicked):

        if (clicked):
            buttons[12] = 100
        else: 
            buttons[12] = button_data[12]

        print "clicked"
    def checkButton13(clicked):

        if (clicked):
            buttons[13] = 100
        else: 
            buttons[13] = button_data[13]

        print "clicked"
    def checkButton14(clicked):

        if (clicked):
            buttons[14] = 100
        else: 
            buttons[14] = button_data[14]

        print "clicked"
    def checkButton15(clicked):

        if (clicked):
            buttons[15] = 100
        else: 
            buttons[15] = button_data[15]

        print "clicked"
    def checkButton16(clicked):

        if (clicked):
            buttons[16] = 100
        else: 
            buttons[16] = button_data[16]

        print "clicked"
    def checkButton17(clicked):

        if (clicked):
            buttons[17] = 100
        else: 
            buttons[17] = button_data[17]

        print "clicked"
    def checkButton18(clicked):

        if (clicked):
            buttons[18] = 100
        else: 
            buttons[18] = button_data[18]

        print "clicked"
    def checkButton19(clicked):

        if (clicked):
            buttons[19] = 100
        else: 
            buttons[19] = button_data[19]
        print "clicked"
    def checkButton20(clicked):

        if (clicked):
            buttons[20] = 100
        else: 
            buttons[20] = button_data[20]

        print "clicked"


# find the button that has the nearest distance from entrance
    def findGoalButton(clicked):
        # QPixmap pixmap(":/rsz_goal.jpg")
         # find the nearest button
        goalButtonIndex = buttons.index(min(buttons)) 

        # save the nearest spot to txt file 
        file = open("goalCoordinate.txt", "w")
        file.write(str(float(goal_x[goalButtonIndex])/100))
        file.write('\n')
        file.write(str(float(goal_y[goalButtonIndex])/100))
        file.write('\n')
        file.write("0")

        # reach parking spot but don't align to the parking lines
        # for the 18 spots, the orientation is 1/sqrt2 1/sqrt2 1/sqrt2 1/sqrt2 
        if (goalButtonIndex == 8) or (goalButtonIndex == 9) or (goalButtonIndex == 10) or (goalButtonIndex == 11) or (goalButtonIndex == 12) or (goalButtonIndex ==  13) or (goalButtonIndex == 14):
            # orientation_1 = ["\n", "value", "\n", "value","\n", "value","\n", "value"]
            file.write("\n")
            file.write("180")
        # the 3 farthest spots, the orientation is 1 1 1 0
        elif (goalButtonIndex == 15) or (goalButtonIndex == 16) or (goalButtonIndex == 17) or (goalButtonIndex == 18) or (goalButtonIndex == 19) or (goalButtonIndex == 20):
            # orientation_2 = ["\n", "1", "\n", "1","\n", "1","\n", "0"]
            file.write("\n")
            file.write("90")
        else:
            file.write("\n")
            file.write("-90")

        # reach and align to the parking lines 
        # for the 18 spots, the orientation is 1 1 1 0
        # if goalButtonIndex != 12| 13| 14
        # orientation_1 = ["\n", "1", "\n", "1","\n", "1","\n", "0"]
        # file.write(orientation_1)

        # for the 3 farthest spots, the orientation is -1/sqrt2 -1/sqrt2 -1/sqrt2 1/sqrt2 
        # else
        # orientation_2 = ["\n", "-value", "\n", "-value","\n", "-value","\n", "value"]
        # file.write(orientation_2)

        file.close()


        # show on GUI 
        print 'Goal : '+ str(goalButtonIndex)
        if goalButtonIndex == 0:
            MainWindow.label_2.setStyleSheet("QLabel { background-color: yellow}")

        else:
            MainWindow.label_2.setStyleSheet("QLabel { background-color: QBrush()}")

        if goalButtonIndex == 1:
            MainWindow.label_3.setStyleSheet("QLabel { background-color: yellow}")
        else:
            MainWindow.label_3.setStyleSheet("QLabel { background-color: QBrush()}")

        if goalButtonIndex == 2:
            MainWindow.label_4.setStyleSheet("QLabel { background-color: yellow}")
        else:
            MainWindow.label_4.setStyleSheet("QLabel { background-color: QBrush()}")

        if goalButtonIndex == 3:
            MainWindow.label_5.setStyleSheet("QLabel { background-color: yellow}")
        else:
            MainWindow.label_5.setStyleSheet("QLabel { background-color: QBrush()}")

        if goalButtonIndex == 4:
            MainWindow.label_6.setStyleSheet("QLabel { background-color: yellow}")
        else:
            MainWindow.label_6.setStyleSheet("QLabel { background-color: QBrush()}")

        if goalButtonIndex == 5:
            MainWindow.label_7.setStyleSheet("QLabel { background-color: yellow}")
        else:
            MainWindow.label_7.setStyleSheet("QLabel { background-color: QBrush()}")

        if goalButtonIndex == 6:
            MainWindow.label_8.setStyleSheet("QLabel { background-color: yellow}")
        else:
            MainWindow.label_8.setStyleSheet("QLabel { background-color: QBrush()}")

        if goalButtonIndex == 7:
            MainWindow.label_9.setStyleSheet("QLabel { background-color: yellow}")
        else:
            MainWindow.label_9.setStyleSheet("QLabel { background-color: QBrush()}")

        if goalButtonIndex == 8:
            MainWindow.label_10.setStyleSheet("QLabel { background-color: yellow}")
        else:
            MainWindow.label_10.setStyleSheet("QLabel { background-color: QBrush()}")

        if goalButtonIndex == 9:
            MainWindow.label_11.setStyleSheet("QLabel { background-color: yellow}")
        else:
            MainWindow.label_11.setStyleSheet("QLabel { background-color: QBrush()}")

        if goalButtonIndex == 10:
            MainWindow.label_12.setStyleSheet("QLabel { background-color: yellow}")
        else:
            MainWindow.label_12.setStyleSheet("QLabel { background-color: QBrush()}")

        if goalButtonIndex == 11:
            MainWindow.label_13.setStyleSheet("QLabel { background-color: yellow}")
        else:
            MainWindow.label_13.setStyleSheet("QLabel { background-color: QBrush()}")

        if goalButtonIndex == 12:
            MainWindow.label_14.setStyleSheet("QLabel { background-color: yellow}")
        else:
            MainWindow.label_14.setStyleSheet("QLabel { background-color: QBrush()}")

        if goalButtonIndex == 13:
            MainWindow.label_15.setStyleSheet("QLabel { background-color: yellow}")
        else:
            MainWindow.label_15.setStyleSheet("QLabel { background-color: QBrush()}")
        if goalButtonIndex == 14:
            MainWindow.label_16.setStyleSheet("QLabel { background-color: yellow}")
        else:
            MainWindow.label_16.setStyleSheet("QLabel { background-color: QBrush()}")
        if goalButtonIndex == 15:
            MainWindow.label_17.setStyleSheet("QLabel { background-color: yellow}")
        else:
            MainWindow.label_17.setStyleSheet("QLabel { background-color: QBrush()}")
        if goalButtonIndex == 16:
            MainWindow.label_18.setStyleSheet("QLabel { background-color: yellow}")
        else:
            MainWindow.label_18.setStyleSheet("QLabel { background-color: QBrush()}")
        if goalButtonIndex == 17:
            MainWindow.label_19.setStyleSheet("QLabel { background-color: yellow}")
        else:
            MainWindow.label_19.setStyleSheet("QLabel { background-color: QBrush()}")

        if goalButtonIndex == 18:
            MainWindow.label_20.setStyleSheet("QLabel { background-color: yellow}")
        else:
            MainWindow.label_20.setStyleSheet("QLabel { background-color: QBrush()}")
        if goalButtonIndex == 19:
            MainWindow.label_21.setStyleSheet("QLabel { background-color: yellow}")
        else:
            MainWindow.label_21.setStyleSheet("QLabel { background-color: QBrush()}")
        if goalButtonIndex == 20:
            MainWindow.label_22.setStyleSheet("QLabel { background-color: yellow}")
        else:
            MainWindow.label_22.setStyleSheet("QLabel { background-color: QBrush()}")


        # change the color of goal button label to yellow 
        #MainWindow.label_2.setAutoFillBackground(True) 
        #color  = QtGui.QColor(255, 0, 0)
        #MainWindow.label_2.setStyleSheet("QLabel { background-color: 
	subprocess.call(['python','serv.py', ipaddress])  



    app = QtGui.QApplication(sys.argv)
    MainWindow = loadUiWidget("AutoparkingGUI_topdownview.ui")
    wid = QtGui.QWidget()
    MainWindow.show()

    MainWindow.checkBox.clicked[bool].connect(checkButton)
    MainWindow.checkBox_1.clicked[bool].connect(checkButton1)
    MainWindow.checkBox_2.clicked[bool].connect(checkButton2)
    MainWindow.checkBox_3.clicked[bool].connect(checkButton3)
    MainWindow.checkBox_4.clicked[bool].connect(checkButton4)
    MainWindow.checkBox_5.clicked[bool].connect(checkButton5)
    MainWindow.checkBox_6.clicked[bool].connect(checkButton6)
    MainWindow.checkBox_7.clicked[bool].connect(checkButton7)
    MainWindow.checkBox_8.clicked[bool].connect(checkButton8)
    MainWindow.checkBox_9.clicked[bool].connect(checkButton9)
    MainWindow.checkBox_10.clicked[bool].connect(checkButton10)
    MainWindow.checkBox_11.clicked[bool].connect(checkButton11)
    MainWindow.checkBox_12.clicked[bool].connect(checkButton12)
    MainWindow.checkBox_13.clicked[bool].connect(checkButton13)
    MainWindow.checkBox_14.clicked[bool].connect(checkButton14)
    MainWindow.checkBox_15.clicked[bool].connect(checkButton15)
    MainWindow.checkBox_16.clicked[bool].connect(checkButton16)
    MainWindow.checkBox_17.clicked[bool].connect(checkButton17)
    MainWindow.checkBox_18.clicked[bool].connect(checkButton18)
    MainWindow.checkBox_19.clicked[bool].connect(checkButton19)
    MainWindow.checkBox_20.clicked[bool].connect(checkButton20)


    MainWindow.pushButton.clicked[bool].connect(findGoalButton)
    
    
    sys.exit(app.exec_())  
    

if __name__ == '__main__':
    main()
