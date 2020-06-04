## Built using : 
Python 3.7.5

## Execution of project : 

 - Start Server

```sh
python server.py
```
 - Start Client CLI

```sh
python client.py
```

### Features Implemented :
 - Chat Server
 - Message Encryption
 - Sending random greeting from client to server from message.txt

## About :
CLI chat is made using Python's Socket Programming inbuilt module socket.It consists of a server and a client for handling incoming and outgoing messages.Messages are encrypted using RSA algorithm.

### Working : 
First start the server using the above command.The server will listen to other clients on IP '127.0.0.1' on PORT '1234'.Whenever the client CLI is started and socket is connected to the server,the client has to enter his name and the socket will be added to socket list and successful connection message will be displayed.Here, we are using select module which gives OS level selection of sockets.If a new connection is made it is added to clients dictionary which is used for broadcasting messages to other clients when a new message arrives.A greeting message is selected randomly from message.txt file and is sent from client to server at the start of connection.For RSA encryption the two prime numbers are kept fixed for now which will give the same public and private key for encryption and decryption.The prime nos can be later made random by using it with a backend.

### Message sending format :
HEADER_LENGTH is fixed for both server and client.First a message_header is made which consists of the length of message with HEADER_LENGTH spaces aligned left.Both the message_header and encrypted message are then encoded and sent to the socket.While recieving the message first the header is recieved to know the length and then that many characters are recieved from the socket and decoded message is displayed.

## Note : 
For Recieving new messages from other clients,the client has to press enter on the CLI.


