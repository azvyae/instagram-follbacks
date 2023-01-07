# Instagram Follbacks

Instagram Follbacks is a Python console application that allows you to see which of your Instagram followers are not following you back. You can also exclude certain users from the list (for example, official accounts that are clearly not going to follow you back but you don't want to include them in the list). You can also keep track of the accounts you have unfollowed by saving them in a list, so that they don't appear in the list again.

## Preparation

To prepare your accounts, make sure you have a folder with your username in the `accounts` folder, and place your `following.json`, `follower.json`, `exclude.json` (optional), and `unfollowed.json` (optional) files there. Sample `exclude.json` and `unfollowed.json` files can be found in the `accounts/sample` folder.

To obtain the `following.json` and `follower.json` files, go to your Instagram privacy settings and download your data in JSON format. Then save the `following.json` and `follower.json` files in the `accounts/<username>` folder.

## Run the App

To run the application, use the command `python main.py <username>` or `python3 main.py <username>`, or if no username is specified, you will be prompted to enter it before continuing.

Example command:

Copy code

```shell
python main.py johnsmith
``` 

thanks to [@talaexe](https://github.com/talaexe) for inspiring me expanding the [WhoDoesntFollowBackIG](https://github.com/talaexe/WhoDoesntFollowBackIG) functionality


I hope this helps! Let me know if you have any questions.
