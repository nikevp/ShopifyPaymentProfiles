# ShopifyPaymentProfiles
Load and edit checkout profiles for Shopify

About:
- Uses Tkinter for gui
- Looks for a profile.json file on load. If none, it will create one when a profile is saved.

All existing profiles are displayed by email on the right:
  - Clicking a profile autofills the form with the saved information.

When saving a profile:
  - If it exists the profile will be updated. (profiles are uniquely identified by email)
  - If it does not exist the profile will be added to profiles.json and a button will be generate on the right of the form.
  
To Do:
  - Add a delete button
  - Change the profile buttons to a scrolling list?


## Screenshot
![screen shot](http://i.imgur.com/ZEYyD2y.png)
