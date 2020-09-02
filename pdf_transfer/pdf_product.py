from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PyPDF2 import PdfFileWriter, PdfFileReader
import pyecharts.options as opts
from pyecharts.charts import Gauge

# 字体库添加中文字体
pdfmetrics.registerFont(TTFont('pingbold', 'PingBold.ttf'))
pdfmetrics.registerFont(TTFont('ping', 'ping.ttf'))
pdfmetrics.registerFont(TTFont('hv', 'Helvetica.ttf'))

class PDFGenerator:
    def __init__(self, filename, filepath):
        self.filename = filename
        self.file_path = filepath
        self.col_width = 40
        self.row_height = 8
        self.line = "______________________________________________"
        self.theme_color = colors.HexColor(0x308bcc)
        self.content_style = ParagraphStyle(name="ContentStyle", fontName="ping", fontSize=12, leading=25, spaceAfter=20,
                                            underlineWidth=1, alignment=TA_LEFT, )
        self.content2_style = ParagraphStyle(name="ContentStyle", fontName="ping", fontSize=12, leading=20, spaceAfter=20,
                                            underlineWidth=1, alignment=TA_LEFT, )
        self.normal_style = ParagraphStyle(name="NormalStyle", fontName="ping", fontSize=12, leading=25, spaceAfter=20,
                                            underlineWidth=1, alignment=TA_CENTER, )
        self.tabletext_style = ParagraphStyle(name="TabletextStyle", fontName="ping", fontSize=12, leading=18, spaceAfter=20,
                                            underlineWidth=1, alignment=TA_LEFT, )
        self.table_title_style = ParagraphStyle(name="TableTitleStyle", fontName="pingbold", fontSize=20, leading=25,
                                                textColor=self.theme_color, spaceAfter=10, alignment=TA_LEFT, )
        self.title_style = ParagraphStyle(name="TitleStyle", fontName="pingbold", fontSize=40, leading=25,
                                                textColor=self.theme_color, spaceAfter=10, alignment=TA_CENTER, )
        # 附加样式
        self.side_style = ParagraphStyle(name="SideStyle", fontName="ping", fontSize=12, leading=20, spaceAfter=20,
                                         underlineWidth=1, alignment=TA_LEFT)

        self.table_style = TableStyle([('FONTNAME', (0, 0), (-1, -1), 'ping'),
                                      ('FONTSIZE', (0, 0), (-1, -1), 12),
                                      ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                      ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                      ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                                      ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                     ])
        self.table2_style = TableStyle([('FONTNAME', (0, 0), (-1, -1), 'ping'),
                                      ('FONTSIZE', (0, 0), (-1, -1), 12),
                                      ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                      ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                      ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                                      ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                      ('SPAN', (0, 0), (0, -1))
                                     ])
        self.report1_style = TableStyle([('FONTNAME', (0, 0), (-1, -1), 'ping'),
                                      ('FONTSIZE', (0, 0), (-1, -1), 12),
                                      ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                                      ('ALIGN',(0, 0),(-1, 0),'CENTER'),
                                      ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                      ('VALIGN', (0, 2), (-1, 2), 'TOP'),
                                      ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                                      ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                      ('BACKGROUND', (0, 0), (-1, 0), self.theme_color),
                                      ('SPAN', (0, 0), (-1, 0)),
                                      ('SPAN', (0, 2), (-1, 2)),
                                      ])
        self.report2_style = TableStyle([('FONTNAME', (0, 0), (-1, -1), 'ping'),
                                      ('FONTSIZE', (0, 0), (-1, -1), 12),
                                      ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                                      ('ALIGN',(0, 0),(-1, 0),'CENTER'),
                                      ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                      ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                                      ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                      ('BACKGROUND', (0, 0), (-1, 0), self.theme_color),
                                      ('SPAN', (0, 0), (-1, 0)),
                                      ])
        self.report3_style = TableStyle([('FONTNAME', (0, 0), (-1, -1), 'ping'),
                                      ('FONTSIZE', (0, 0), (-1, -1), 12),
                                      ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                                      ('ALIGN',(0, 0),(-1, 0),'CENTER'),
                                      ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                      ('VALIGN', (0, 4), (-1, 4), 'TOP'),
                                      ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                                      ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                      ('BACKGROUND', (0, 0), (-1, 0), self.theme_color),
                                      ('SPAN', (0, 0), (-1, 0)),
                                      ('SPAN', (0, 4), (-1, 4)),
                                      ])
        self.report4_style = TableStyle([('FONTNAME', (0, 0), (-1, -1), 'ping'),
                                      ('FONTSIZE', (0, 0), (-1, -1), 12),
                                      ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                                      ('ALIGN',(0, 0),(-1, 0),'CENTER'),
                                      ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                      ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                                      ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                      ('BACKGROUND', (0, 0), (-1, 0), self.theme_color),
                                      ])

    def generatePDF(self, report, tables, result_report=None):
        # 生成表格
        story = []

        # 生成封面相关信息，其中静态图请替换为本机路径
        story.append(Spacer(1, 20 * mm))
        img = Image("C:\\Users\\User\\Desktop\\fuying\\fuying\\pdf_transfer\\logo.png")
        img.drawWidth = 100 * mm
        img.drawHeight = 100 * mm
        story.append(img)
        story.append(Spacer(1, 20 * mm))
        story.append(Paragraph("蛋白质组学生理刻画检测报告",self.title_style))
        story.append(Spacer(1, 20 * mm))
        story.append(Paragraph("检测编号："+report['test_num']+"\a\a\a"+"报告日期"+report['report_date'],self.normal_style))
        story.append(PageBreak())

        story.append(Spacer(1,5*mm))
        story.append(Paragraph("致受检者书", self.table_title_style))
        story.append(Spacer(1, 10 * mm))
        sex = "女士"
        if(report['sex'] == "男"):
            sex = "先生"
        story.append(Paragraph("尊敬的"+report['name']+sex,self.content_style))
        story.append(Paragraph("您好！", self.content_style))
        story.append(Paragraph("\a\a复瑛健康（上海复瑛生物科技有限公司）是生命健康领域的新兴企业，坚持自主创新和成果转化，立足新一代蛋白质组技术，基于数据驱动、健康评估的检测服务公司，旨在将生命科学、临床医学及数据挖掘等创新技术融为一体，推出全新的健康评估模式服务于人类健康。",self.content2_style))
        story.append(Paragraph("\a\a蛋白质组学生理刻画产品是利用次世代蛋白质组技术配合机器学习的大数据精准分型，1滴指尖血为样本可获得2000+蛋白质检测指标，涵盖100+项生理功能，完成40+大类的生理刻画，检测数据量为常规体检的近百倍，提供更加完备的个人全景生理刻画。",self.content2_style))
        story.append(Paragraph("\a\a在此我们也特别提醒您注意：受检者委托复瑛健康开展蛋白质组学生理刻画检测服务，系基于受检者生理功能相关评估结果，预测无明显症状的受检者是否存在生理状态不佳的情况，该检测不是一种诊断过程，而是一种简便快速的评估方法，以便提高客户的生活质量。检测结果不作为临床诊断和治疗的依据。",self.content2_style))
        story.append(Paragraph("\a\a本检测的意义在于通过较完备的个人全景式生理刻画，助您掌握健康状态，希望您对此给予充分的理解与信任，我们愿意与您一同积极面对可能出现的结果。由于技术发展的局限性，个体间存在的生物学差异等原因，本报告仅对本次送检样本负责。",self.content2_style))
        story.append(Paragraph("\a\a希望您能将您的宝贵意见与建议及时反馈给我们。我们免费的服务电话是********（工作日，8:30-17:30），我们将竭诚为您服务！祝您健康！", self.content2_style))
        story.append(Paragraph("\a\a此致",self.content2_style))
        story.append(Paragraph("敬礼",self.content2_style))
        story.append(Paragraph("上海复瑛生物科技有限公司", self.content2_style))
        story.append(PageBreak())

        story.append(Spacer(1,5*mm))
        story.append(Paragraph("产品简介",self.table_title_style))
        story.append(Spacer(1, 10 * mm))
        story.append(Paragraph("\a\a蛋白质作为生命活动的执行者，直接反映着一个个体的生理、病理情况。随着人类基因组计划的实施和推进，生命科学研究已进入了后基因组时代。蛋白质组研究是后基因组时代生命科学研究的核心内容之一。蛋白质组学以细胞内全部蛋白质及其活动方式为研究对象。在早期诊断、疾病预防、分型、判断预后等诸多方面都具有巨大的潜力。",self.content_style))
        story.append(Paragraph("\a\a现阶段，本检测平台总原始数据量达到1G；谱图数达到10万张，肽段数达到5.000个以上，检测体液样本的蛋白质鉴定数可达2,000种以上。",self.content_style))
        story.append(Paragraph("\a\a根据上万组正常人蛋白质组数据，建立基准数据训练集。通过机器学习将蛋白质组数据同临床表型进行管理关联，建立包含一百种特征的训练模型。将用户样本进行蛋白质组分析后与训练集比对，可对样本进行分类或分型，并据此提供较为可靠的临床辅助结论。",self.content_style))
        story.append(PageBreak())

        # 这里的图片路径使用时请修改！
        story.append(Spacer(1, 5*mm))
        story.append(Paragraph("技术路线",self.table_title_style))
        story.append(Spacer(1, 5*mm))
        img = Image("C:\\Users\\User\\Desktop\\fuying\\fuying\\pdf_transfer\\rout.png")
        img.drawHeight = 70 * mm
        img.drawWidth = 160 * mm
        story.append(img)
        story.append(Spacer(1, 10*mm))
        story.append(Paragraph("技术原理",self.table_title_style))
        story.append(Spacer(1, 5*mm))
        img = Image("C:\\Users\\User\\Desktop\\fuying\\fuying\\pdf_transfer\\principle.png")
        img.drawHeight = 80 * mm
        img.drawWidth = 160 * mm
        story.append(img)
        story.append(PageBreak())

        # 生成用户信息表
        r1_table = [['用户信息'],
                    ['姓名',report['name'],'性别',report['sex'],'年龄',report['age']],
                    [Paragraph(report['health_history'],self.tabletext_style)],]
        r2_table = [['样本信息'],
                    ['送样日期',report['sample_date'],'样本编号',report['sample_num']],
                    ['样品来源',report['resource'],'样品类型','type']]
        r3_table = [['检测信息'],
                    ['检测项目',report['subject']],
                    ['检测编号',report['test_num']],
                    ['检测方法',report['method']],
                    [Paragraph(report['explanation'],self.tabletext_style)]]
        r4_table = [['细化检测结果'],
                    ["一、实验室检测质控"]]

        story.append(Table(r1_table,colWidths=[18 * mm, 35 * mm, 18 * mm, 35 * mm, 18 * mm, 36 * mm],
                           rowHeights = [self.row_height * mm, self.row_height * mm, 25 * mm], style=self.report1_style))
        story.append(Table(r2_table, colWidths=[25 * mm, 55 * mm, 25 * mm, 55 * mm],
                           rowHeights=self.row_height * mm, style=self.report2_style))
        story.append(Table(r3_table, colWidths=[25 * mm, 135 * mm],
                           rowHeights=[self.row_height * mm, self.row_height * mm, self.row_height * mm, self.row_height * mm, 30 * mm], style=self.report3_style))
        story.append(Table(r4_table, colWidths=[160 * mm],
                           rowHeights= self.row_height * mm, style=self.report4_style))

        for set in report["quality_report"]:
            set['table'][0].insert(0,set['name'])
            set['table'][1].insert(0,set['name'])
            for i in range(2):
                for j in range(set['table'][i].__len__()):
                    set['table'][i][j] = Paragraph(set['table'][i][j],self.tabletext_style)
            table = Table(set['table'],colWidths=(160/set['table'][0].__len__()) * mm,
                          rowHeights = 15 * mm, style = self.table2_style)
            story.append(table)
        story.append(PageBreak())

        story.append(Paragraph("二、质谱结果",self.tabletext_style))
        img = Image(report['mass_spectrogram_img'])
        img.drawHeight = 80 * mm
        img.drawWidth = 160 * mm
        story.append(img)
        story.append(Spacer(1, 4 * mm))
        story.append(Paragraph(report["ms_text"],self.content_style))
        story.append(PageBreak())


        story.append(Paragraph("三、生理刻画结果", self.tabletext_style))
        for set in tables:

            # 生成指标总表
            story.append(Paragraph(set['name'],self.table_title_style))
            story.append(Table(set['sum_table'],colWidths=[20 * mm, 60 * mm, 40 * mm, 40 * mm],
                               rowHeights = self.row_height *mm, style=self.table_style))
            story.append(PageBreak())

            # 生成图表pdf
            i = 0
            for i in range(set['img_table'].__len__()):
                img_table = set['img_table'][i]
                img = Image(img_table['img_path'])
                img.drawHeight = 60 * mm
                img.drawWidth = 100 * mm
                story.append(Paragraph(img_table['title'], self.table_title_style))
                story.append(Spacer(1, 4 * mm))
                story.append(img)
                story.append(Spacer(1, 10 * mm))
                story.append(Paragraph(img_table['description'],self.content_style))
                if i % 2 == 1:
                    story.append(PageBreak())
                else:
                    story.append(Paragraph(self.line, self.table_title_style))
                    story.append(Spacer(1, 4 * mm))
            if i % 2 == 0:
                story.append(PageBreak())

        # 结果说明
        if result_report != None:
            story.append(Spacer(1, 5*mm))
            story.append(Paragraph("结果说明",self.table_title_style))
            story.append(Spacer(1, 10 * mm))
            for str in result_report['result']:
                story.append(Paragraph(str,self.content_style))
            story.append(Spacer(1,10 * mm))
            story.append(Paragraph("1.本次检测结果只对本次送检样本负责，结果仅供参考，不作为临床诊断依据",self.content2_style))
            story.append(Paragraph("2.如果对检测结果有异议，请在收到报告后七日内与我们联系。",self.content2_style))
            story.append(Spacer(1, 10 * mm))
            story.append(Paragraph("检测员：\a\a" + result_report["test_member"] +
                                   "\a\a复核者：\a\a" + result_report["check_member"] +
                                   "\a\a报告日期：\a\a" + result_report["report_date"],
                                   self.content2_style))
            story.append(PageBreak())

            # 预测分数
            img = Image(result_report["score_img"], kind="absolute", hAlign="CENTER")
            img.drawHeight = 90 * mm
            img.drawWidth = 100 * mm
            img.vAlign = "TOP"
            story.append(Spacer(1, 5*mm))
            story.append(Paragraph("了解预测分数", self.table_title_style))
            story.append(Spacer(1, 4*mm))
            story.append(img)
            story.append(Spacer(1, 8*mm))
            story.append(Paragraph("健康评分主要是根据个人蛋白质组表达水平与万人队列相匹配，并根据"
                                   "相关生理指数高低与健康状态相关联，通过计算显示整体健康评分。", self.side_style))
            story.append(Paragraph("基础分：500 分；健康情况正常：1 分；健康情况极差：-3 分；健康情况较差："
                                   "-1 分；健康情况良好：1 分；健康情况优秀：3 分。",self.side_style))
            story.append(Paragraph("您的将康档案记录评估健康 " + result_report["sum_num"] + "次；评估异常" + result_report["error_num"] + "次", self.side_style))
            story.append(PageBreak())

            # 功能报告
            for set in result_report["score_report"]:
                type = set['type']
                table = set['table']
                for row in table:
                    row.insert(0,type)
                for i in range(table.__len__()):
                    for j in range(table[i].__len__()):
                        table[i][j] = Paragraph(table[i][j], self.tabletext_style)
                table = Table(table, colWidths=[10*mm,40*mm,20*mm,80*mm],
                              rowHeights=40 * mm, style=self.table2_style)
                story.append(table)
            story.append(PageBreak())

        # 生成pdf
        doc = SimpleDocTemplate(self.file_path + self.filename + ".pdf",
                                leftMargin=20 * mm, rightMargin=20 * mm, topMargin=20 * mm, bottomMargin=20 * mm,
                                showBoundary=1 * mm)
        doc.build(story)

    def MergePDF(self, pdf_array, outfile):

        output = PdfFileWriter()
        outputPages = 0

        if pdf_array:
            for pdf_file in pdf_array:
                print("%s" % pdf_file)

                # 读取源PDF文件
                input = PdfFileReader(open(pdf_file, "rb"))

                # 获得源PDF文件中页面总数
                pageCount = input.getNumPages()
                outputPages += pageCount
                print("页数：%d" % pageCount)

                # 分别将page添加到输出output中
                for iPage in range(pageCount):
                    output.addPage(input.getPage(iPage))

            print("合并后的总页数:%d." % outputPages)
            # 写入到目标PDF文件
            outputStream = open(outfile, "wb")
            output.write(outputStream)
            outputStream.close()
            print("PDF文件合并完成！")

        else:
            print("没有可以合并的PDF文件！")

