web_personal_finance is a _web based personal finance software_.
It is built with [Python][0] using the [Django Web Framework][1].

Copyright (C) 2020  Chen Liang

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

# web_personal_finance

This project has the following basic apps:

* Accounting (An accounting app that tracks Assets, Liabilities, Incomes and Expenses.)
* Report (A report app that presents graphic overview of the accounts and transactions.)
* Investment (A investment tracking app that tracks all of the purchased stocks.)

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv web_personal_finance`
    2. `$ . web_personal_finance/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate

### Detailed instructions

Take a look at the docs for more information.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
