import unittest
from main.compress import compress, decompress



class test_compress(unittest.TestCase):
  ##初始化工作
  def setUp(self):
    pass
  #退出清理工作
  def tearDown(self):
    pass

  #具体的测试用例，一定要以test开头
  def test_compress(self):
    P = [1033643608831567487790089432004741658142561018071,
         726856681719841688283774655779088684746607186722]
    self.assertEqual(compress(P), ['0xb50e2eb55cd84112077a5acca94b4623a8b020d7', 0], 'test_compress fail')

  def test_decompress(self):
    P = ['0xb50e2eb55cd84112077a5acca94b4623a8b020d7', 0]
    p = 0xb77902abd8db9627f5d7ceca5c17ef6c5e3b0969
    a = 0x9021748e5db7962e1b208e3949d42ad0388a18c
    b = 0x744f47974caabdd8b8192e99da51c87f91cc453e
    self.assertEqual(decompress(P, a, b, p), [1033643608831567487790089432004741658142561018071, 726856681719841688283774655779088684746607186722], 'test_decompress fail')



if __name__ =='__main__':
  unittest.main()