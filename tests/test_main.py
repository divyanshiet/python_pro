import contextlib
import io
import unittest

from school_app import main


class TestSchoolApp(unittest.TestCase):
    def test_main_runs_and_prints_average(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            main()

        rendered = output.getvalue()
        self.assertIn("All tasks completed", rendered)
        self.assertIn("88.5", rendered)


if __name__ == "__main__":
    unittest.main()
