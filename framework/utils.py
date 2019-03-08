import xlrd
from framework.logger import Logger

logger=Logger(logger="Utils").getLog()
class Utils(object):
    @classmethod
    def read_excel(cls,excelPath,sheetName='Sheet1'):
        workbook=xlrd.open_workbook(excelPath)
        sheet=workbook.sheet_by_name(sheetName)
        rowNum=sheet.nrows
        colNum=sheet.ncols
        keys = sheet.row_values(0)
        if rowNum<=1:
            logger.error("抱歉，总行数小于1")
        else:
            r=[]
            j=1
            for i in range(1,rowNum):
                sheet_data={}
                values=sheet.row_values(j)
                for j in range(colNum):
                    sheet_data[keys[j]]=values[j]
                r.append(sheet_data)
                j+=1
        return r


# if __name__=="__main__":
#     data_list=Utils.read_excel("E:/appium_UI_test_memo/data/data.xlsx","Sheet1")
#     print(data_list)




