### Application Programming Interface(API) ###

# 1 - API

'''
    refers to a set of rules, protocols, and tools that allows different software applications to communicate with each other. 
'''

# 2 - Building API

'''
Let's build a RESTful API using Python, Flask, and MongoDB.
 It's like a superpower for our database, allowing us to create, read, update, 
 and delete data with HTTP requests. With our Python skills and knowledge of HTTP,
 we're ready to make some magic happen!
'''

# 3 - HTTP(Hypertext Transfer Protocol)

'''
HTTP is like the language spoken between your browser 
(the client) and the server where data is stored. 
It's a protocol used to send requests for resources, 
like web pages or images, from the client to the server, 
and to receive responses back. So, when you're browsing the web,
your browser is the client, and it sends requests to the server,
which then sends back the requested data.
'''

# 4 - Structure of HTTP

'''
Request Header:

    Initial Line: This includes the method (e.g., GET, POST), the URI (Uniform Resource Identifier) of the requested resource, and the HTTP version.
    Header Lines: These contain additional information about the request, such as the user-agent (the software making the request), accepted content types, cookies, and more.
    Blank Line: Separates the header from the optional message body.
    Message Body: Contains data being sent with the request, like form data or file uploads.

Response Header:

    Initial Line: This includes the HTTP version, status code (indicating the success or failure of the request), and a reason phrase describing the status code.
    Header Lines: Similar to the request, these contain additional information about the response, such as content type, server information, cookies, and more.
    Blank Line: Separates the header from the optional message body.
    Message Body: Contains the requested resource, like HTML for a web page, image data, or any other content.
    This structure is consistent across both request and response messages in HTTP, facilitating communication between clients and servers.
'''

# 5 - Initial Request Line(Status Line)

# This Python script introduces the basics of HTTP protocol,
# focusing on request and response structures.

# Request Line (for client's request):
# - Method (e.g., GET, POST), requested resource path, and HTTP version.
# Example: GET / HTTP/1.1

# Status Line (for server's response):
# - HTTP version, status code (e.g., 200 OK, 404 Not Found), and reason phrase.
# Example: HTTP/1.0 200 OK

# Header Fields:
# - Additional info about request/response (e.g., host, user-agent).
# Example: Host: thirtydaysofpython-v1-final.herokuapp.com

# Message Body:
# - Contains data sent after headers. In responses, it usually includes requested resource.
# - Headers like Content-Type and Content-Length describe body.
# Example: Content-Type: text/html

# Request Methods:
# - Represent actions on a resource (e.g., GET, POST, PUT, DELETE).
# - GET: Retrieve data. 
# - POST: Create new data. 
# - PUT: Update data. 
# - DELETE: Remove data.