from libs import rd
import uuid
def new_token():
    return uuid.uuid4().hex
def save_token(token,user_id):
    #保存
    rd.set(token,user_id)
    rd.expire(token, 12 * 3600)  # 有效时间： 12小时
def check_token(token):
    # 验证token
    return rd.exists(token)
def get_token_user_id(token):
    # 通过token获取user_id
    if check_token(token):
        return rd.get(token).decode()
if __name__ == '__main__':
    # print(rd.exists('e620b40cd10d4049b12fd47787d36dc1'))
    print(rd.get('6b5110772b24453599e90bfb59794149').decode())
