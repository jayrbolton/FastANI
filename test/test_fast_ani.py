import os
import sys
import unittest
dirname = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(dirname, '../lib/FastANI/')))

from fast_ani_output import get_result_data, create_html_tables  # noqa
from fast_ani_proc import run_fast_ani_pairwise  # noqa

# Test the fastANI python utilites in /lib/FastANI


class TestFastANI(unittest.TestCase):

    def test_fast_ani_proc_and_output(self):
        dir = os.path.abspath(dirname + '/../data')
        path1 = os.path.join(dir, 'shigella.fna')
        path2 = os.path.join(dir, 'ecoli.fna')
        out_paths = run_fast_ani_pairwise('/tmp', [path1, path2])
        self.assertEqual(set(out_paths), set([
            '/tmp/ecoli-shigella.out',
            '/tmp/shigella-ecoli.out'
        ]))
        result_data = get_result_data(out_paths)
        print(result_data)
        self.assertEqual(len(result_data), 2)
        self.assertEqual(result_data[0]['orthologous_matches'], '1324')
        self.assertEqual(result_data[0]['percentage_match'], '97.6765')
        self.assertEqual(result_data[0]['total_fragments'], '1547')
        html = create_html_tables(result_data)
        print(html)
        self.assertGreater(len(html), 0)


if __name__ == '__main__':
    unittest.main()