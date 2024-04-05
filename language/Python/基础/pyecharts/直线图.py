from pyecharts.charts import Line
from pyecharts.options import TitleOpts

line = Line()

line.add_xaxis(["美国","中国","日本"])
line.add_yaxis("GDP",[50,30,20])

# 配置选项
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示",pos_left="center",pos_bottom="1%")
)

line.render()