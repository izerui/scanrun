from model.BaseModel import BaseModel


class TaskModel(BaseModel):

    def __init__(self, datas):
        _heads = [{'title': '业务主键', 'code': 'saleInventoryRecordId', 'hidden': True},
                  {'title': "销售单号", 'code': "saleOrderDocNo"},
                  {'title': "客户编码", 'code': "customerSerial"},
                  {'title': "客户名称", 'code': "customerName"},
                  {'title': "客户订单号", 'code': "customerOrderDocNo"},
                  {'title': "货品编码", 'code': "inventoryCode"},
                  {'title': "货品名称", 'code': "inventoryName"},
                  {'title': "规格型号", 'code': "inventorySpec"},
                  {'title': "任务数量", 'code': "taskQuantity"},
                  {'title': "已扫码数量", 'code': "scanCodeQuantity"},
                  {'title': "未扫码数量", 'code': "waitScanCodeQuantity"},
                  {'title': "装箱数量", 'code': "boxQuantity"},
                  {'title': "卡板数量", 'code': "palletQuantity"},
                  {'title': "单位", 'code': "unitName"},
                  {'title': "客户料号", 'code': "customerMaterialCode"},
                  {'title': "客户品名", 'code': "customerInventoryName"},
                  {'title': "客户型号", 'code': "customerInventorySpec"},
                  {'title': "业务员", 'code': "employeeName"},
                  {'title': "任务创建人", 'code': "creatorName"},
                  {'title': "任务创建日期", 'code': "createTime"},
                  {'title': "订单交期", 'code': "deliveryDate"},
                  {'title': "销售订单数量", 'code': "quantity"}
                  ]
        super().__init__(_heads, datas)
