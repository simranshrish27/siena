import unittest
from algoassignment import *
gui=Tk()
root= Student(gui)
class test(unittest.TestCase):
    def test_search(self):
        list= [('1', 'simran', 'siris', 'Bsc(Hons)computing', 'kathmandu', '9812918149'),
                ('4', 'susma', 'bashyal', 'Bsc(Hons)computing', 'butwal', '888888'),
                ('3', 'dev', 'mainali', 'Bsc(Hons)ethical', 'airport', '666666')]
        ex_result=[('3','dev','mainali', 'Bsc(Hons)ethical','airport','666666')]

        root.combo_search.set("first_name")
        root.Esearch.insert(0, 'dev')

        ac_result = root.search_item(list)
        self.assertEqual(ex_result,ac_result)

    def test_bubble_sort(self):
        list = [('1', 'simran', 'siris', 'Bsc(Hons)computing', 'kathmandu', '9812918149'),
                ('4', 'susma', 'bashyal', 'Bsc(Hons)computing', 'butwal', '888888'),
                ('3', 'dev', 'mainali', 'Bsc(Hons)ethical', 'airport', '666666')
                ]
        ex_result = [('1', 'simran', 'siris', 'Bsc(Hons)computing', 'kathmandu', '9812918149'),
                     ('3', 'dev', 'mainali', 'Bsc(Hons)ethical', 'airport', '666666'),
                     ('4', 'susma', 'bashyal', 'Bsc(Hons)computing', 'butwal', '888888')]

        root.combo_sort.set("student_id")
        actual = root.bubble_sort(list)
        self.assertEqual(ex_result, actual)


if __name__ == '__main__':
    unittest.main()
