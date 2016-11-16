## Gryffindor ##
In order to make Caf Wizard more accessible, I decided to rewrite it in Flask. This has multiple advantages:
* Users can receive new builds in real-time (no waiting for Apple's approval)
* iOS+Android+Web in one codebase.
* Responsive UI (Bootstrap is easy to use/magical)

Additionally, I have removed the AWS backend in favor of the simpler Bon Appetit API. I used to run a separate PHP script that parsed data from Bon Appetit and stored it in DynamoDB. Now, the client is in charge of parsing the data. I simply request JSON data from Bon Appetit, parse it, and display it. No more abstracted backend.

---------------------
Setting up virtualenv
---------------------

Run the following commands to setup the virtual environment and install the correct modules:

    $ virtualenv uploadzen_env
    $ source uploadzen_env/bin/activate
    $ pip install -r requirements.txt

When installing a new module, make sure to update requirements.txt using pip freeze!
