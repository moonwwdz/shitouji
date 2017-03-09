strs = '却不知将来如何。若问那赦公，也有二子。长名贾琏，今已二十来往了。亲上作亲，娶的就是政老爹夫人王氏之内侄女，【甲戌侧批：另出熙凤一人。】今已娶了二年。这位琏爷身上现捐的是个同知，也是不肯读书，于世路上好机变，言谈去的，所以如今只在乃叔政老爷家住着，帮着料理些家务。谁知自娶了他令夫人之后，倒上下无一人不称颂他夫人的，琏爷倒退了一射之地。说模样又极标致，言谈又爽利，心机又极深细，竟是个男人万不及一的。”【甲戌侧批：未见其人，先已有照。甲戌眉批：非警幻案下而来为谁？】 雨村听了，笑道：“可知我前言不谬。【甲戌侧批：略一总住。】你我方才所说的这几个人'
out = "<p>"
s_list = []
out_list = []
mark = ["，","。","“","”","："]
for i,s in enumerate(strs):
    if i+1 == len(strs):
        break
    if s in ["】"]:
        #         print("<ruby>"+"".join(s_list).replace('【',"")+"</ruby>")
        out_list.append("<ruby>"+"".join(s_list).replace('【',"")+"</ruby>")
        s_list = []
    elif strs[i+1] in ["【","】"]:
        s_list.append(s+"<rt>")
    elif s not in mark:
        s_list.append(s)
    else:
        s_list.append(s)
        if "【" not in s_list:
            #             print("=="+"".join(s_list).replace('【',""))
            out_list.append("".join(s_list).replace('【',""))
            s_list = []
out += "".join(out_list)
out += "</p>"
print(out)