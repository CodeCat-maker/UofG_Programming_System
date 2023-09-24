
class Report:
    report_id: str = ""
    status: bool = False
    type_report: int = 0
    time: str = ""

    def __int__(self, report_id, status, type_report, time):
        self.report_id = report_id
        self.status = status
        self.type_report = type_report
        self.time = time

    # Instance method to print all information about the report
    def info(self):
        print("Report ID: ", self.report_id, "\nStatus: ", self.status, "\nType of Report: ", self.type_report,
              "\nTime: ", self.time)
