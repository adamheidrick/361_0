# 361: Software Engineering

This course introduces tools and methods for real-world software development. 

## Assignment 3.5: Communication Contract
This microservice provides a random number within range based on the users request.

###A. Instructions on how to Request Data:
* Have a .txt file in your project that your program can write to with the following name: 
```random-int-request.txt```
* In your code, you can make a request by writing a number in string format to the random-int-request.txt file.
* Simply write the upper limit of the range to the text file.
* Here are a few examples in Python:
```
# This will request a random number within range of 1 -> 5
# Rmember to convert the number to string. You can use str(int)
request_source = 'random-int-request.txt' 
with open(source, 'w') as f:
                f.write(str(5))
                f.close()
```

```
# This will request a number within range of 1 -> lenght of array.
# Remember to convert the length of array to string. 

request = 'random-int-request.txt' 
with open(request, 'w') as f:
                f.write(str(len(someArray)))
                f.close()
```
### B: Instructions on how to Receive Data:
* Similar to above: have a .txt file in your project that your program can read from with the following name: 
```random-int-receive.txt```
* Simply read the random-int-receive.txt to reveive tha data. 
* Here is an example in Python:
```
# This will receieve a random number based on request.
# The variable data will hold the random number. 

returned_data= 'random-int-receive.txt' 
with open(requested_data, 'r') as f:
                    data = f.read()
                    f.close()
```
###C: UML Sequence Diagram: 
![Alt text](https://github.com/adamheidrick/361_0/blob/main/SequenceDiagram.jpeg.jpeg?raw=true "UML Sequence Diagram")
