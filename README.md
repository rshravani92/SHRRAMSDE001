# SHRRAMSDE001
To get posts from Expedia Facebook page

Details
The program is developed as a Python 2.7 script in GetOrganizationFacebookPosts.py
The program will write the data in JSON format to ExpediaPosts.txt file(The file name can be changed in the program)

Instructions to run the program
The program can be imported as new project in IDE like PyCharm to be executed
To run program, the user have to provide access token. This access token is required to retrieve data from Facebook Graph API
https://developers.facebook.com/tools/explorer/

Design Assumptions
The JSON structure has the list of all posts having post details like date and time of the post and message
The Organization name and the timestamp of file generation is provided in file to track in future
The details of the retrieved posts are provided as a set of post date, time and message. In future, if any post specific details have to added, It can be added to dictionary.

