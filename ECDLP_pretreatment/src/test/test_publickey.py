import unittest
from main.publickey import getPublicKey
from main.compress import decompress



class test_publickey(unittest.TestCase):
  ##初始化工作
  def setUp(self):
    pass
  #退出清理工作
  def tearDown(self):
    pass

  #具体的测试用例，一定要以test开头
  def test_publickey(self):
    p = 0xb77902abd8db9627f5d7ceca5c17ef6c5e3b0969
    a = 0x9021748e5db7962e1b208e3949d42ad0388a18c
    b = 0x744f47974caabdd8b8192e99da51c87f91cc453e
    n_a = 0x9022802bb688656ee1914e6dd7f74e1ecd1d6780
    P = ['0x4f1ecacc3b1e56066b02f6a6033f940fc5c9805',0]
    compress_Q_a =  ['0xb50e2eb55cd84112077a5acca94b4623a8b020d7', 0]
    self.assertEqual(getPublicKey(P,n_a, a, b, p), decompress(compress_Q_a, a, b, p), 'test_publickey fail')


if __name__ =='__main__':
  unittest.main()