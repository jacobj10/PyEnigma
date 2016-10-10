import sys

def init_dict():
    num_dict={}
    low_dict={}
    final_dict={}
    reflector={}
    return (low_dict,num_dict,final_dict,reflector)
def scramble(dict,numlist):
    counter=0
    rev_dict={}
    while counter<26:
        dict[chr(counter+65)]=chr(numlist[counter]+64)
        rev_dict[chr(numlist[counter]+64)]=chr(counter+65)
        counter+=1
    return dict,numlist,rev_dict
def arrange(scrambler,start):
    numlist=scrambler[1]
    index=numlist.index(ord(start)-64)
    x=0
    newlist=list()
    templist=list()
    newlist=numlist[index:len(numlist)]+numlist[0:index]
    return newlist    
def generate_reflect_dict(dict,reflector_list):
    x=0
    while x<len(reflector_list)-1:
        dict[chr(reflector_list[x]+64)]=chr(reflector_list[x+1]+64)
        dict[chr(reflector_list[x+1]+64)]=chr(reflector_list[x]+64)
        x+=2
    return dict
def translate(scrambler1,scrambler2,scrambler3, reflector, char):
    dict1=scrambler1[0]
    dict2=scrambler2[0]
    dict3=scrambler3[0]
    rev1=scrambler1[2]
    rev2=scrambler2[2]
    rev3=scrambler3[2]
    return rev1[rev2[rev3[reflector[dict3[dict2[dict1[char]]]]]]]
def shift(scrambler):
    numlist=scrambler[1]
    temp=numlist[1:len(numlist)]
    temp=temp+numlist[0:1]
    return temp
def main():
    x=init_dict()
    numlist1=(10, 3, 8, 9, 2, 12, 18, 14, 23, 26, 7, 17, 19, 25, 15, 20, 24, 4, 16, 21, 5, 11, 6, 13, 1, 22)
    numlist2=(2, 16, 9, 3, 11, 12, 14, 19, 20, 13, 4, 17, 10, 5, 22, 23, 6, 21, 18, 25, 8, 15, 7, 1, 26, 24)
    numlist3=(25, 15, 2, 23, 11, 6, 1, 14, 26, 5, 10, 22, 16, 19, 21, 13, 9, 8, 12, 17, 18, 7, 3, 4, 24, 20)
    listdict={"A":numlist1,"B":numlist2, "C":numlist3}
    print "Scrambler A is wired" , numlist1
    print "Scrambler B is wired" , numlist2
    print "Scrambler C is wired" , numlist3
    print "PLEASE ENTER DESIRED ORIENTATION OF SCRAMBLERS (i.e. ABC CBA ACB)"
    order=raw_input()
    numlist1=listdict[order[0]]
    numlist2=listdict[order[1]]
    numlist3=listdict[order[2]]
    reflectorlist=(9 , 10 , 2 , 14 , 15 , 13 , 11 , 12 , 16 , 1 , 8 , 26 , 21 , 24 , 3 , 22 , 25 , 19 , 4 , 6 , 7 , 17 , 23 , 5 , 18 , 20)
    scrambler1=scramble(x[0],numlist1)
    scrambler2=scramble(x[1],numlist2)
    scrambler3=scramble(x[2],numlist3)
    reflector=generate_reflect_dict(x[3],reflectorlist)
    print "Starting UPPERCASE letter for Scrambler 1"
    start1=raw_input().upper()
    numlist1=arrange(scrambler1,start1)
    print "Starting UPPERCASE letter for Scrambler 2"
    start2=raw_input().upper()
    numlist2=arrange(scrambler2,start2)
    print "Starting UPPERCASE letter for Scrambler 3"
    start3=raw_input().upper()
    numlist3=arrange(scrambler3,start3)
    scrambler1=scramble(scrambler1[0],numlist1)
    scrambler2=scramble(scrambler2[0],numlist2)
    scrambler3=scramble(scrambler3[0],numlist3)
    print "Enter string to enter the ENIGMA"
    plaintext=raw_input().upper()
    print(chr(27) + "[2J")
    y=0
    ciphertext=""
    while y<len(plaintext):
              ciphertext+=translate(scrambler1,scrambler2,scrambler3,reflector,plaintext[y])
              numlist1=shift(scrambler1)
              scrambler1=scramble(scrambler1[0], numlist1)
              if y%26==0:
                  numlist2=shift(scrambler2)
                  scrambler2=scramble(scrambler2[0],numlist2)
                  if y%52==0:
                      numlist3=shift(scrambler3)
                      scrambler3=scramble(scrambler3[0],numlist3)
              y+=1
    print ciphertext
main()
