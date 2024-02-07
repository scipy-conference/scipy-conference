# Auto-Emailer
Simple script to automate the process of sending mass emails

## Components
The `auto_email.py` script has 2 main components: the `RECIPIENTS_FILE` and the `HTML_FILE`.
- The `RECIPIENTS_FILE` should contain the first name, last name, and email addresses of those being sent the email. The format is explicit:

    ```
    First Last email@provider.com,
    Logan Thomas logan.thomas005@gmail.com
    ```
- The `HTML_FILE` is the template for rendering the email message. Placeholders can be used with `{{}}` (e.g. `{{Name}}`).

## To Run
- The `HTML_FILE` variable should be updated to the `.html` file template you plan to use (`'draft_email_proposal.html'`). It is left as `'test.html'` so you can dry run things before sending out.
- Be sure to change the email signature name to your own rather than mine (Logan Thomas)
- The `RECIPIENTS_FILE` file should be updated to include a list of those whom you wish to send the email to. The format is `First Last email@com.com,`.
I’d send to about 50 at a time so that you don’t have to worry about sending all at once.
- To run, execute the command `python auto_email.py` and provide the password for the tutorials@scipy.org email address
- I think any python 3.6+ will work, but if IIRC I was running on 3.11.
