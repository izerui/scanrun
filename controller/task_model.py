from PySide6.QtGui import QStandardItemModel, QStandardItem


class TaskModel(QStandardItemModel):
    heads = [{
        'title': "销售单号",
        'code': "saleOrderDocNo",
        'ellipsis': True,
        'width': 120,
        'sorter': True,
    },
        {
            'title': "客户编码",
            'code': "customerSerial",
            'ellipsis': True,
            'width': 120,
        },
        {
            'title': "客户名称",
            'code': "customerName",
            'ellipsis': True,
            'width': 120,
        },
        {
            'title': "客户订单号",
            'code': "customerOrderDocNo",
            'ellipsis': True,
            'width': 120,
        },
        {
            'title': "货品编码",
            'code': "inventoryCode",
            'ellipsis': True,
            'width': 120,
            'sorter': True,
        },
        {
            'title': "货品名称",
            'code': "inventoryName",
            'ellipsis': True,
            'width': 120,
        },
        {
            'title': "规格型号",
            'code': "inventorySpec",
            'ellipsis': True,
            'width': 120,
        },
        {
            'title': "单位",
            'code': "unitName",
            'ellipsis': True,
            'width': 120,
        },
        {
            'title': "客户料号",
            'code': "customerMaterialCode",
            'ellipsis': True,
            'width': 120,
        },
        {
            'title': "客户品名",
            'code': "customerInventoryName",
            'ellipsis': True,
            'width': 120,
        },
        {
            'title': "客户型号",
            'code': "customerInventorySpec",
            'ellipsis': True,
            'width': 120,
        },
        {
            'title': "业务员",
            'code': "employeeName",
            'ellipsis': True,
            'width': 120,
        },
        {
            'title': "任务创建人",
            'code': "creatorName",
            'ellipsis': True,
            'width': 120,
        },
        {
            'title': "任务创建日期",
            'code': "createTime",
            'ellipsis': True,
            'width': 120,
            'sorter': True,
        },
        {
            'title': "订单交期",
            'code': "deliveryDate",
            'ellipsis': True,
            'sorter': True,
            'width': 120,
        },
        {
            'title': "销售订单数量",
            'code': "quantity",
            'ellipsis': True,
            'width': 120,
            'align': "right",
        },
        {
            'title': "任务数量",
            'code': "taskQuantity",
            'ellipsis': True,
            'width': 120,
            'align': "right",
        },
        {
            'title': "已扫码数量",
            'code': "scanCodeQuantity",
            'ellipsis': True,
            'width': 120,
            'align': "right",
        },
        {
            'title': "未扫码数量",
            'code': "waitScanCodeQuantity",
            'ellipsis': True,
            'width': 120,
            'align': "right"
        },
        {
            'title': "装箱数量",
            'code': "boxQuantity",
            'ellipsis': True,
            'width': 120,
            'align': "right",
        },
        {
            'title': "卡板数量",
            'code': "palletQuantity",
            'ellipsis': True,
            'width': 120,
            'align': "right",
        }
    ]

    def __init__(self, tableView):
        super().__init__()
        self.tableView = tableView
        self.renderHeads()


    def renderHeads(self):
        head_labels = []
        for head in TaskModel.heads:
            head_labels.append(head['title'])
        self.setHorizontalHeaderLabels(head_labels)

    def addRowData(self, row):
        columns = []
        for i, head in enumerate(TaskModel.heads):
            columns.append(QStandardItem(row[head['code']]))
        self.appendRow(columns)

    def setRowDatas(self, rows):
        self.rows = rows
        self.clear()
        self.renderHeads()
        for row in rows:
            self.addRowData(row)

    def currentSelectedRow(self):
        rowIndex = self.tableView.currentIndex().row()
        return self.rows[rowIndex]
