from views.app_user import dao

#系统刷新
def xtrefresh():
    idlist = dao.query_idlist()
    for i in idlist:
        print(i['id'])
        user_id = i['id']
        user_info = dao.get_profile(i['id'])
        sql = 'select * from wklc_users ' \
              'where id=%s'
        user_datas = dao.query(sql, user_id)[0]
        money = 0
        for i in user_info[:-2]:
            money += i["num"]
        totalMoney = float('%.2f' % (user_datas['zyMoney'] + money))
        yersterdayReturn = user_info[5]['num']
        totalReturn = user_info[6]['num']
        print('yes',yersterdayReturn)
        print('tot',totalReturn)
        dao.update_user(totalMoney, yersterdayReturn, totalReturn, user_id)
if __name__ == '__main__':
    xtrefresh()