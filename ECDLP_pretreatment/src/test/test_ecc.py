import unittest
from main.ecc import calculate_p_q, calculate_2p, calculate_np



class test_ecc(unittest.TestCase):
  ##初始化工作
  def setUp(self):
    pass
  #退出清理工作
  def tearDown(self):
    pass

  #具体的测试用例，一定要以test开头
  def test_add(self):
    self.assertEqual(calculate_p_q(2, 3, 12, 11, 3, 8, 13), [9, 7], 'test_add fail')

  def test_double(self):
    self.assertEqual(calculate_2p(2, 3, 3, 8, 13), [12, 11], 'test_double fail')

  def test_mul(self):
    self.assertEqual(calculate_np(9, 2, 3, 3, 8, 13), [0, 0], 'test_mul fail')


if __name__ =='__main__':
  unittest.main()