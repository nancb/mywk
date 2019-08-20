from redis import Redis
rd= Redis(host='121.199.63.71',
           port=6376,db=1)
if __name__ == '__main__':
    # print(rd.exists('sdasda'))
    print(rd.keys('*'))

    # rd.flushall()
    # print(rd.get('e620b40cd10d4049b12fd47787d36dc1'))