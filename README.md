# Messaging system rest API
## About
The task is to write a simple rest API backend system that is responsible for handling messages between users.
A message contains:
* sender (owner)
* Receiver
* Message
* Subject
* creation date

## The rest API should contains:

- Write message
- Get all messages for a specific user
- Get all unread messages for a specific user
- Read message (return one message)
- Delete message (as owner or as receiver)


## Performance of use REST framework API

    Get all messages using GET request:
    * endpoint /messages

    Write message using POST request:
    * endpoint /messages/

    Body request requires next fields as:
    {
    "sender": "id number of existing user",
    "receiver": "id number of existing user",
    "subject": "str",
    "message": "str"
    }


    Read one message with given id using GET request:
    * endpoint /specific-message/message_id
      For be sure just an authenticated user can only see his own messages, for that purpose required value = token and
      key = Authorization


    Get all sent messages for user by his id number, for that purpose required value = token and key = Authorization.
    GET request, endpoint /all-messages/user_id

    Get all unred sent messages for user by his id number, for that purpose required value = token and
    key = Authorization.
    GET request, endpoint /all-unread-messages/user_id

    Delete a message by given id number using DELETE request:
    * endpoint /specific-message/message_id/
      For be sure just an authenticated user can only delete messages as owner or as receiver, for that purpose
      required value = token and key = Authorization
