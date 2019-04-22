# Hackers and Slackers API

![Python](https://img.shields.io/badge/Python-3.7.2-blue.svg?logo=python&longCache=true&logoColor=white&colorB=23a8e2&style=flat-square&colorA=36363e)
![Pandas](https://img.shields.io/badge/Pandas-0.23.0-blue.svg?logo=python&longCache=true&logoColor=white&colorB=23a8e2&style=flat-square&colorA=36363e)
![Flask](https://img.shields.io/badge/Flask-1.0.2-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=23a8e2&colorA=36363e)
![Flask-Redis](https://img.shields.io/badge/Flask--Redis-0.3.0-blue.svg?longCache=true&logo=redis&style=flat-square&logoColor=white&colorB=D82C20&colorA=36363e)
![BeautifulSoup](https://img.shields.io/badge/Beautifulsoup4-4.6.3-blue.svg?longCache=true&logo=delicious&longCache=true&style=flat-square&logoColor=white&colorB=23a8e2&colorA=36363e)
![PyMySQL](https://img.shields.io/badge/PyMySQL-0.9.3-red.svg?longCache=true&style=flat-square&logo=mysql&logoColor=white&colorA=36363e&colorB=4479A1)
![Sendgrid](https://img.shields.io/badge/sendgrid-5.6.0-blue.svg?longCache=true&logo=delicious&longCache=true&style=flat-square&logoColor=white&colorB=23a8e2&colorA=36363e)
![Mixpanel](https://img.shields.io/badge/mixpanel-4.3.2-blue.svg?longCache=true&logo=coderwall&longCache=true&style=flat-square&logoColor=white&colorB=002992&colorA=36363e)
![Flask-SQLAlchemy](https://img.shields.io/badge/Flask--SQLAlchemy-2.3.2-red.svg?longCache=true&style=flat-square&logo=scala&logoColor=white&colorA=36363e)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=36363e)
[![GitHub Issues](https://img.shields.io/github/issues/toddbirchard/hackersandslackers-api.svg?style=flat-square&colorA=36363e)](https://github.com/toddbirchard/link-embedder/issues)
[![GitHub Stars](https://img.shields.io/github/stars/toddbirchard/hackersandslackers-api.svg?style=flat-square&colorB=e3bb18&colorA=36363e)](https://github.com/toddbirchard/hackersandslackers-api/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/toddbirchard/hackersandslackers-api.svg?style=flat-square&colorA=36363e)](https://github.com/toddbirchard/hackersandslackers-api/network)

## What Is This Thing?

This is an API serving a Ghost blog: [Hackers and Slackers dot com](https://hackersandslackers.com/). Under the constraints of a blog theme, this API was created to provided additional functionality to an otherwise simple app designed solely to serve content. While still in active development, this project serves a number of purposes:

### Link Embedder
* Replaces a given site’s `<a>` with sophisticated link previews as embedded HTML.
* Scrapes the following from any given URL:
  * Title
  * Description
  * Preview image
  * Author
  * Publish Date
  * Tags
  * Domain Origin
* Metadata is embedded as pure HTML to improve the site owner’s SEO and user friendliness by adding rich content to sites which are link-heavy.
* Site content is modified by directly interacting with the site's database.

### Account creation
* A collection of features aimed to simplify the sign up processes as much as possible.
* Infers information about the user to simplify onboarding.
* Welcomes new users via a Sendgrid mailer.

### Auto Syndication
* Automates the syndication of new posts to content platforms lacking this functionality (namely Medium)

### Analytics... stuff.
* It's complicated.
