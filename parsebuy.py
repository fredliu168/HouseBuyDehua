# coding:utf-8
import pandas as pd
from pyplotz.pyplotz import PyplotZ
from pyplotz.pyplotz import plt
import datetime as dt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # for Chinese characters

def draw_pie(labels, quants):
    # make a square figure
    plt.figure(1, figsize=(10, 10))
    # For China, make the piece explode a bit
    expl = [0]*len(quants)  # 第二块即China离开圆心0.1

    expl[2] = 0.1
    # Colors used. Recycle if not enough.
    colors = ["blue", "red", "coral", "green", "yellow", "orange"]  # 设置颜色（循环显示）
    # Pie Plot
    # autopct: format of "percent" string;百分数格式
    plt.pie(quants, textprops = {'fontsize':15, 'color':'k'},explode=expl, colors=colors, labels=labels, autopct='%1.1f%%', pctdistance=0.8, shadow=False)
    plt.title('嘉裕花苑二期项目5#-18#楼1500户申购入围家庭所在乡镇', bbox={'facecolor': '0.8', 'pad': 5})


    plt.show()
    # plt.savefig("png.jpg")
    plt.close()



def town_count():
    town = df['town'].value_counts()
    town_df = town.to_frame()

    index = town_df.town.index.tolist()
    counts = town_df['town'].tolist()

    plt.figure(figsize=(9, 6))

    # 画线条
    l2, = plt.plot(index, counts, color='red', linewidth=1.0, linestyle='--', label='square line')
    # 画柱状图
    plt.bar(index, counts, alpha=0.9, width=0.55, facecolor='lightskyblue', edgecolor='white', label='one', lw=1)
    plt.xticks(rotation=45, fontsize=10)
    plt.title('嘉裕花苑二期项目5#-18#楼1500户申购入围家庭所在乡镇')
    plt.xlabel("乡镇")
    plt.ylabel("人数")

    # 设置数字标签
    for a, b in zip(index, counts):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)

    plt.show()

    draw_pie(index, counts)


def country():
    #print(df.loc[df["town"] == "龙门滩"])
    country = df.loc[df["town"] == "葛坑"]['country'].value_counts()
    country_df = country.to_frame()

    index = country_df.country.index.tolist()
    counts = country_df['country'].tolist()
    plt.figure(figsize=(9, 6))
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # for Chinese characters
    plt.bar(index, counts, alpha=0.9, width=0.55, facecolor='lightskyblue', edgecolor='white', label='one', lw=1)
    plt.xticks(rotation=45, fontsize=10)
    # 设置数字标签
    for a, b in zip(index, counts):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)

    plt.title('嘉裕花苑二期项目5#-18#楼1500户申购入围家庭所在乡镇')
    plt.show()


def fun(x):
    return x[6:10]


def age_show():
    # 显示年龄分布情况
    now_year = dt.datetime.today().year  # 当前的年份
    # 计算年龄
    df['birth'] = pd.to_datetime(df['userid'].map(fun))
    df['Age'] = now_year - df.birth.dt.year
    t = df

    age2 = t[(t.Age >= 20) & (t.Age < 25)]['Age'].count()
    age3 = t[(t.Age >= 25) & (t.Age < 30)]['Age'].count()
    age4 = t[(t.Age >= 30) & (t.Age < 35)]['Age'].count()
    age5 = t[(t.Age >= 35) & (t.Age < 40)]['Age'].count()
    age6 = t[(t.Age >= 40) & (t.Age < 45)]['Age'].count()
    age7 = t[(t.Age >= 45) & (t.Age < 50)]['Age'].count()
    age8 = t[(t.Age >= 50) & (t.Age < 55)]['Age'].count()
    age9 = t[(t.Age >= 55) & (t.Age < 60)]['Age'].count()
    age10 = t[(t.Age >= 60) & (t.Age < 80)]['Age'].count()

    s = pd.DataFrame({'人数': [age2, age3, age4, age5, age6, age7, age8, age9, age10]},
                     index=['20-25', '25-30', '30-35', '35-40', '40-45', '45-50', '50-55', '55-60', '60-76'])

    s.plot(kind='bar')
    plt.title('嘉裕花苑二期项目5#-18#楼1500户申购入围家庭年龄分布')
    plt.show()

    Age = df.Age.value_counts()
    print(Age)
    Age = Age.to_frame()
    Age = Age.sort_index()
    print(Age)
    Age.plot(kind='line')
    plt.title('嘉裕花苑二期项目5#-18#楼1500户申购入围家庭年龄分布')
    plt.show()

if __name__ == '__main__':
    pltz = PyplotZ()  # create an instance
    df = pd.read_csv('./data/buyer.csv')
    df.columns = ['id', 'id1', 'username', 'town', 'country', 'userid', 'marry']

    town_count()
