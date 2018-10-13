Changelog
=========

v0.0.9 - 2018-10-13
-------------------

Added
^^^^^

- Responsive menu for the mobile view

v0.0.8 - 2018-10-13
-------------------

Added
^^^^^

- The project name and version is now included in the :code:`<title>` tag.

Changed
^^^^^^^

- The link animation element on menu items has been moved to the :code:`<li>`
  element to be more consistent with the "selected menu item" styling.

Fixed
^^^^^

- Fixed the link back to the homepage for projects that are hosted on some
  subdomain.
- Implemented a potential fix for certain elements now resizing responsively on
  mobile

v0.0.7 - 2018-10-13
-------------------

Fixed
^^^^^

- The appropriate section is now highlighted on mobile
- Figure captions are now centered
- Implemented a more compact menu design which should fix the disappearing menu
  items issue on narrower screens.

v0.0.6 - 2018-08-30
-------------------

- New "Fancy" section headers.
- Site title now follows the user down the page in desktop view
- Added a fade animation on the background colors of :code:`:target` so the user
  knows what it is

- Fix for long code examples overflowing their borders


v0.0.5 - 2018-08-28
-------------------

- Improved layout (in my opinion :) )
  + Sidebar now on the left
  + White background throughout, fewer coloured borders

- Better font choice, inline code is more obvious now

- Improved admonition styles, they take up less space and (hopefully) more
  interesting to look at

- Navigation sections now give some feedback showing which section the user is
  currently in


v0.0.4 - 2018-08-05
-------------------

Add MathJax support, demo site and first parts of search

- Add support for rendering mathematics using the :code:`:math:` role and
  :code:`.. math::` directive
- The javascript required for search is now loaded on the search page,
  just need to figure out how to display the results.
- Fleshing out the demo site, showing a few code examples, tables,
  figures, maths and more


v0.0.3 - 2018-07-18
-------------------

- Fix main.css path

v0.0.2 - 2018-07-18
-------------------

- Fix missing css in package

v0.0.1 - 2018-07-18
-------------------

- Initial release
