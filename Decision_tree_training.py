__author__='sbp'
'''
@author Saurabh Parekh 
This program writes program which is the code of the decision tree. This program write another program which works like 
decision tree. There are six feature imputs and 2 class classifier. As it is a assignment I am not allowed to share the 
input file but it will worrk pretty well with any kind of data, any number of attributes and any number of classifier we minor 
modification and
'''

import math
decision_list=[]


def endOfFile(file):
    '''

    :param file:
    :return: NOne
    this file writes the end of file of the classifier file. The classifier is acutally an if-else loop created by this
    file. In short this file will write the code for your decision tree.
    The input data has six freatures and based on the features the the given data point is classsified as grehound or
    wippet

    '''
    tabs='\t'
    file.write("with open('input_fillename','w') as myfile:\n")
    file.write(tabs+"for lines in range(len(ans)):\n")
    tabs=tabs+"\t"
    file.write(tabs+"row= ans[lines]\n")
    file.write(tabs+"myfile.write(row)\n")
    file.write(tabs+"myfile.write('\\n')")


def writingStartFileBoiler(file):
    '''
    This function writes the begining of the file.
    :param file:
    :return: None
    '''
    tabs="\t"
    file.write("input1=[]\n")
    file.write("flag=False\n")
    file.write("total_greyhound=0\n")
    file.write("total_wippet=0\n")
    file.write("targets=[]\n")
    file.write("with open('HW_05C_DecTree_TESTING__FOR_STUDENTS__v540.csv') as file:\n")
    file.write(tabs+"for lines in file:\n")
    tabs=tabs+"\t"
    file.write(tabs+"lines = lines.strip().split(',')\n")
    #print(lines)
    file.write(tabs+"if flag == False:\n")
    tabs1=tabs+"\t"
    file.write(tabs1+"flag = True\n")
    file.write(tabs+"else:\n")
    file.write(tabs1+ "input1.append([float(lines[0]), float(lines[1]), float(lines[2]), float(lines[3]), float(lines[4]),float(lines[5])])\n")
    file.write("ans=[]\n")
    tab='\t'
    file.write("for item in range(len(input1)):\n")




def gini(input1, target,total_greyhound,total_whippet):
    '''

    :param input1:
    :param target:
    :param total_greyhound:
    :param total_whippet:
    :return: best gini index, best threshold.
    The function finds the mixed gini value for each value of a particular value and then resukt the best gini value
    along with its threshold value
    '''

    bestgini=1.5
    bestthreshold=0

    for values in input1:
        '''
        for loop does all the gini calculation and gives best gini value and the threshold
        '''
        number_of_greyhound_left = 0
        number_of_whippet_left = 0

        for item in range(len(input1)):
            if input1[item] < values:
                if target[item]=='Greyhound':
                    number_of_greyhound_left=number_of_greyhound_left+1
                elif target[item]=='Whippet':
                    number_of_whippet_left=number_of_whippet_left+1

        number_of_greyhound_right=total_greyhound-number_of_greyhound_left
        number_of_whippet_right=total_whippet-number_of_whippet_left

        # calculating the left gini
        if number_of_greyhound_left+number_of_whippet_left==0:# handling the edge case when there are no terms in the left.
            gini_left=0
        else:
            gini_left=1-(math.pow((number_of_greyhound_left/(number_of_greyhound_left+number_of_whippet_left)),2))-(math.pow(
                number_of_whippet_left/(number_of_greyhound_left+number_of_whippet_left),2
        ))
        # calculating the right gini
        if number_of_greyhound_right+number_of_whippet_right==0:
            gini_right=0
        else:
            gini_right=1-(math.pow((number_of_greyhound_right/(number_of_greyhound_right+number_of_whippet_right+1)),2))-(math.pow((
            number_of_whippet_right/(number_of_whippet_right+number_of_greyhound_right+1))
            ,2))
        probab_l=(number_of_greyhound_left+number_of_whippet_left)/(total_greyhound+total_whippet)
        probab_r=(number_of_greyhound_right+number_of_whippet_right)/(total_greyhound+total_whippet)


        # calculating the mix gini index
        final_gini=gini_left*probab_l + gini_right*probab_r

        #updatting the gini value and the threshold if a new best gini found
        if final_gini<bestgini:
            bestgini=final_gini
            bestthreshold=values



    return bestgini, bestthreshold



