#G1
class Report:
    def get_summary(self):
        return "general summary report"

#G2, G3
class SalesReport(Report):
    def get_summary(self):
        return "sales summary report of " + super().get_summary()

#G4
sales_report = SalesReport()
print(sales_report.get_summary())