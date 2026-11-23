
"""


Goal of the video
=================

How to make changes in existing code

How to create new files/pages

How to use Claude Code's Multimodal capabilities





========================================================================

command : claude

---------------------------------------------------------------------------

command : /rename landing page improvements

---------------------------------------------------------------------------

promt
.....

Add two links to the folder in @templates/based.html:

- "Terms and Conditions"
- "Privacy Policy"

Both should be plain text links, no special styling needed for now.
Point both to "#" as placeholder herfs since the pages don't exist yet.

Do  not modify anything else on the page.

---------------------------------------------------------------------------


! git add.
! git commit -m "landing: and terms and privacy links to folder"

---------------------------------------------------------------------------

Promt
.....

Create a "Terms and Conditions" pages for Spendly.

1. Add a new route in [@app.py](http://app.py/):
GET /terms - renders templates/terms.html
2. Create templates/terms.html with genric terms and conditions
content appropriate for a personal expense tracking app.
Includes sections link: Acceptance of Terms, Use of Service,
User Data, Limitations of liability, and Changes to Terms.
Extend base.html if it exists, otherwise match the style of landing.html.
3. In templets/landing.html, update the "Terms and Conditions" 
footer link herf from "#" to "/terms".


Promt 
.....

Also make sure the appearance of 
@templates/terms.html matches the website's theme


-------------------------------------------------------------------------------

!git add.
!git commit -m "landing: add terms and conditions page and route"


-------------------------------------------------------------------------------

Promt
.....

Do the same as you did for the Terms and conditions page,
but for Privacy Policy.

1. Add a new route in [@app.py](http://app.py/):
GET /terms - renders templates/terms.html
2. Create templates/terms.html with genric terms and conditions
content appropriate for a personal expense tracking app.
Includes sections link: Acceptance of Terms, Use of Service,
User Data, Limitations of liability, and Changes to Terms.
Extend base.html if it exists, otherwise match the style of landing.html.
3. In @templets/landing.html, update the "Terms and Conditions" 
footer link herf from "#" to "/terms".
4. Make sure the appearance looks like the website's theme

! git add.
!git commit -m "landing: add privacy policy page and route"


-------------------------------------------------------------------------------------------------------------------------

I have attached a screenshot of the updated spedly hero sections design.

Modify only the hero section in @templates/langing.html and 
@static/css/landing.css
to match this image exactly. Do not touch any other part of the page.

! git add.
!git commit -m "redesign hero section to match mockup"


-------------------------------------------------------------------------------------------------------------------------

Add a modal to templates/landing.html that opens when the user clicks
"See how it works".

Requirements:

- Clicking "See how it works" opens a model overlay
- Modal contains an embedded YouTube video (use any placeholder
  YouTube URL)
  for now, I will replace it lator)
- Video should be playable inside the modal
- Clicking the close button OR clicking outside the modal close it
- When the modal closes, the video must stop playing (not continue in
  background)
- No page libraries or dependencies - vanilla JS only, since we are not 
  using any JS framework in this project

- Do not modify any other part of the page.

! git add.
!git commit -m "landing: add youtube model on see how it works click"


-------------------------------------------------------------------------------------------









good strategies is that
-----------------------

Do not write promt manually 
It means first we write our promt on any chat bot and its out copy past in file.txt


role of @ is to inform cloude to work in that file




"""