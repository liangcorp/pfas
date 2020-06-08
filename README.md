Copyright 2020 Chen Liang

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


web_personal_finance is a _web based personal finance software_.
It is built with [Python][0] using the [Django Web Framework][1].

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
