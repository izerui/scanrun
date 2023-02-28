from model.BaseModel import BaseModel


class UploadedModel(BaseModel):

    def __init__(self, datas):
        _heads = [
            {"code": "unitCode", "title": "产品码"},
            {"code": "boxCode", "title": "箱码"},
            {"code": "palletCode", "title": "卡板码"},
            {"code": "chejianCode", "title": "车间Code", "hidden": True},
            {"code": "chejianName", "title": "车间"},
            {"code": "banzuCode", "title": "班组Code", "hidden": True},
            {"code": "banzuName", "title": "班组"},
            {"code": "businessKey", "title": "bk", "hidden": True},
            {"code": "createTime", "title": "扫码时间"},
            {"code": "creator", "title": "扫码人编号", "hidden": True},
            {"code": "creatorName", "title": "扫码人"},
            {"code": "uploadTime", "title": "上传时间"},
            {"code": "uploader", "title": "上传人Code", "hidden": True},
            {"code": "uploaderName", "title": "上传人"},
            {"code": "inventoryId", "title": "货品Id", "hidden": True},
            {"code": "inventoryCode", "title": "货品编码"},
            {"code": "inventoryName", "title": "货品Name"},
            {"code": "inventorySpec", "title": "货品规格"},
            {"code": "customerCode", "title": "客户编号", "hidden": True},
            {"code": "customerInventoryName", "title": "客户品名"},
            {"code": "customerInventorySpec", "title": "客户规格"},
            {"code": "customerMaterialCode", "title": "客户料号"},
            {"code": "saleOrderDocNo", "title": "销售订单号"},
            {"code": "customerOrderDocNo", "title": "客户订单号"},
            {"code": "customerName", "title": "客户名称"},
            {"code": "customerSerial", "title": "客户编码", "hidden": True},
            {"code": "employeeCode", "title": "业务员code", "hidden": True},
            {"code": "employeeName", "title": "业务员"},
            {"code": "operaCreator", "title": "扫码操作人", "hidden": True},
            {"code": "operaDate", "title": "作业日期", "hidden": True},
            {"code": "operaTime", "title": "作业时间", "hidden": True},
            {"code": "recordId", "title": "行号", "hidden": True},
            {"code": "taskCreateTime", "title": "任务创建时间"},
            {"code": "taskCreator", "title": "任务创建人编码"},
            {"code": "taskCreatorName", "title": "任务创建人"},
            {"code": "unitName", "title": "货品单位"}
        ]
        super().__init__(_heads, datas)
