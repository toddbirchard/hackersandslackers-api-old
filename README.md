# Hackers and Slackers API

![Python](https://img.shields.io/badge/Python-3.7.2-blue.svg?logo=python&longCache=true&logoColor=white&colorB=23a8e2&style=flat-square&colorA=36363e)
![Pandas](https://img.shields.io/badge/Pandas-0.23.0-blue.svg?logo=python&longCache=true&logoColor=white&colorB=23a8e2&style=flat-square&colorA=36363e)
![Flask](https://img.shields.io/badge/Flask-1.0.2-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=23a8e2&colorA=36363e)
![Flask-Redis](https://img.shields.io/badge/Flask--Redis-0.3.0-blue.svg?longCache=true&logo=redis&style=flat-square&logoColor=white&colorB=D82C20&colorA=36363e)
![BeautifulSoup](https://img.shields.io/badge/Beautifulsoup4-4.6.3-blue.svg?longCache=true&logo=delicious&longCache=true&style=flat-square&logoColor=white&colorB=23a8e2&colorA=36363e)
![PyMySQL](https://img.shields.io/badge/PyMySQL-0.9.3-red.svg?longCache=true&style=flat-square&logo=mysql&logoColor=white&colorA=36363e&colorB=4479A1)
![Sendgrid](https://img.shields.io/badge/sendgrid-5.6.0-blue.svg?longCache=true&logo=delicious&longCache=true&style=flat-square&logoColor=white&colorB=23a8e2&colorA=36363e)
![Mixpanel](https://img.shields.io/badge/mixpanel-4.3.2-blue.svg?longCache=true&logo=coderwall&longCache=true&style=flat-square&logoColor=white&colorB=002992&colorA=36363e)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.2.12-red.svg?longCache=true&style=flat-square&logo=scala&logoColor=white&colorA=36363e)
![Google Cloud Functions](https://img.shields.io/badge/Google—Cloud—Functions-v93-blue.svg?longCache=true&logo=google&longCache=true&style=flat-square&logoColor=white&colorB=23a8e2&colorA=36363e)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=36363e)
[![GitHub Issues](https://img.shields.io/github/issues/toddbirchard/hackersandslackers-api.svg?style=flat-square&colorA=36363e)](https://github.com/toddbirchard/link-embedder/issues)
[![GitHub Stars](https://img.shields.io/github/stars/toddbirchard/hackersandslackers-api.svg?style=flat-square&colorB=e3bb18&colorA=36363e)](https://github.com/toddbirchard/hackersandslackers-api/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/toddbirchard/hackersandslackers-api.svg?style=flat-square&colorA=36363e)](https://github.com/toddbirchard/hackersandslackers-api/network)

## Functionality

The Hackers and Slackers API is in active development and aimed to serve three purposes: **account creation, auto-publish to Medium,** and **mass link embeds.**

* **Link embedder:** Scans entire target site for `<a>` tags to be replaced with sophisticated link previews as embedded HTML. Aimed to improve SEO by adding rich content to sites which are link-heavy.
* **Account creation:** Aimed to simplify the onboarding process as much as possible for end users. Minimal “sign up” form  (currently two fields) accompanied with tasks needed for account creation.
* **Auto-publish to Medium:** Leverages the Medium Rest API to auto-publish posts from a Ghost blog to a Medium publication.
