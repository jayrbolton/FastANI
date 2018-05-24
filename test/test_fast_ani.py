import os
import sys
import unittest
import tempfile
dirname = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(dirname, '../lib/FastANI/')))

from utils.fast_ani_output import get_result_data, create_html_tables  # noqa
from utils.fast_ani_proc import run_fast_ani_pairwise  # noqa

# Test the fastANI python utilites in /lib/FastANI


class TestFastANI(unittest.TestCase):

    @unittest.skip('x')
    def test_fast_ani_proc_and_output(self):
        data_dir = os.path.join(dirname, 'data')
        path1 = os.path.join(data_dir, 'shigella.fna')
        path2 = os.path.join(data_dir, 'ecoli.fna')
        # print(path1, path2)
        self.assertTrue(os.path.isfile(path1))
        self.assertTrue(os.path.isfile(path2))
        tmp_dir = tempfile.mkdtemp()
        out_paths = run_fast_ani_pairwise(tmp_dir, [path1, path2])
        self.assertEqual(set(out_paths), set([
            os.path.join(tmp_dir, 'ecoli-shigella.out'),
            os.path.join(tmp_dir, 'shigella-ecoli.out')
        ]))
        result_data = get_result_data(out_paths)
        # print(result_data)
        self.assertEqual(len(result_data), 2)
        self.assertEqual(result_data[0]['orthologous_matches'], '1324')
        self.assertEqual(result_data[0]['percentage_match'], '97.6765')
        self.assertEqual(result_data[0]['total_fragments'], '1547')
        html = create_html_tables(result_data)
        # print(html)
        self.assertGreater(len(html), 0)


if __name__ == '__main__':
    unittest.main()
