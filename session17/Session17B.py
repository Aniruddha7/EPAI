#!/usr/bin/env python
# coding: utf-8

# In[1]:


#01
#Write Python program to figure out smallest number in a user given list
l1=[]
number =int (input("No.of elements to list:"))
for i in range(1,number+1):
  element=int (input("enter the elements:"))
  l1.append(element)
print("smallest number in list", min(l1))


# In[2]:


#02
#Write python funtion to convert a list into dictionary
def convert_to_dict(lst1):
  iterator=iter(lst1)
  dictionary= dict(zip(iterator, iterator))
  return dictionary

lst1= ['Emp_name', 'xyz', 'Emp_id', 123]
print(convert_to_dict(lst1))


# In[4]:


#03
#Write python program to convert dictionary to tuples list

dict1= {'Emp_name': 'xyz', 'Emp_id':123}

list2= [(k,v) for k,v in dict1.items()]
print(list2)


# In[5]:


#04
#Write python funtion to convert decimal number to binary

# decimal value 
decimal = 37
def dec_to_bin(number):
  if number>1:
    dec_to_bin(number // 2)
  print(number % 2) 

# Calling function 
dec_to_bin(decimal) 


# In[6]:


#05
#Write a Python funtion to find the repeated words in a sentence

string= "A Python programmer sometimes codes in Python but also sometimes codes in C++"
def repeated_words(str):
  str= str.split()
  string1= []
  for i in str:              
  
        # filtering out repeated words  
        if i not in string1: 
        # append value in empty list 
            string1.append(i)
            #print(string1)
  for i in range(0, len(string1)): 
    print(string1[i], 'is repeated:', str.count(string1[i]), 'times') 

repeated_words(string)


# In[7]:


#06
#Write a python program to replace the word in the given string
string ="Bugatti 16.4 Veyron is the fastest car in the world"
print(string)
print(string.replace("Bugatti 16.4 Veyron", "Venom F5", 1)+(" currently"))


# In[8]:


#07
#Write python program to check string palindrome
str1= "kayak"
if str1==str1[::-1]:
  print("string is palindrome")
else:
  print("not palindrome")


# In[9]:


#08
#Write a python function to count the number of vowels in string
vowels = "aeiou"
str= "Python programming"

def vowel_count(str, vowels):
  count={}.fromkeys(vowels, 0)
  for character in str:
    if character in count:
      count[character]+=1
  return count
print(vowel_count(str, vowels))


# In[10]:


#09
#Write python program to find the word with maximum vowels

lis1=["car", "python", "loop", "rangefinder"]
output= ""
max_length=0

for words in lis1:
  vowel_length=len([ele for ele in words if ele in['a','e','i','o','u']])
  if vowel_length>max_length:
    max_lenght=vowel_length
    output=words
print("word with max vowels", output)


# In[11]:


#10
#write python funtion to find the longest string in the list

def longest_word(word_list):
    length = []
    for words in word_list:
        length.append((len(words), words))
    length.sort()
    return length[-1][0], length[-1][1]
result = longest_word(["car", "Truck", "World", "Galaxy", "Universe"])
print("Longest word: ",result[1])
print("longest word length: ",result[0])


# In[ ]:


#11
#Wite a python program to 

