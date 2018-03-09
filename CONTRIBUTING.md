# Contributing guidelines

1. Developer writes some code. When this code changes schema developer calls
   `makemigrations`:
   * `python manage.py makemigrations`

3. This generates migrations file in the migrations directory.

4. Developer applies migrations locally and tests changes:
   * `python manage.py migrate`

5. If the developer is satisfied, the pull/merge request is opened.

5. Reviewers of the code will check the change.<br>
   If the change contains modifications that require upgraded schema, reviewers
   will check if the correct migration files are present in the migrations
   directory (that is, the user called `makemigrations` and migration files were
   generated).

6. After the PR, server will backup the deployed database and will try to run:
   * `python manage.py migrate`

7. Reviewer will check the result of the migrations.

8. If the migration on server succeeded and the reviews are positive, merge can get approved.
