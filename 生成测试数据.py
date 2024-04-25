from faker import Faker
from openpyxl import Workbook

# 创建实例
fake = Faker(locale='zh_CN')

# 定义表头
headers = ['序号', '市', '区', '街道', '社区', '采集地点', '采集管号', '身份证号', '姓名', '性别', '电话', '住址',
           '年龄', '类别', '备注', '采集时间', '采集人姓名', '采集人电话', '标本类型', '接收实验室', '检测时间', '人员关系', '箱号']

# 生成数据并写入Excel
wb = Workbook()
ws = wb.active
ws.append(headers)
for i in range(1, 3001):
    row_data = [
        i,
        '本溪市',
        fake.random_element(elements=('平山区', '溪湖区', '明山区', '南芬区')),
        fake.random_element(elements=('南地街道', '工人街道', '平山街道', '东明街道', '崔东街道', '北台街道', '河西街道', '北地街道', '石桥子街道', '桥头街道', '金山街道', '高峪街道', '东兴街道', '新明街道', '牛心台街道', '卧龙街道', '火连寨街道')),
        fake.random_element(elements=('文化社区', '中心社区', '枫桥社区', '花园社区', '棉织社区', '站前社区')),
        fake.building_number(),
        fake.random_int(min=100000000, max=999999999),
        fake.ssn(),
        fake.name(),
        fake.random_element(elements=('男', '女')),
        fake.phone_number(),
        fake.address(),
        fake.random_int(min=1, max=100),
        fake.random_element(elements=('类别1', '类别2', '类别3')),
        'NULL',
        fake.date_time_this_year(),
        fake.name(),
        fake.phone_number(),
        fake.random_element(elements=('鼻拭子', '咽拭子', '唾液样本')),
        '本溪市核酸检测基地实验室',
        fake.date_time_this_year(),
        '本人',
        fake.random_int(min=1, max=10)
    ]
    ws.append(row_data)

# 保存文件
wb.save('data.xlsx')
