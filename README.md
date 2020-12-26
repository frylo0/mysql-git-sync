# MySQL GIT SYNC
## Sync your DB via GitHUB

## Installation & Usage

1. Clone repo: `git clone https://github.com/fritylo/mysql-git-sync`
2. Run start.py script: `python3 start.py`, to store DB connection data
3. Create system alias for `db-pull.py` and `db-push.py` scripts call:
   - Linux aliases: [how to](https://shapeshed.com/unix-alias/)
   - Windows aliases: [how to](https://superuser.com/questions/560519/how-to-set-an-alias-in-windows-command-line)
4. Create `SQLDUMP` folder in you project folder.
5. Use aliases to sync via github.