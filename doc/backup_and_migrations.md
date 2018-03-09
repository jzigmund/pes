# Database backup

### Backup process

Optional checks before actual dump:
* check if database that should be backed up exists
* check if the destination is writable and there is enough space for the dump

Create the dump, use `gzip` to save space

```shell
pg_dump -U postgres originaldb | gzip > /path/to/dump.sql.gz
```


### Restore process

Pick a name for backup db, e.g. originaldb_suffix

Optional checks before restoration:
* check if there already does not exist db with the same name

Create a database where the dump should be restored and set owner

```shell
createdb -U postgres -O owner originaldb_suffix
```

Restore the dump to the newly created database

```shell
gunzip -c /path/to/dump.sql.gz | psql -U postgres originaldb_suffix -1 -f -
```

With option `-1` the whole dump will be restored as a single transaction, i.e.
the restore is either fully completed or fully rolled back.

Optional check for success of the restore.

### Cleanup

Delete intermediate dump file

```shell
rm /path/to/dump.sql.gz
```

### Notes

All checks are optional in a sense that whenever any of the condition is violated,
dump or restore will eventually fail with corresponding error log. Moreover the
check for sufficient storage is tricky because the size of the dump is nearly
impossible to calculate, especially when compression is used.

All steps can be concatenated to one command to avoid checking for success of previous one.

### Summary

Needed inputs:
* `dump_dir` - directory for the dump file
* `originaldb` - name of the original database to clone
* `db_suffix` - suffix for creating the new database name, eg date
* `owner` - owner of the cloned database

### Concatenated steps

```shell
dump_path="${dump_dir}"/"${originaldb}".sql.gz
createdb -U postgres -O "${owner}" "${originaldb}"_"${db_suffix}" && \
pg_dump -U postgres "${originaldb}" | gzip > "${dump_path}" && \
gunzip -c "${dump_path}" | psql -U postgres -d "${originaldb}"_"${db_suffix}" -1 -f - && \
rm "${dump_path}"
```

---

# Schema migration

We are using Django for handling the schema migrations.

Check the Django docs for more info (especially `makemigrations`, `migrate` and `showmigrations`)
https://docs.djangoproject.com/en/2.0/topics/migrations/

The migration is currently handled as following:


1. Server detects if there are any pending migrations left to be applied:
    * `python3 ${PES_PROJECT_ROOT}/manage.py showmigrations | grep '\[ \]' | wc -l)"`

2. If there are any migrations detected, server backs up the database.

3. Lastly, migrations are applied:
   * `python3 "${PES_PROJECT_ROOT}"/manage.py migrate`


See backup and migrate script for details:
`pes-service/root/etc/pes/init.d/20-backup-and-migrate.sh`
