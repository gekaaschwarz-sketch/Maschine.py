import os
import sqlite3
import tempfile
import unittest
from pathlib import Path
from tests.helpers import copy_script, create_test_db, run_script_in_cwd

REPO_DB = "speditions_tresor.db"


class TestIntegrityScripts(unittest.TestCase):

    def test_integrity_check_on_copy(self):
        """Run 180_integrity_check.py on a DB copy and assert PRAGMA returns ok and no FK violations."""
        with tempfile.TemporaryDirectory() as tmp:
            dst_db = Path(tmp) / REPO_DB
            create_test_db(str(dst_db))

            s180 = copy_script('10_metadata_diagnose/180_integrity_check.py', tmp)
            r = run_script_in_cwd(s180, tmp)
            conn = sqlite3.connect(str(dst_db))
            cur = conn.cursor()
            cur.execute('PRAGMA integrity_check;')
            res = cur.fetchone()[0]
            self.assertEqual(res, 'ok')
            cur.execute('PRAGMA foreign_key_check;')
            fk = cur.fetchall()
            self.assertEqual(fk, [])
            conn.close()


if __name__ == '__main__':
    unittest.main()
