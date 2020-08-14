from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
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
        self.theme_color = colors.HexColor(0x308bcc)
        self.content_style = ParagraphStyle(name="ContentStyle", fontName="ping", fontSize=12, leading=25, spaceAfter=20,
                                            underlineWidth=1, alignment=TA_LEFT, )
        self.table_title_style = ParagraphStyle(name="TableTitleStyle", fontName="pingbold", fontSize=20, leading=25,
                                                textColor=self.theme_color, spaceAfter=10, alignment=TA_LEFT, )
        self.table_style = TableStyle([('FONTNAME', (0, 0), (-1, -1), 'ping'),
                                      ('FONTSIZE', (0, 0), (-1, -1), 12),
                                      ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                      ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                      ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                                      ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                     ])

    def generatePDF(self, tables):
        # 生成表格
        story = []

        for set in tables:
            # 生成指标总表
            story.append(Paragraph(set['name'],self.table_title_style))
            story.append(Table(set['sum_table'],colWidths=[self.col_width *mm,self.col_width *mm,self.col_width *mm,self.col_width *mm],
                               rowHeights = self.row_height *mm, style=self.table_style))
            story.append(PageBreak())

            # 生成图表pdf
            i = 0
            for i in range(set['img_table'].__len__()):
                img_table = set['img_table'][i]
                story.append(Paragraph(img_table['title'], self.table_title_style))
                img = Image(img_table['img_path'])
                img.drawHeight = 60 * mm
                img.drawWidth = 100 * mm
                story.append(img)
                story.append(Paragraph(img_table['description'],self.content_style))
                if i % 2 == 1:
                    story.append(PageBreak())
            if i % 2 == 0:
                story.append(PageBreak())

        # 生成pdf
        doc = SimpleDocTemplate(self.file_path + self.filename + ".pdf",
                                leftMargin=20 * mm, rightMargin=20 * mm, topMargin=20 * mm, bottomMargin=20 * mm)
        doc.build(story)



if __name__ == '__main__':
    report_pdfg = PDFGenerator("report","C:\\Users\\User\\Desktop\\fuying\\fuying\\pdf_transfer\\")
    tables = [
        {"name": "基础套餐评估结果",
        "sum_table": [['序号','项目名称','您的预测评分','健康状态'],
                      ['1.1','生理年龄评价','-3','较差'],
                      ['1.2','肥胖评价','-2','正常'],
                      ['1.3','肝功能','11','良好']],
        "img_table": [{"title":"1.1.1 生理年龄指数","img_path":"C:\\Users\\User\\Desktop\\fuying\\fuying\\pdf_transfer\\079824\\1.1.1.png",
                       "description":"您的生理年龄指数预测结果为36.60,极高于您的口述年龄，您比同龄人整体更操劳，需注意日常保养，适当锻炼。"},
                      {"title":"1.2.1 内脏脂肪率指数","img_path":"C:\\Users\\User\\Desktop\\fuying\\fuying\\pdf_transfer\\079824\\1.2.1.png",
                       "description":"您的内脏脂肪率指数在万人队列中的位比为92.79%，处在极高位区，表示您的内脏脂肪率指数水平高于92.79%的人群，需注意日常生活及饮食情况，根据自身需求进行相应调整。若感不适请及时就医。"},
                      {"title": "1.2.1 内脏脂肪率指数",
                       "img_path": "C:\\Users\\User\\Desktop\\fuying\\fuying\\pdf_transfer\\079824\\1.2.1.png",
                       "description": "您的内脏脂肪率指数在万人队列中的位比为92.79%，处在极高位区，表示您的内脏脂肪率指数水平高于92.79%的人群，需注意日常生活及饮食情况，根据自身需求进行相应调整。若感不适请及时就医。"}],},
        {"name": "基础套餐评估结果",
         "sum_table": [['序号', '项目名称', '您的预测评分', '健康状态'],
                       ['1.1', '生理年龄评价', '-3', '较差'],
                       ['1.2', '肥胖评价', '-2', '正常'],
                       ['1.3', '肝功能', '11', '良好']],
         "img_table": [{"title": "1.1.1 生理年龄指数",
                        "img_path": "C:\\Users\\User\\Desktop\\fuying\\fuying\\pdf_transfer\\079824\\1.1.1.png",
                        "description": "您的生理年龄指数预测结果为36.60,极高于您的口述年龄，您比同龄人整体更操劳，需注意日常保养，适当锻炼。"},
                       {"title": "1.2.1 内脏脂肪率指数",
                        "img_path": "C:\\Users\\User\\Desktop\\fuying\\fuying\\pdf_transfer\\079824\\1.2.1.png",
                        "description": "您的内脏脂肪率指数在万人队列中的位比为92.79%，处在极高位区，表示您的内脏脂肪率指数水平高于92.79%的人群，需注意日常生活及饮食情况，根据自身需求进行相应调整。若感不适请及时就医。"}], },
    ]
    report_pdfg.generatePDF(tables)

