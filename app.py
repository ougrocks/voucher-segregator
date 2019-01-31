import pandas as pd
from fpdf import FPDF

EXCEL_FILE = 'voucher.xlsx'

vouchers = pd.read_excel(EXCEL_FILE)
message = 'Your voucher code '

for i in range(0, len(vouchers)):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=message + vouchers.iloc[i][0], ln=1, align="C")
    pdf.output(vouchers.iloc[i][0] + ".pdf")
