# Court Love - Testing

[Live link to website](https://court-love-8302d0b2e53d.herokuapp.com/)


## Automated testing


### HTML validator
- Some issue came up about h2 tags on the **All lessons** page. This is because I adjust the heading content depending on which button is clicked, and I did not separate the h2 per category or place, so this resulted in either an empty h2 tag or a trailing h2 tag. So I fixed this with separate h2 blocks and added a class to display them on one line next to each other. So in case there is both a category and a place, there is a correct heading visible, that consists of two h2 blocks next to each other.

### CSS validator

### Python validator

### Javascript validator

### Lighthouse testing



## Manual testing


### User story testing

### Issues

#### Capacity handler
# capacity handler (https://stackoverflow.com/questions/61310901/how-to-update-a-value-from-table-accessed-via-foreign-key-django-orm)
                    # this does not work as the capacity model is changed, it should not. I should change this to a normal field I think. Or have new field in lesson with capacity left that gets updated?






10:27
So first I wanted to use the same field but it was better with a separate field.


Lizzy_4P
  3:11 PM
delete order line item in checkout when places left is 0, did not work I got an error message. so I moved it to the card instead, also changed the direclyt to chekout to go to cart.


Lizzy_4P
  11:24 AM
works good in checkout, but you can go to the cart and see the item there again. but you cant checkout with it
11:29
could add same code to cart view?


Lizzy_4P
  11:50 AM
I put correct code in cart and removed from chekout. Also, in the toast I changed so that you have to go to cart first, so chekout get the updated cart. Now there is an issue if the user would use the chekout url and not go viacart...


Lizzy_4P
  11:58 AM
i put a code in chekout that it goes back to cart incase there is a lesson with 0


Lizzy_4P
  11:05 AM
now you can comple purchase and then add same lesson and pay again. Unfixed bug. But however, not a lot will force themselces to pay twice :)

#### Date range (unfixed)
Lizzy_4P
  12:35 AM
DateFromToRangeFilter did not work, I could not get it to work, so I remove django_filters and did something else. User story: as a site user, I can select a date range in which I want to see offered lessons so that I can easily adapt the list of lessons on dates I can attend. could have, since people can scroll






12:37
And there will not be super many lessons out there

#### Lesson images
I wanted to have images with the lesson, even though it is not neccesary. So I did not want to give the user the possibility of uploading an image, as it is not neccessary, but I still want to give some choice to the user in which image will be used. So I fount this interesting option of using choices (https://stackoverflow.com/questions/31948172/python-django-form-where-user-selects-from-a-list-of-images, by Pynchia), which seemed easy and enough for the MVP. To make this work, I also followed the instructions of Melvyn Sopacua here (https://groups.google.com/g/django-users/c/iP2TmUHwdDI). 

#### Whitespace validation
The **Add lesson** form has the CharField **Name** and TextField **Description**. They are requered fields, but when I tested to fill in white spaces and click **Add lesson**, it did not give an error. I searched for this issue and found that Django does allow Char- and TextFields to have an empty string even if they are required (i.e. https://forum.djangoproject.com/t/charfield-not-enforcing-null-constraint/35127). So I looked at a solution with customising the form field for these two fields, adding a validator to check for a minimum length of 1 (*validators=[MinLengthValidator(1)]*). But this did not change anything. I then retested the form and treid to fill in the other fields and whitespaces in the **Name** and **Description** field, and then I actually got errors on those fields that they are required. So apparently, these errors are not triggered when most of the fields are empty, but they are triggered when a few are empty.

#### Profile image
remove checkbox in image selection, very weird that it stayd vlue when selected. Something with bootstrap. In the devtools, the correct background colour was set, but it was actually blue. Even though I managed to override it in the checkout form to green, i did not manage to change it to red. So I redid it with a white background and red text.

because my image solution is different than in the walkthrough which has different views for adding and editing, I had an issue since updating hte image is in the same view, and I needed to refresh the page to see the remove button, or to see it removed. So I tried with javascript but that did not work. In the end, a simple redirect to profile url fixes this issue, now the remove option is gone directly after removing an image, and it is added directlt after adding an image.

### Full testing


#### Browser testing

#### Device testing

Tested extensively on a Dell laptop, and on a Lenovo laptop, and Huawei phone. All works well.

#### Feature testing

#### Unfixed bugs
You cannot add a lesson to the cart more than once, but if you complete the purchase, you can add the same lesson to the empty cart and pay for it again. I left this like it is, because not a lot of people will force themselves to pay for the same lesson twice by actively adding the lesson to the cart again. If they would, it would be their mistake and they can contact Court Love to cancel it.