def split(input1,level,s,tab,file):
    '''

    :param input1:  the parent list
    :param level: which level is the tree at
    :param s: if it is a right child or left child
    :return: None

    The function finds the attribute with the minimum gini and splits the input file in two parts accordingly  it also
    builds the decision tree by the adding the nodes in ito the global list. its a recursive function.
    '''
    global decision_list

    total_number_of_greyhound=0
    total_number_of_whippet=0

    for item in range(len(input1)):
        if input1[item][6]=='Greyhound':
            total_number_of_greyhound=total_number_of_greyhound+1
        else:
            total_number_of_whippet=total_number_of_whippet+1

    # stopping criteria of the 90% of the data that needs to be same.
    if total_number_of_greyhound/(total_number_of_greyhound+total_number_of_whippet+0.1)>=0.90:
        decision_list.append('Greyhound')
        #print(" "*level+"Grehound "+s)
        tab=tab+"\t"
        sentence=tab+"ans.append(\"Greyhound\")\n"
        file.write(sentence)
        return None
    elif total_number_of_whippet/(total_number_of_greyhound+total_number_of_whippet+0.1)>=0.90:
        decision_list.append('whippet')
        #print(" "*level+"whippet "+s)
        tab = tab + "\t"
        sentence=tab+"ans.append(\"Whippet\")\n"
        file.write(sentence)
        return None

    # if stopping criteria is not met keepin finding best gini and splitting

    else:
        attr_u = []
        attr_v = []
        attr_w = []
        attr_x = []
        attr_y = []
        attr_z = []
        targets = []
        total_greyhound=0
        total_wippet=0
        threshold=0
        node=0
        for item in range(len(input1)):
            #for loop gets the data structure ready for calculating the gini.
            attr_u.append(input1[item][0])
            attr_v.append(input1[item][1])
            attr_w.append(input1[item][2])
            attr_x.append(input1[item][3])
            attr_y.append(input1[item][4])
            attr_z.append(input1[item][5])
            target = input1[item][6]
            if target == 'Greyhound':
                total_greyhound = total_greyhound + 1
            elif target == 'Whippet':
                total_wippet = total_wippet + 1
            targets.append(input1[item][6])
        #print(targets)
        # finding the gini inex of each attribute
        gini_attrib_u ,threshold_attrib_u = gini(attr_u,targets,total_greyhound,total_wippet)
        gini_attrib_v, threshold_attrib_v = gini(attr_v, targets, total_greyhound, total_wippet)
        gini_attrib_w, threshold_attrib_w = gini(attr_w, targets, total_greyhound, total_wippet)
        gini_attrib_x, threshold_attrib_x = gini(attr_x, targets, total_greyhound, total_wippet)
        gini_attrib_y, threshold_attrib_y = gini(attr_y, targets, total_greyhound, total_wippet)
        gini_attrib_z, threshold_attrib_z = gini(attr_z, targets, total_greyhound, total_wippet)

        ginis=[gini_attrib_u,gini_attrib_v,gini_attrib_w,gini_attrib_x,gini_attrib_y,gini_attrib_z]

        # finding the minimum gini from all the attributes
        min_index=ginis.index(min(ginis))
        if min_index==0:
            node='attrib_u'
            threshold=threshold_attrib_u
        elif min_index==1:
            node = 'attrib_v'
            threshold = threshold_attrib_v
        elif min_index==2:
            node = 'attrib_w'
            threshold = threshold_attrib_w
        elif min_index==3:
            node = 'attrib_x'
            threshold = threshold_attrib_x
        elif min_index==4:
            node = 'attrib_y'
            threshold = threshold_attrib_y
        elif min_index==5:
            node = 'attrib_z'
            threshold = threshold_attrib_z
        #print(" "*level+" Node",[node, min_index, threshold],s)

        # adding to the decision list its the min index which is use-full in for classifier and not the attriute- atleast
        #I am computin it using the index number and not the attribute name, attribute name is for clarity
        decision_list.append([node, min_index, threshold])

        left_split=[]
        right_split=[]


        for item in range(len(input1)):
            '''
            Splitting the input based on the threshold of the attribute having least  gini index.
            '''
            if input1[item][min_index]<threshold:
                left_split.append(input1[item])
            elif input1[item][min_index]>=threshold:
                right_split.append(input1[item])
        tab=tab+'\t'
        if len(left_split)>=1:
            #sentence=tab+"if item1[",min_index,"] <" ,threshold
            #print(tab+"if item1[",min_index,"] <" ,threshold)
            file.write(tab+"if input1[item][")
            file.write(str(min_index))
            file.write("] <" )
            file.write(str(threshold)+":\n")

            split(left_split,level+1,'L',tab,file)
        if len(right_split)>=1:
            #sentence=tab+"elif item1["+ str(min_index)+"] >=" ,threshold
            #print(tab+"elif item1["+ str(min_index)+"] >=" ,threshold)
            #tab=tab+"\t"
            #file.write(sentence)
            file.write(tab + "elif input1[item][")
            file.write(str(min_index))
            file.write("] >=")
            file.write(str(threshold) + ":\n")

            split(right_split,level+1,'R',tab,file)

        return None


def main():

     in_file=[]
     flag=False
     input1=[]

     total_greyhound=0
     total_wippet=0
     with open('your_training_data.csv') as file:
         for lines in file:
            lines=lines.strip().split(',')
            #print(lines)
            if flag==False:
                flag=True
            else:
                input1.append([float(lines[0]),float(lines[1]),float(lines[2]),float(lines[3]),float(lines[4]),float(lines[5]),lines[6]])# there are
                # 6 input features and lines[6] reads the classifier class.
                target=lines[6]
                if target=='Greyhound':
                    total_greyhound=total_greyhound+1
                elif target=='Whippet':
                    total_wippet=total_wippet+1


     level=1
     s='N'
     tab=''
     with open('Classifier.py','w') as file:
        writingStartFileBoiler(file)
        split(input1,level,s,tab,file)
        endOfFile(file)

     print("decision_list ",decision_list)
     print("Classifier created succesfully")



if __name__ == '__main__':
    main()