# 传入分数 **/1000
def generateDashBoard(num):
    Gauge_1 = (Gauge(init_opts=opts.InitOpts(width="800px",height="400px"))
        .add(series_name="个人健康得分",data_pair=[["",num]],max_=1000,
             detail_label_opts=opts.TooltipOpts(is_show=True,formatter="{value}分"),
             axisline_opts=opts.AxisLineOpts(
                 linestyle_opts=opts.LineStyleOpts(
                     color=[(0.3, "#fd666d"), (0.7, "#37a2da"), (1, "#1fa34a")], width=30)))
        .set_global_opts(title_opts=opts.TitleOpts(title="个人健康得分",pos_left="center"),
                         legend_opts=opts.LegendOpts(is_show=False),)
        # 更换图片地址
        .render("C:\\Users\\User\\Desktop\\fuying\\fuying\\pdf_transfer\\gauge.html"))

if __name__ == '__main__':
    report_pdfg = PDFGenerator("report","C:\\Users\\User\\Desktop\\fuying\\fuying\\pdf_transfer\\")
    report = {
        "name": "陈周",
        "sex": "男",
        "age": "32",
        "health_history": "病史或临床表现：（用户填写）",
        "report_date": "2020/07/29",
        "sample_date": "2020/07/29",
        "sample_num": "abc1234",
        "resource": "委托送检",
        "type": "手指血",
        "subject": "全套餐",
        "test_num": "Exp079824",
        "method": "次世代非数据依赖采集蛋白质组检测技术",
        "explanation": "（结果解读）本次检测结果，您的内脏脂肪、总胆固醇、少数代谢功能指数以及个别免疫功能指数存在明显异常，建议您在日常生活中注意健康饮食结构，适当进行运动，预防疾病的发生。若有不适请及时就医",
        "quality_report": [
            {"name": "血液样本",
            "table": [['全血总量（μL）','血浆总量（μL）','血浆颜色','是否合格','操作平台','质控标准'],
                      ['30','10','淡黄色','是','Thermo','血浆总量>5μL']]},
            {"name":"蛋白提取",
            "table": [['血浆上样量（μL）','蛋白质量（μg）','高丰度去除','是否合格','操作平台','质控标准'],
                      ['2','100','是','是','Thermo','蛋白质量>30μg']]},
            {"name": "蛋白提取",
            "table": [['血浆上样量（μL）', '蛋白质量（μg）', '高丰度去除', '是否合格', '操作平台', '质控标准'],
                      ['2', '100', '是', '是', 'Thermo', '蛋白质量>30μg']]},
            ],
        "mass_spectrogram_img": "C:\\Users\\User\\Desktop\\fuying\\fuying\\pdf_transfer\\079824\\mass_spectrogram_img.png",
        "ms_text": "数据采集量1.5 G，谱图数81,220张，蛋白质鉴定总数2408。",

    }
    tables = [
        {"name": "基础套餐评估结果1",
        "sum_table": [['序号','项目名称','您的预测评分','健康状态'],
                      ['1.1','生理年龄评价','-3','较差'],
                      ['1.2','肥胖评价','-2','正常'],
                      ['1.3','肝功能','11','良好']],
        "img_table": [{"title":"1.1.1 生理年龄指数","img_path":"C:\\Users\\User\\Desktop\\fuying\\fuying\\pdf_transfer\\079824\\1.1.1.png",
                       "description":"您的生理年龄指数预测结果为36.60,极高于您的口述年龄，您比同龄人整体更操劳，需注意日常保养，适当锻炼。"},
                      {"title":"1.2.1 内脏脂肪率指数","img_path":"C:\\Users\\User\\Desktop\\fuying\\fuying\\pdf_transfer\\079824\\1.2.1.png",
                       "description":"您的内脏脂肪率指数在万人队列中的位比为92.79%，处在极高位区，表示您的内脏脂肪率指数水平高于92.79%的人群，需注意日常生活及饮食情况，根据自身需求进行相应调整。若感不适请及时就医。"},
                      {"title": "1.2.1 内脏脂肪率指数","img_path": "C:\\Users\\User\\Desktop\\fuying\\fuying\\pdf_transfer\\079824\\1.2.1.png",
                       "description": "您的内脏脂肪率指数在万人队列中的位比为92.79%，处在极高位区，表示您的内脏脂肪率指数水平高于92.79%的人群，需注意日常生活及饮食情况，根据自身需求进行相应调整。若感不适请及时就医。"}],},
        {"name": "基础套餐评估结果2",
         "sum_table": [['序号', '项目名称', '您的预测评分', '健康状态'],
                       ['1.1', '生理年龄评价', '-3', '较差'],
                       ['1.2', '肥胖评价', '-2', '正常'],
                       ['1.3', '肝功能', '11', '良好']],
         "img_table": [{"title": "1.1.1 生理年龄指数","img_path": "C:\\Users\\User\\Desktop\\fuying\\fuying\\pdf_transfer\\079824\\1.1.1.png",
                        "description": "您的生理年龄指数预测结果为36.60,极高于您的口述年龄，您比同龄人整体更操劳，需注意日常保养，适当锻炼。"},
                       {"title": "1.2.1 内脏脂肪率指数","img_path": "C:\\Users\\User\\Desktop\\fuying\\fuying\\pdf_transfer\\079824\\1.2.1.png",
                        "description": "您的内脏脂肪率指数在万人队列中的位比为92.79%，处在极高位区，表示您的内脏脂肪率指数水平高于92.79%的人群，需注意日常生活及饮食情况，根据自身需求进行相应调整。若感不适请及时就医。"}], },
    ]
    result_report = {
        # 添加属性
        "sum_num" : "1",
        "error_num" : "0",
        "score_img" : "C:\\Users\\User\\Desktop\\fuying\\fuying\\pdf_transfer\\score.png",
        "score_report" : [{"type":"基础评价",
                           "table" : [["甘油三酯指数","偏高","均衡饮食、避免过度疲劳、戒烟戒酒，定期体检监测内分泌系统功能、心脑血管情况"],
                                      ["载脂蛋白指数","偏低","清淡饮食、减少淀粉、糖类、油脂摄入，避免过度疲劳、戒烟戒酒，根据自身情况合理制定运动计划，适当增加日常运动量，定期体检监测内分系统功能、心脑血管情况"],
                                      ["总胆固醇指数","偏低","合理安排作息、均衡饮食、避免过度疲劳、戒烟戒酒，定期体检监测肝功能、内分泌系统情况"]],},
                          {"type": "代谢功能评价",
                           "table": [["L-丝氨酸合成指数", "偏高", "均衡饮食、避免过度疲劳、戒烟戒酒，定期体检监测内分泌系统功能、心脑血管情况"],
                                     ["L-苏氨酸降解指数", "偏低",
                                      "清淡饮食、减少淀粉、糖类、油脂摄入，避免过度疲劳、戒烟戒酒，根据自身情况合理制定运动计划，适当增加日常运动量，定期体检监测内分系统功能、心脑血管情况"]],},
                           {"type": "免疫功能评价",
                            "table": [["中枢 CD4+ T 细胞指数", "偏高", "定期体检排除病毒、细菌感染、自身免疫性疾病可能，均衡饮食、避免暴饮暴食、避免过度疲劳、戒烟戒酒，并根据自身条件合理制定运动计划，循序渐进锻炼身体"],
                                      ["总CD8+T 细胞指数", "偏高",
                                       "定期体检排除病毒、细菌感染、自身免疫性疾病可能，均衡饮食、避免暴饮暴食、避免过度疲劳、戒烟戒酒，并根据自身条件合理制定运动计划，循序渐进锻炼身体"]],},
                           {"type":"many评价",
                            "table":[
                [
                    'Th2细胞指数', '偏高',
                    '定期体检排除感染、自身免疫疾病可能，均衡饮食、避免暴饮暴食、避免过度疲劳、戒烟戒酒，并根据自身条件合理制定运动计划，循序渐进锻炼身体'
                ],
                [
                    '嗜碱性粒细胞指数', '偏高',
                    '定期体检排除感染、自身免疫疾病可能，均衡饮食、避免暴饮暴食、避免过度疲劳、戒烟戒酒，并根据自身条件合理制定运动计划，循序渐进锻炼身体'
                ],
                [
                    '微环境指数', '偏高',
                    '定期体检排除感染、自身免疫疾病可能，均衡饮食、避免暴饮暴食、避免过度疲劳、戒烟戒酒，并根据自身条件合理制定运动计划，循序渐进锻炼身体'
                ],
                [
                    '总基质指数', '偏高',
                    '定期体检排除感染、自身免疫疾病可能，均衡饮食、避免暴饮暴食、避免过度疲劳、戒烟戒酒，并根据自身条件合理制定运动计划，循序渐进锻炼身体'
                ],
                [
                    '幼稚性CD8+T细胞指数', '偏低',
                    '定期体检排除免疫缺陷病可能，均衡饮食、保证适量肉蛋奶摄入、避免过度疲劳，并根据自身条件合理制定运动计划，循序渐进锻炼身体'
                ],
                [
                    '肥大细胞指数', '偏低',
                    '定期体检排除免疫缺陷病可能，均衡饮食、保证适量肉蛋奶摄入、避免过度疲劳，并根据自身条件合理制定运动计划，循序渐进锻炼身体'
                ],
            ],}],

        "result": ["(1)免疫系统评价中，中枢CD4+T细胞指数，效应性CD4+T细胞指数，记忆性CD4+T细胞指数，M1型巨噬细胞指数，γδT细胞指数，单核细胞指数，共6项生理指数明显异常于人群队列，且对健康状态有明显负面影响，机体出现部分免疫效应的概率较大。建议您注意日常生活及饮食情况，适当运动，适当补充营养物质，以提高机体免疫力，预防疾病的发生，若生活中有感不适请及时就医。",
                   "(2)代谢功能评价中，嘌呤指数，生酮指数，共2项生理指数明显异常于人群队列，且对健康状态有明显负面影响，机体有一定概率出现痛风、低血糖、或糖原贮存不足等情况，日积月累容易导致健康问题，建议您注意日常生活及饮食情况，适当运动，若生活中有感不适请及时就医。",
                   "(3)基础评价中，生理年龄，内脏脂肪率指数，尿素指数，甘油三酯指数，总胆固醇指数，共5项生理指数明显异常于人群队列，且对健康状态有明显负面影响。建议您生活中保持精神愉悦，少食多餐，粗细粮搭配，适当使用含植物纤维的食物，使用保护心脑血管的食物，并适当运动。",
                   "健康是动态的，生理指标也随之变化，复瑛健康建议您每半年进行一次蛋白质组学生理刻画，建立个人专属健康档案，有助于提早发现异常状态，预防疾病的发生。上医治未病，中医治己病，下医治大病。复瑛健康助您改善“未病之症”。"],
        "test_member": "a",
        "check_member": "b",
        "report_date": report['report_date']
    }
    report_pdfg.generatePDF(report,tables,result_report)
    pdf1 = "C:\\Users\\User\\Desktop\\fuying\\fuying\\pdf_transfer\\report.pdf"
    pdf2 = "C:\\Users\\User\\Desktop\\fuying\\fuying\\pdf_transfer\\template_ending.pdf"
    report_pdfg.MergePDF([pdf1,pdf2],"C:\\Users\\User\\Desktop\\fuying\\fuying\\pdf_transfer\\report_res.pdf")
