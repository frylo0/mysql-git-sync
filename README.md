# MySQL GIT SYNC
## Sync your DB via GitHUB

## Installation & Usage

1. Clone repo: `git clone https://github.com/fritylo/mysql-git-sync`.
2. Run start setup: `python3 dbd.py start`, to setup DB connection data.
3. Create system alias for `dbd.py` script:
   - Linux aliases: [how to](https://shapeshed.com/unix-alias/)
   - Windows aliases: [how to](https://superuser.com/questions/560519/how-to-set-an-alias-in-windows-command-line)
4. Create `SQLDUMP` folder in you project folder.
5. Use aliases to sync via github:
   - push: `dbd push`.
   - pull: `dbd pull`.
6. If you change password or login of you DB run start setup again (2.).