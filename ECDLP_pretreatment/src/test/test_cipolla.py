import unittest
from main.cipolla import cipolla



class test_cipolla(unittest.TestCase):
  ##初始化工作
  def setUp(self):
    pass
  #退出清理工作
  def tearDown(self):
    pass

  #具体的测试用例，一定要以test开头
  def test0(self):
    self.assertEqual(cipolla(2, 7), (4, 3), 'test0 fail')

  def test1(self):
    self.assertEqual(cipolla(8218,10007), (9872, 135), 'test1 fail')

  def test2(self):
    self.assertEqual(cipolla(56,101), (37, 64), 'test2 fail')

  def test3(self):
    self.assertEqual(cipolla(1,11), (1, 10), 'test3 fail')

  def test4(self):
    self.assertEqual(cipolla(8219,10007), (), 'test4 fail')



if __name__ =='__main__':
  unittest.main()