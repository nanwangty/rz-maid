# 这是一个计数器 调用一次数字加1 并return 出去
import pickle

def jishu():
    with open('jishu.pkl', 'rb')as f:
        shu = pickle.load(f) + 1
        with open('jishu.pkl', 'wb')as z:
            pickle.dump(shu,z)
            return shu

