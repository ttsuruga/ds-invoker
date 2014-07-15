ds-invoker
==========

Set of simple python scripts to invoke digital signage content with web browser.

## Some Note for Use

The code is developped with python 3.4.

You will need to generate openssl pem file command like below, and place together with rpcsslserver.py.

*openssl req -new -x509 -days 3650 -nodes -out cert.pem -keyout cert.pem*

On Windows digital signage client machine, add firewall rule to let python have incomming connection.

Adjust the "localhost" in both server and client code to ip of the digital signage client machine, where rpcsslserver.py runs.

Adjust the url in client code to desired url for testing.

Add path to IE on Windows digital signage client machine PATH, so rpc can lauch IE.

## To Do

###### rpcsslserver.py

Implement Taskkilling of digital sinage clinet when invoking brower, and relaunching digital signage clinet when it ends.

Implement forced focus on the invoked browser windows to assure it shows on top of everything else.

###### rpcsslclient.py

Implementing towards web interface making use of the function, with large number of client to control in mind.
