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

