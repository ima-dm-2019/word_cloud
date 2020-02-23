# 用来做词云
import wordcloud
# 用来做词云形状图片
import imageio
# 用来做List向字符串的转换
import jieba

# 设置词云的形状背景以待选择
mk_1 = imageio.imread("dollar.png")
mk_2 = imageio.imread("money.png")
mk_3 = imageio.imread("robot.png")
mk_4 = imageio.imread("chinamap.png")


# 将已经处理好的List作为参数传入即可
def make_word_cloud(textlist):
    # 选择词云背景
    a = choosing_background()
    # 创建词云对象
    w = create_one(mk=a)
    # 将传入List变成字符串
    string = " ".join(textlist)
    # 将词云对象和文本信息结合
    w.generate(string)
    saving(w)
    print("词云生成成功！")


# 选择词云背景，这里只挑了mk_1和mk_3，后续还可以再调
def choosing_background():
    print("请告诉我你要设置怎样的词云背景。\n")
    print("1或者2是金融类，3科技，4中国地图")
    # 如果没有这一行代码，会出现“local variable 'mk'referenced before assignment”的问题,所以先随便赋一个值
    mk = imageio.imread("dollar.png")
    loop = 1
    while loop == 1:
        option = input("你的选择是：")
        if option == 1:
            mk = mk_1
            break
        elif option == 2:
            mk = mk_2
            break
        elif option == 3:
            mk = mk_3
        elif option == 4:
            mk = mk_4
        else:
            pass
        break
    return mk


# 创建一个词云对象，将设置好的词云背景作为参数传入
def create_one(mk):
    w = wordcloud.WordCloud(width=1000,
                            height=700,
                            background_color='white',
                            font_path='msyh.ttc',
                            scale=15,
                            mask=mk,
                            )
    return w


# 保存为图片，在输出图片的时候需要设置名称
def saving(w):
    name = input("请告诉我这个词云叫什么：")
    picture_name = "{x}.png".format(x=name)
    w.to_file(picture_name)


if __name__ == '__main__':
    # 预设了一个列表，可以试着运行一下，能生成词云，不过列表太小了，没什么实际效果就是了
    str = ['动力学', '和', '电磁学']
    make_word_cloud(textlist=str)
