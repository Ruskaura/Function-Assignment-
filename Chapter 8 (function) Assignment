{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 8-1 Message: \n",
    "- Write a function called display_message() that prints one sentence\n",
    "  telling everyone what you are learning about in this chapter. Call the\n",
    "  function, and make sure the message displays correctly."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "def display_message():\n",
    "    '''this function prints a message'''\n",
    "    message = \"In this chapter I am learning about functions in Python\"\n",
    "\n",
    "    print(message)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "In this chapter I am learning about functions in Python\n"
     ]
    }
   ],
   "source": [
    "display_message()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 8-2. Favorite Book:\n",
    "- Write a function called favorite_book() that accepts one\n",
    "  parameter, title. The function should print a message, such as One of my\n",
    "  favorite books is Alice in Wonderland. Call the function, making sure to\n",
    "include a book title as an argument in the function call."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "One of my favorite books is Alice in Wonderland\n"
     ]
    }
   ],
   "source": [
    "def favorite_book(title):\n",
    "    print(f'One of my favorite books is {title}')\n",
    "\n",
    "\n",
    "favorite_book('Alice in Wonderland')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 8-3 T-Shirt: \n",
    "- Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.\n",
    "Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The size of my shirt is 42\n",
      "The message written on it is : proudly computer scientist\n",
      "The size of my shirt is 39\n",
      "The message written on it is : Ta namoda mai kamar yau sallah\n"
     ]
    }
   ],
   "source": [
    "def make_shirt(size, message):\n",
    "    '''this function makes a t-shirt'''\n",
    "    print(f'The size of my shirt is {size}')\n",
    "    print(f'The message written on it is : {message}')\n",
    "# Using positional argument\n",
    "make_shirt(39, 'proudly computer scientist')\n",
    "\n",
    "# using keyword argument\n",
    "make_shirt(size=39, message = 'Ta namoda mai kamar yau sallah')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 8-4 Large Shirts: \n",
    "- Modify the make_shirt() function so that shirts are large\n",
    "by default with a message that reads I love Python. Make a large shirt and a\n",
    "medium shirt with the default message, and a shirt of any size with a different\n",
    "message."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Size of shirt = large, Message on shirt: I love Python\n",
      "Size of shirt = Medium, Message on shirt: I love Python\n",
      "Size of shirt = Extra Large, Message on shirt: I love CSS\n"
     ]
    }
   ],
   "source": [
    "def make_shirt(size= 'large', message = 'I love Python'):\n",
    "    print(f'Size of shirt = {size}, Message on shirt: {message}')\n",
    "# dafault shirt\n",
    "make_shirt()\n",
    "# Medium shirt\n",
    "make_shirt(size = 'Medium')\n",
    "# any size shirt\n",
    "make_shirt(size = 'Extra Large', message = 'I love CSS')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 8-5 Cities:\n",
    "- Write a function called describe_city() that accepts the name of\n",
    "a city and its country. The function should print a simple sentence, such as\n",
    "Reykjavik is in Iceland. Give the parameter for the country a default value.\n",
    "Call your function for three different cities, at least one of which is not in the\n",
    "default country."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Reyjavik is in Iceland\n",
      "Abuja is in Nigeria\n",
      "Zamfara is in Nigeria\n",
      "Accra is in Ghana\n"
     ]
    }
   ],
   "source": [
    "def describe_city(city, country = 'Nigeria'):\n",
    "    print(f'{city} is in {country}')\n",
    "    \n",
    "\n",
    "describe_city(city = 'Reyjavik', country= 'Iceland')\n",
    "\n",
    "describe_city(city = 'Abuja')\n",
    "describe_city(city = 'Zamfar')\n",
    "describe_city(city = 'Accra', country= 'Ghana')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 8-6 City Names: \n",
    "- Write a function called city_country() that takes in the name\n",
    "of a city and its country. The function should return a string formatted like this:\n",
    "\"Santiago, Chile\"\n",
    "Call your function with at least three city-country pairs, and print the values\n",
    "that are returned."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accra, Ghana\n",
      "Abuja, Nigeria\n",
      "New York, Usa\n"
     ]
    }
   ],
   "source": [
    "def city_country(city, country):\n",
    "    '''Takes in city name and country and prints a formatted message'''\n",
    "    return f\"{city.title()}, {country.title()}\"\n",
    "\n",
    "\n",
    "print(city_country('Accra', 'Ghana'))\n",
    "print(city_country('Abuja', 'Nigeria'))\n",
    "print(city_country('New York', 'Usa'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 8-7 Album: \n",
    "- Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.\n",
    "Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'artist': 'Maher zain', 'title': 'Paradise'}\n",
      "{'artist': 'Humood', 'title': 'Hayyah (Qatar worldcup'}\n",
      "{'artist': 'Audu steem', 'title': 'Koguna', 'songs': 12}\n"
     ]
    }
   ],
   "source": [
    "def make_album(artist_name, album_title, number_of_songs=None):\n",
    "    '''this function creates a dictionary called album info'''\n",
    "    album_info = {\n",
    "        'artist': artist_name,\n",
    "        'title': album_title\n",
    "    }\n",
    "    if number_of_songs:\n",
    "        album_info['songs'] = number_of_songs\n",
    "    return album_info\n",
    "\n",
    "album1 = make_album('Maher zain', 'Paradise')\n",
    "album2 = make_album('Humood', 'Hayyah(Qatar worldcup)')\n",
    "album3 = make_album('Audu steem', 'Koguna', 12)\n",
    "\n",
    "# Printing each return value to display the album information\n",
    "print(album1)\n",
    "print(album2)\n",
    "print(album3)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 8-8 User Albums: \n",
    "-Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter 'q' at any time to quit.\n",
      "{'artist': 'Saleem', 'title': 'Labarina'}\n",
      "Enter 'q' at any time to quit.\n",
      "{'artist': 'Nura m inuwa', 'title': 'Gidan Sarauta'}\n",
      "Enter 'q' at any time to quit.\n"
     ]
    }
   ],
   "source": [
    "def make_album(artist_name, album_title, number_of_songs=None):\n",
    "    album_info = {\n",
    "        'artist': artist_name,\n",
    "        'title': album_title\n",
    "    }\n",
    "    if number_of_songs:\n",
    "        album_info['songs'] = number_of_songs\n",
    "    return album_info\n",
    "\n",
    "while True:\n",
    "    print(\"Enter 'q' at any time to quit.\")\n",
    "    artist = input(\"Enter the artist's name: \")\n",
    "    if artist.lower() == 'q':\n",
    "        break\n",
    "    \n",
    "    title = input(\"Enter the album title: \")\n",
    "    if title.lower() == 'q':\n",
    "        break\n",
    "    \n",
    "    album = make_album(artist, title)\n",
    "    print(album)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 8-9. Messages: \n",
    "-Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "What is your name?\n",
      "My name is Rabiu usman sani\n",
      "How was your day?\n",
      "It was fine.\n"
     ]
    }
   ],
   "source": [
    "def show_messages(messages):\n",
    "    for message in messages:\n",
    "        print(message)\n",
    "\n",
    "text_messages = [\"What is your name?\", \"My name is Rabiu usman sani\", \"How was your day?\", \"It was fine.\"]\n",
    "\n",
    "show_messages(text_messages)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 8-10. Sending Messages: \n",
    "- Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "What is your name?\n",
      "My name is Rabiu usman sani\n",
      "How was your day?\n",
      "It was cool.\n",
      "\n",
      "Original messages:\n",
      "['What is your name?', 'My name is Rabiu usman sani', 'How was your day?', 'It was cool.']\n",
      "\n",
      "Sent messages:\n",
      "['What is your name?', 'My name is Rabiu usman sani', 'How was your day?', 'It was cool.']\n"
     ]
    }
   ],
   "source": [
    "def send_messages(messages):\n",
    "    sent_messages = []\n",
    "    for message in messages:\n",
    "        print(message)\n",
    "        sent_messages.append(message)\n",
    "    return sent_messages\n",
    "\n",
    "\n",
    "sent_messages = send_messages(text_messages)\n",
    "\n",
    "# Printing both lists\n",
    "print(\"\\nOriginal messages:\")\n",
    "print(text_messages)\n",
    "\n",
    "print(\"\\nSent messages:\")\n",
    "print(sent_messages)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 8-11. Archived Messages: \n",
    "- Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "What is your name?\n",
      "My name is Rabiu usman sani\n",
      "How was your day?\n",
      "It was cool.\n",
      "\n",
      "Original messages:\n",
      "['What is your name?', 'My name is Rabiu usman sani', 'How was your day?', 'It was cool.']\n",
      "\n",
      "Sent messages:\n",
      "['What is your name?', 'My name is Rabiu usman sani', 'How was your day?', 'It was cool.']\n"
     ]
    }
   ],
   "source": [
    "def send_messages(messages):\n",
    "    sent_messages = []\n",
    "    for message in messages:\n",
    "        print(message)\n",
    "        sent_messages.append(message)\n",
    "    return sent_messages\n",
    "\n",
    "copied_messages = text_messages[:]\n",
    "\n",
    "sent_messages = send_messages(copied_messages)\n",
    "\n",
    "# Printing both lists\n",
    "print(\"\\nOriginal messages:\")\n",
    "print(text_messages)\n",
    "\n",
    "print(\"\\nSent messages:\")\n",
    "print(sent_messages)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 8-12. Sandwiches: \n",
    "- Write a function that accepts a list of items a person wants\n",
    "on a sandwich. The function should have one parameter that collects as many\n",
    "items as the function call provides, and it should print a summary of the sandwich\n",
    "that’s being ordered. Call the function three times, using a different number\n",
    "of arguments each time."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please make a sandwich with the following ingredients:\n",
      "- Apple\n",
      "- Banana\n",
      "- Orange\n",
      "Please make a sandwich with the following ingredients:\n",
      "- fish\n",
      "- egg\n",
      "Please make a sandwich with the following ingredients:\n",
      "- butter\n",
      "- sugarcane\n",
      "- pineapple\n",
      "- juice\n"
     ]
    }
   ],
   "source": [
    "def make_sandwich(*ingredients):\n",
    "    print(\"Please make a sandwich with the following ingredients:\")\n",
    "    for ingredient in ingredients:\n",
    "        print(\"- \" + ingredient)\n",
    "\n",
    "make_sandwich('Apple', 'Banana', 'orange')\n",
    "make_sandwich('fish', 'egg')\n",
    "make_sandwich('butter', 'sugarcane', 'pineapple', 'juice')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 8-13. User Profile: \n",
    "- Start with a copy of user_profile.py from page 148. Build a\n",
    "profile of yourself by calling build_profile(), using your first and last names\n",
    "and three other key-value pairs that describe you."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'first_name': 'Rabiu', 'last_name': 'usman sani', 'age': 26, 'Location': 'Kaura', 'hobbies': ['watching series korean film', 'chatting']}\n"
     ]
    }
   ],
   "source": [
    "def build_profile(first_name, last_name, **additional_info):\n",
    "    profile = {\n",
    "        'first_name': first_name,\n",
    "        'last_name': last_name,\n",
    "    }\n",
    "    profile.update(additional_info)\n",
    "    return profile\n",
    "\n",
    "# Building a profile\n",
    "my_profile = build_profile('Rabiu', 'usman sani', age= 26, Location='Kaura', hobbies=['watching series korea film', 'chatting'])\n",
    "print(my_profile)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 8-14. Cars: \n",
    "- Write a function that stores information about a car in a dictionary.\n",
    "The function should always receive a manufacturer and a model name. It\n",
    "should then accept an arbitrary number of keyword arguments. Call the function\n",
    "with the required information and two other name-value pairs, such as a\n",
    "color or an optional feature. \n",
    "  - Your function should work for a call like this one:\n",
    "    - car = make_car('jelani', 'outback', color='black', tow_package=True)\n",
    "    - Print the dictionary that’s returned to make sure all the information was\n",
    "stored correctly."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'manufacturer': 'jelani', 'model': 'outback', 'color': 'black', 'tow_package': True}\n"
     ]
    }
   ],
   "source": [
    "def make_car(manufacturer, model, **car_info):\n",
    "    car = {\n",
    "        'manufacturer': manufacturer,\n",
    "        'model': model,\n",
    "    }\n",
    "    car.update(car_info)\n",
    "    return car\n",
    "\n",
    "# Creating a car dictionary\n",
    "car = make_car('jelani', 'outback', color='black', tow_package=True)\n",
    "print(car)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 8-15. Printing Models: \n",
    "- Put the functions for the example printing_models.py in a separate file called printing_functions.py. Write an import statement at the top of printing_models.py, and modify the file to use the imported functions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "250"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from printing_functions import add\n",
    "add(10, 50)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exersise 8-16. Imports: \n",
    "- Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:\n",
    "  - import module_name\n",
    "  - from module_name import function_name\n",
    "  - from module_name import function_name as fn\n",
    "  - import module_name as mn\n",
    "  - from module_name import *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Addition: 8\n",
      "Subtraction: 6\n",
      "Multiplication: 42\n",
      "Division: 5.0\n",
      "Power: 8\n",
      "Addition (from imported module): 7\n"
     ]
    }
   ],
   "source": [
    "# 1: import module_name\n",
    "import printing_functions\n",
    "\n",
    "# 2: from module_name import function_name\n",
    "from printing_functions import subtract, divide as div\n",
    "\n",
    "# 3: from module_name import function_name as fn\n",
    "import printing_functions as pf\n",
    "\n",
    "# 4: import module_name as mn\n",
    "import printing_functions as mn\n",
    "\n",
    "# 5: from module_name import *\n",
    "from printing_functions import *\n",
    "\n",
    "# Using the functions\n",
    "result1 = printing_functions.add(5, 3)\n",
    "result2 = subtract(10, 4)\n",
    "result3 = pf.multiply(6, 7)\n",
    "result4 = div(10, 2)\n",
    "result5 = power(2, 3)\n",
    "result6 = add(3, 4)\n",
    "\n",
    "print(\"Addition:\", result1)\n",
    "print(\"Subtraction:\", result2)\n",
    "print(\"Multiplication:\", result3)\n",
    "print(\"Division:\", result4)\n",
    "print(\"Power:\", result5)\n",
    "print(\"Addition (from imported module):\", result6)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 8-17. Styling Functions: \n",
    "- Choose any three programs you wrote for this chapter, and make sure they follow the styling guidelines described in this section."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def add(a, b):\n",
    "    ''' Return the sum of two numbers'''\n",
    "    return a + b\n",
    "\n",
    "add(2, 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def is_even(number):\n",
    "    \"\"\"Check if a number is even.\"\"\"\n",
    "    return number % 2 == 0\n",
    "\n",
    "is_even(40)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "90"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def multiply_by_ten(number):\n",
    "    \"\"\"Multiply a number by 10.\"\"\"\n",
    "    return number * 10\n",
    "\n",
    "multiply_by_ten(9)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
