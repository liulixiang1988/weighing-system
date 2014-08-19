# -*- coding:utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
# * Rearrange models' order
# * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class VNewid(models.Model):
    s = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'V_newid'


class ServiceLog(models.Model):
    command_id = models.CharField(db_column='CommandId', max_length=30, blank=True)  # Field name made lowercase.
    return_command_id = models.CharField(db_column='ReturnCommandId', max_length=60,
                                         blank=True)  # Field name made lowercase.
    op_table = models.CharField(db_column='OpTable', max_length=50, blank=True)  # Field name made lowercase.
    op_command = models.CharField(db_column='OpCommand', max_length=50, blank=True)  # Field name made lowercase.
    op_result = models.IntegerField(db_column='OpResult', blank=True, null=True)  # Field name made lowercase.
    op_time = models.DateTimeField(db_column='OpTime', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    op_type = models.IntegerField(db_column='OpType', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Beizhu', max_length=2000, blank=True)  # Field name made lowercase.
    records = models.IntegerField(db_column='Records', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_WeighHouseService_Log'


class Batch(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    batch_code = models.CharField(db_column='BatchCode', max_length=50, blank=True)  # Field name made lowercase.
    batch_number = models.CharField(db_column='BatchNumber', max_length=50, blank=True)  # Field name made lowercase.
    batch_name = models.CharField(db_column='BatchName', max_length=50, blank=True)  # Field name made lowercase.
    weigh_house_codes = models.CharField(db_column='WeighHouseCodes', max_length=200,
                                         blank=True)  # Field name made lowercase.
    status = models.NullBooleanField(db_column='Status')  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    upload_bit = models.IntegerField(db_column='UploadBit', blank=True, null=True)  # Field name made lowercase.
    upload_time = models.DateTimeField(db_column='UploadTime', blank=True, null=True)  # Field name made lowercase.
    create_user_code = models.CharField(db_column='CreateUserCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CreateUserName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    last_modified_user_code = models.CharField(db_column='LastModifiedUserCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    last_modified_username = models.CharField(db_column='LastModifiedUserName', max_length=50,
                                              blank=True)  # Field name made lowercase.
    last_modified_time = models.DateTimeField(db_column='LastModifiedTime', blank=True,
                                              null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.
    attribute1 = models.CharField(db_column='Attribute1', max_length=100, blank=True)  # Field name made lowercase.
    attribute2 = models.CharField(db_column='Attribute2', max_length=100, blank=True)  # Field name made lowercase.
    attribute3 = models.CharField(db_column='Attribute3', max_length=100, blank=True)  # Field name made lowercase.
    attribute4 = models.CharField(db_column='Attribute4', max_length=100, blank=True)  # Field name made lowercase.
    attribute5 = models.CharField(db_column='Attribute5', max_length=100, blank=True)  # Field name made lowercase.
    attribute6 = models.CharField(db_column='Attribute6', max_length=100, blank=True)  # Field name made lowercase.
    attribute7 = models.CharField(db_column='Attribute7', max_length=100, blank=True)  # Field name made lowercase.
    attribute8 = models.CharField(db_column='Attribute8', max_length=100, blank=True)  # Field name made lowercase.
    attribute9 = models.CharField(db_column='Attribute9', max_length=100, blank=True)  # Field name made lowercase.
    attribute10 = models.CharField(db_column='Attribute10', max_length=100, blank=True)  # Field name made lowercase.
    attribute11 = models.CharField(db_column='Attribute11', max_length=100, blank=True)  # Field name made lowercase.
    attribute12 = models.CharField(db_column='Attribute12', max_length=100, blank=True)  # Field name made lowercase.
    attribute13 = models.CharField(db_column='Attribute13', max_length=100, blank=True)  # Field name made lowercase.
    attribute14 = models.CharField(db_column='Attribute14', max_length=100, blank=True)  # Field name made lowercase.
    attribute15 = models.CharField(db_column='Attribute15', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_batch'


class CarControl(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    plan_code = models.CharField(db_column='PlanCode', max_length=50)  # Field name made lowercase.
    car_number = models.CharField(db_column='CarNumber', max_length=100, blank=True)  # Field name made lowercase.
    weigh_house_codes = models.CharField(db_column='WeighHouseCodes', max_length=500,
                                         blank=True)  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    upload_bit = models.IntegerField(db_column='UploadBit', blank=True, null=True)  # Field name made lowercase.
    upload_time = models.DateTimeField(db_column='UploadTime', blank=True, null=True)  # Field name made lowercase.
    create_user_code = models.CharField(db_column='CreateUserCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CreateUserName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    last_modified_user_code = models.CharField(db_column='LastModifiedUserCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    last_modified_username = models.CharField(db_column='LastModifiedUserName', max_length=50,
                                              blank=True)  # Field name made lowercase.
    last_modified_time = models.DateTimeField(db_column='LastModifiedTime', blank=True,
                                              null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_carcontrol'


class CarTare(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    car_number = models.CharField(db_column='CarNumber', max_length=10)  # Field name made lowercase.
    tare_weight = models.FloatField(db_column='TareWeight', blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=50, blank=True)  # Field name made lowercase.
    weigh_house_codes = models.CharField(db_column='WeighHouseCodes', max_length=200,
                                         blank=True)  # Field name made lowercase.
    status = models.NullBooleanField(db_column='Status')  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    upload_bit = models.IntegerField(db_column='UploadBit', blank=True, null=True)  # Field name made lowercase.
    upload_time = models.DateTimeField(db_column='UploadTime', blank=True, null=True)  # Field name made lowercase.
    create_user_code = models.CharField(db_column='CreateUserCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CreateUserName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    last_modified_user_code = models.CharField(db_column='LastModifiedUserCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    last_modified_username = models.CharField(db_column='LastModifiedUserName', max_length=50,
                                              blank=True)  # Field name made lowercase.
    last_modified_time = models.DateTimeField(db_column='LastModifiedTime', blank=True,
                                              null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_cartare'


class Customer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_code = models.CharField(db_column='CustomerCode', max_length=50)  # Field name made lowercase.
    erp_code = models.CharField(db_column='ErpCode', max_length=50, blank=True)  # Field name made lowercase.
    customer_number = models.CharField(db_column='CustomerNumber', max_length=50,
                                       blank=True)  # Field name made lowercase.
    customer_name = models.CharField(db_column='CustomerName', max_length=100, blank=True)  # Field name made lowercase.
    customer_alias = models.CharField(db_column='CustomerAlias', max_length=100,
                                      blank=True)  # Field name made lowercase.
    weigh_house_codes = models.CharField(db_column='WeighHouseCodes', max_length=200,
                                         blank=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    status = models.NullBooleanField(db_column='Status')  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    upload_bit = models.IntegerField(db_column='UploadBit', blank=True, null=True)  # Field name made lowercase.
    upload_time = models.DateTimeField(db_column='UploadTime', blank=True, null=True)  # Field name made lowercase.
    create_user_code = models.CharField(db_column='CreateUserCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CreateUserName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    last_modified_user_code = models.CharField(db_column='LastModifiedUserCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    last_modified_username = models.CharField(db_column='LastModifiedUserName', max_length=50,
                                              blank=True)  # Field name made lowercase.
    last_modified_time = models.DateTimeField(db_column='LastModifiedTime', blank=True,
                                              null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.
    attribute1 = models.CharField(db_column='Attribute1', max_length=100, blank=True)  # Field name made lowercase.
    attribute2 = models.CharField(db_column='Attribute2', max_length=100, blank=True)  # Field name made lowercase.
    attribute3 = models.CharField(db_column='Attribute3', max_length=100, blank=True)  # Field name made lowercase.
    attribute4 = models.CharField(db_column='Attribute4', max_length=100, blank=True)  # Field name made lowercase.
    attribute5 = models.CharField(db_column='Attribute5', max_length=100, blank=True)  # Field name made lowercase.
    attribute6 = models.CharField(db_column='Attribute6', max_length=100, blank=True)  # Field name made lowercase.
    attribute7 = models.CharField(db_column='Attribute7', max_length=100, blank=True)  # Field name made lowercase.
    attribute8 = models.CharField(db_column='Attribute8', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_customer'


class DataLineInfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    weigh_record_number = models.CharField(db_column='WeighRecordNumber', max_length=50)  # Field name made lowercase.
    plan_code = models.CharField(db_column='PlanCode', max_length=50)  # Field name made lowercase.
    plan_number = models.CharField(db_column='PlanNumber', max_length=50, blank=True)  # Field name made lowercase.
    batch_number = models.CharField(db_column='BatchNumber', max_length=50, blank=True)  # Field name made lowercase.
    supplier_code = models.CharField(db_column='SupplierCode', max_length=50, blank=True)  # Field name made lowercase.
    supplier_name = models.CharField(db_column='SupplierName', max_length=100, blank=True)  # Field name made lowercase.
    recipient_code = models.CharField(db_column='RecipientCode', max_length=50,
                                      blank=True)  # Field name made lowercase.
    recipient_name = models.CharField(db_column='RecipientName', max_length=100,
                                      blank=True)  # Field name made lowercase.
    material_code = models.CharField(db_column='MaterialCode', max_length=50, blank=True)  # Field name made lowercase.
    material_name = models.CharField(db_column='MaterialName', max_length=100, blank=True)  # Field name made lowercase.
    specification = models.CharField(db_column='Specification', max_length=50, blank=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=50, blank=True)  # Field name made lowercase.
    car_number = models.CharField(db_column='CarNumber', max_length=10, blank=True)  # Field name made lowercase.
    grossweigh_house_code = models.CharField(db_column='GrossWeighHouseCode', max_length=50,
                                             blank=True)  # Field name made lowercase.
    grossweighmachinecode = models.CharField(db_column='GrossWeighMachineCode', max_length=50,
                                             blank=True)  # Field name made lowercase.
    grossweight = models.FloatField(db_column='GrossWeight', blank=True, null=True)  # Field name made lowercase.
    grossweightime = models.DateTimeField(db_column='GrossWeighTime', blank=True,
                                          null=True)  # Field name made lowercase.
    grossweighmancode = models.CharField(db_column='GrossWeighManCode', max_length=50,
                                         blank=True)  # Field name made lowercase.
    grossweighmanname = models.CharField(db_column='GrossWeighManName', max_length=50,
                                         blank=True)  # Field name made lowercase.
    grossweighsupervisorcode = models.CharField(db_column='GrossWeighSupervisorCode', max_length=50,
                                                blank=True)  # Field name made lowercase.
    grossweighsupervisor = models.CharField(db_column='GrossWeighSupervisor', max_length=50,
                                            blank=True)  # Field name made lowercase.
    grossweighshift = models.CharField(db_column='GrossWeighShift', max_length=50,
                                       blank=True)  # Field name made lowercase.
    tareweigh_house_code = models.CharField(db_column='TareWeighHouseCode', max_length=50,
                                            blank=True)  # Field name made lowercase.
    tareweighmachinecode = models.CharField(db_column='TareWeighMachineCode', max_length=50,
                                            blank=True)  # Field name made lowercase.
    tare_weight = models.FloatField(db_column='TareWeight', blank=True, null=True)  # Field name made lowercase.
    tare_weightime = models.DateTimeField(db_column='TareWeighTime', blank=True,
                                          null=True)  # Field name made lowercase.
    tareweighmancode = models.CharField(db_column='TareWeighManCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    tareweighmanname = models.CharField(db_column='TareWeighManName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    tareweighsupervisorcode = models.CharField(db_column='TareWeighSupervisorCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    tareweighsupervisor = models.CharField(db_column='TareWeighSupervisor', max_length=50,
                                           blank=True)  # Field name made lowercase.
    tareweighshift = models.CharField(db_column='TareWeighShift', max_length=50,
                                      blank=True)  # Field name made lowercase.
    ismanualinputtare = models.NullBooleanField(db_column='IsManualInputTare')  # Field name made lowercase.
    suttle = models.FloatField(db_column='Suttle', blank=True, null=True)  # Field name made lowercase.
    measure_unit = models.CharField(db_column='MeasureUnit', max_length=50, blank=True)  # Field name made lowercase.
    weightime = models.DateTimeField(db_column='WeighTime', blank=True, null=True)  # Field name made lowercase.
    deduction = models.FloatField(db_column='Deduction', blank=True, null=True)  # Field name made lowercase.
    deductionpercent = models.FloatField(db_column='DeductionPercent', blank=True,
                                         null=True)  # Field name made lowercase.
    twicededuction = models.FloatField(db_column='TwiceDeduction', blank=True, null=True)  # Field name made lowercase.
    twicedeductionpercent = models.FloatField(db_column='TwiceDeductionPercent', blank=True,
                                              null=True)  # Field name made lowercase.
    moisturecontent = models.FloatField(db_column='MoistureContent', blank=True,
                                        null=True)  # Field name made lowercase.
    ismanualinput = models.NullBooleanField(db_column='IsManualInput')  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    issurplus = models.NullBooleanField(db_column='IsSurplus')  # Field name made lowercase.
    isreturnpurchase = models.NullBooleanField(db_column='IsReturnPurchase')  # Field name made lowercase.
    create_user_code = models.CharField(db_column='CreateUserCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CreateUserName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    last_modified_user_code = models.CharField(db_column='LastModifiedUserCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    last_modified_username = models.CharField(db_column='LastModifiedUserName', max_length=50,
                                              blank=True)  # Field name made lowercase.
    last_modified_time = models.DateTimeField(db_column='LastModifiedTime', blank=True,
                                              null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.
    attribute1 = models.CharField(db_column='Attribute1', max_length=100, blank=True)  # Field name made lowercase.
    attribute2 = models.CharField(db_column='Attribute2', max_length=100, blank=True)  # Field name made lowercase.
    attribute3 = models.CharField(db_column='Attribute3', max_length=100, blank=True)  # Field name made lowercase.
    attribute4 = models.CharField(db_column='Attribute4', max_length=100, blank=True)  # Field name made lowercase.
    attribute5 = models.CharField(db_column='Attribute5', max_length=100, blank=True)  # Field name made lowercase.
    attribute6 = models.CharField(db_column='Attribute6', max_length=100, blank=True)  # Field name made lowercase.
    attribute7 = models.CharField(db_column='Attribute7', max_length=100, blank=True)  # Field name made lowercase.
    attribute8 = models.CharField(db_column='Attribute8', max_length=100, blank=True)  # Field name made lowercase.
    attribute9 = models.CharField(db_column='Attribute9', max_length=100, blank=True)  # Field name made lowercase.
    attribute10 = models.CharField(db_column='Attribute10', max_length=100, blank=True)  # Field name made lowercase.
    attribute11 = models.CharField(db_column='Attribute11', max_length=100, blank=True)  # Field name made lowercase.
    attribute12 = models.CharField(db_column='Attribute12', max_length=100, blank=True)  # Field name made lowercase.
    attribute13 = models.CharField(db_column='Attribute13', max_length=100, blank=True)  # Field name made lowercase.
    attribute14 = models.CharField(db_column='Attribute14', max_length=100, blank=True)  # Field name made lowercase.
    attribute15 = models.CharField(db_column='Attribute15', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_datalineinfo'


class DatalineinfoDetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    batch_number = models.IntegerField(db_column='BatchNumber', blank=True, null=True)  # Field name made lowercase.
    car_number = models.CharField(db_column='CarNumber', max_length=30, blank=True)  # Field name made lowercase.
    weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    weightime = models.DateTimeField(db_column='WeighTime', blank=True, null=True)  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.
    attribute1 = models.CharField(db_column='Attribute1', max_length=100, blank=True)  # Field name made lowercase.
    attribute2 = models.CharField(db_column='Attribute2', max_length=100, blank=True)  # Field name made lowercase.
    attribute3 = models.CharField(db_column='Attribute3', max_length=100, blank=True)  # Field name made lowercase.
    attribute4 = models.CharField(db_column='Attribute4', max_length=100, blank=True)  # Field name made lowercase.
    attribute5 = models.CharField(db_column='Attribute5', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_datalineinfo_detail'


class DatalineinfoDetailCache(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    batch_number = models.IntegerField(db_column='BatchNumber', blank=True, null=True)  # Field name made lowercase.
    car_number = models.CharField(db_column='CarNumber', max_length=30, blank=True)  # Field name made lowercase.
    weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    weightime = models.DateTimeField(db_column='WeighTime', blank=True, null=True)  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.
    attribute1 = models.CharField(db_column='Attribute1', max_length=100, blank=True)  # Field name made lowercase.
    attribute2 = models.CharField(db_column='Attribute2', max_length=100, blank=True)  # Field name made lowercase.
    attribute3 = models.CharField(db_column='Attribute3', max_length=100, blank=True)  # Field name made lowercase.
    attribute4 = models.CharField(db_column='Attribute4', max_length=100, blank=True)  # Field name made lowercase.
    attribute5 = models.CharField(db_column='Attribute5', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_datalineinfo_detail_cache'


class Datalineinfobak(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    recordid = models.IntegerField(db_column='RecordID', blank=True, null=True)  # Field name made lowercase.
    weigh_record_number = models.CharField(db_column='WeighRecordNumber', max_length=50,
                                           blank=True)  # Field name made lowercase.
    plan_code = models.CharField(db_column='PlanCode', max_length=50, blank=True)  # Field name made lowercase.
    plan_number = models.CharField(db_column='PlanNumber', max_length=50, blank=True)  # Field name made lowercase.
    batch_number = models.CharField(db_column='BatchNumber', max_length=50, blank=True)  # Field name made lowercase.
    supplier_code = models.CharField(db_column='SupplierCode', max_length=50, blank=True)  # Field name made lowercase.
    supplier_name = models.CharField(db_column='SupplierName', max_length=100, blank=True)  # Field name made lowercase.
    recipient_code = models.CharField(db_column='RecipientCode', max_length=50,
                                      blank=True)  # Field name made lowercase.
    recipient_name = models.CharField(db_column='RecipientName', max_length=100,
                                      blank=True)  # Field name made lowercase.
    material_code = models.CharField(db_column='MaterialCode', max_length=50, blank=True)  # Field name made lowercase.
    material_name = models.CharField(db_column='MaterialName', max_length=100, blank=True)  # Field name made lowercase.
    specification = models.CharField(db_column='Specification', max_length=50, blank=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=50, blank=True)  # Field name made lowercase.
    car_number = models.CharField(db_column='CarNumber', max_length=10, blank=True)  # Field name made lowercase.
    grossweigh_house_code = models.CharField(db_column='GrossWeighHouseCode', max_length=50,
                                             blank=True)  # Field name made lowercase.
    grossweighmachinecode = models.CharField(db_column='GrossWeighMachineCode', max_length=50,
                                             blank=True)  # Field name made lowercase.
    grossweight = models.FloatField(db_column='GrossWeight', blank=True, null=True)  # Field name made lowercase.
    grossweightime = models.DateTimeField(db_column='GrossWeighTime', blank=True,
                                          null=True)  # Field name made lowercase.
    grossweighmancode = models.CharField(db_column='GrossWeighManCode', max_length=50,
                                         blank=True)  # Field name made lowercase.
    grossweighmanname = models.CharField(db_column='GrossWeighManName', max_length=50,
                                         blank=True)  # Field name made lowercase.
    grossweighsupervisorcode = models.CharField(db_column='GrossWeighSupervisorCode', max_length=50,
                                                blank=True)  # Field name made lowercase.
    grossweighsupervisor = models.CharField(db_column='GrossWeighSupervisor', max_length=50,
                                            blank=True)  # Field name made lowercase.
    grossweighshift = models.CharField(db_column='GrossWeighShift', max_length=50,
                                       blank=True)  # Field name made lowercase.
    tareweigh_house_code = models.CharField(db_column='TareWeighHouseCode', max_length=50,
                                            blank=True)  # Field name made lowercase.
    tareweighmachinecode = models.CharField(db_column='TareWeighMachineCode', max_length=50,
                                            blank=True)  # Field name made lowercase.
    tare_weight = models.FloatField(db_column='TareWeight', blank=True, null=True)  # Field name made lowercase.
    tare_weightime = models.DateTimeField(db_column='TareWeighTime', blank=True,
                                          null=True)  # Field name made lowercase.
    tareweighmancode = models.CharField(db_column='TareWeighManCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    tareweighmanname = models.CharField(db_column='TareWeighManName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    tareweighsupervisorcode = models.CharField(db_column='TareWeighSupervisorCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    tareweighsupervisor = models.CharField(db_column='TareWeighSupervisor', max_length=50,
                                           blank=True)  # Field name made lowercase.
    tareweighshift = models.CharField(db_column='TareWeighShift', max_length=50,
                                      blank=True)  # Field name made lowercase.
    ismanualinputtare = models.NullBooleanField(db_column='IsManualInputTare')  # Field name made lowercase.
    suttle = models.FloatField(db_column='Suttle', blank=True, null=True)  # Field name made lowercase.
    measure_unit = models.CharField(db_column='MeasureUnit', max_length=50, blank=True)  # Field name made lowercase.
    weightime = models.DateTimeField(db_column='WeighTime', blank=True, null=True)  # Field name made lowercase.
    deduction = models.FloatField(db_column='Deduction', blank=True, null=True)  # Field name made lowercase.
    deductionpercent = models.FloatField(db_column='DeductionPercent', blank=True,
                                         null=True)  # Field name made lowercase.
    twicededuction = models.FloatField(db_column='TwiceDeduction', blank=True, null=True)  # Field name made lowercase.
    twicedeductionpercent = models.FloatField(db_column='TwiceDeductionPercent', blank=True,
                                              null=True)  # Field name made lowercase.
    moisturecontent = models.FloatField(db_column='MoistureContent', blank=True,
                                        null=True)  # Field name made lowercase.
    ismanualinput = models.NullBooleanField(db_column='IsManualInput')  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    issurplus = models.NullBooleanField(db_column='IsSurplus')  # Field name made lowercase.
    isreturnpurchase = models.NullBooleanField(db_column='IsReturnPurchase')  # Field name made lowercase.
    create_user_code = models.CharField(db_column='CreateUserCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CreateUserName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    last_modified_user_code = models.CharField(db_column='LastModifiedUserCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    last_modified_username = models.CharField(db_column='LastModifiedUserName', max_length=50,
                                              blank=True)  # Field name made lowercase.
    last_modified_time = models.DateTimeField(db_column='LastModifiedTime', blank=True,
                                              null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.
    attribute1 = models.CharField(db_column='Attribute1', max_length=100, blank=True)  # Field name made lowercase.
    attribute2 = models.CharField(db_column='Attribute2', max_length=100, blank=True)  # Field name made lowercase.
    attribute3 = models.CharField(db_column='Attribute3', max_length=100, blank=True)  # Field name made lowercase.
    attribute4 = models.CharField(db_column='Attribute4', max_length=100, blank=True)  # Field name made lowercase.
    attribute5 = models.CharField(db_column='Attribute5', max_length=100, blank=True)  # Field name made lowercase.
    attribute6 = models.CharField(db_column='Attribute6', max_length=100, blank=True)  # Field name made lowercase.
    attribute7 = models.CharField(db_column='Attribute7', max_length=100, blank=True)  # Field name made lowercase.
    attribute8 = models.CharField(db_column='Attribute8', max_length=100, blank=True)  # Field name made lowercase.
    attribute9 = models.CharField(db_column='Attribute9', max_length=100, blank=True)  # Field name made lowercase.
    attribute10 = models.CharField(db_column='Attribute10', max_length=100, blank=True)  # Field name made lowercase.
    attribute11 = models.CharField(db_column='Attribute11', max_length=100, blank=True)  # Field name made lowercase.
    attribute12 = models.CharField(db_column='Attribute12', max_length=100, blank=True)  # Field name made lowercase.
    attribute13 = models.CharField(db_column='Attribute13', max_length=100, blank=True)  # Field name made lowercase.
    attribute14 = models.CharField(db_column='Attribute14', max_length=100, blank=True)  # Field name made lowercase.
    attribute15 = models.CharField(db_column='Attribute15', max_length=100, blank=True)  # Field name made lowercase.
    createrecordusercode = models.CharField(db_column='CreateRecordUserCode', max_length=50,
                                            blank=True)  # Field name made lowercase.
    createrecordusername = models.CharField(db_column='CreateRecordUserName', max_length=50,
                                            blank=True)  # Field name made lowercase.
    createrecordtime = models.DateTimeField(db_column='CreateRecordTime', blank=True,
                                            null=True)  # Field name made lowercase.
    operationtype = models.CharField(db_column='OperationType', max_length=50, blank=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_datalineinfobak'


class Datalineinfoiface(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    weigh_record_number = models.CharField(db_column='WeighRecordNumber', max_length=50)  # Field name made lowercase.
    plan_code = models.CharField(db_column='PlanCode', max_length=50)  # Field name made lowercase.
    plan_number = models.CharField(db_column='PlanNumber', max_length=50, blank=True)  # Field name made lowercase.
    batch_number = models.CharField(db_column='BatchNumber', max_length=50, blank=True)  # Field name made lowercase.
    supplier_code = models.CharField(db_column='SupplierCode', max_length=50, blank=True)  # Field name made lowercase.
    supplier_name = models.CharField(db_column='SupplierName', max_length=100, blank=True)  # Field name made lowercase.
    recipient_code = models.CharField(db_column='RecipientCode', max_length=50,
                                      blank=True)  # Field name made lowercase.
    recipient_name = models.CharField(db_column='RecipientName', max_length=100,
                                      blank=True)  # Field name made lowercase.
    material_code = models.CharField(db_column='MaterialCode', max_length=50, blank=True)  # Field name made lowercase.
    material_name = models.CharField(db_column='MaterialName', max_length=100, blank=True)  # Field name made lowercase.
    specification = models.CharField(db_column='Specification', max_length=50, blank=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=50, blank=True)  # Field name made lowercase.
    car_number = models.CharField(db_column='CarNumber', max_length=10, blank=True)  # Field name made lowercase.
    grossweigh_house_code = models.CharField(db_column='GrossWeighHouseCode', max_length=50,
                                             blank=True)  # Field name made lowercase.
    grossweighmachinecode = models.CharField(db_column='GrossWeighMachineCode', max_length=50,
                                             blank=True)  # Field name made lowercase.
    grossweight = models.FloatField(db_column='GrossWeight', blank=True, null=True)  # Field name made lowercase.
    grossweightime = models.DateTimeField(db_column='GrossWeighTime', blank=True,
                                          null=True)  # Field name made lowercase.
    grossweighmancode = models.CharField(db_column='GrossWeighManCode', max_length=50,
                                         blank=True)  # Field name made lowercase.
    grossweighmanname = models.CharField(db_column='GrossWeighManName', max_length=50,
                                         blank=True)  # Field name made lowercase.
    grossweighsupervisorcode = models.CharField(db_column='GrossWeighSupervisorCode', max_length=50,
                                                blank=True)  # Field name made lowercase.
    grossweighsupervisor = models.CharField(db_column='GrossWeighSupervisor', max_length=50,
                                            blank=True)  # Field name made lowercase.
    grossweighshift = models.CharField(db_column='GrossWeighShift', max_length=50,
                                       blank=True)  # Field name made lowercase.
    tareweigh_house_code = models.CharField(db_column='TareWeighHouseCode', max_length=50,
                                            blank=True)  # Field name made lowercase.
    tareweighmachinecode = models.CharField(db_column='TareWeighMachineCode', max_length=50,
                                            blank=True)  # Field name made lowercase.
    tare_weight = models.FloatField(db_column='TareWeight', blank=True, null=True)  # Field name made lowercase.
    tare_weightime = models.DateTimeField(db_column='TareWeighTime', blank=True,
                                          null=True)  # Field name made lowercase.
    tareweighmancode = models.CharField(db_column='TareWeighManCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    tareweighmanname = models.CharField(db_column='TareWeighManName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    tareweighsupervisorcode = models.CharField(db_column='TareWeighSupervisorCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    tareweighsupervisor = models.CharField(db_column='TareWeighSupervisor', max_length=50,
                                           blank=True)  # Field name made lowercase.
    tareweighshift = models.CharField(db_column='TareWeighShift', max_length=50,
                                      blank=True)  # Field name made lowercase.
    ismanualinputtare = models.NullBooleanField(db_column='IsManualInputTare')  # Field name made lowercase.
    suttle = models.FloatField(db_column='Suttle', blank=True, null=True)  # Field name made lowercase.
    measure_unit = models.CharField(db_column='MeasureUnit', max_length=50, blank=True)  # Field name made lowercase.
    weightime = models.DateTimeField(db_column='WeighTime', blank=True, null=True)  # Field name made lowercase.
    deduction = models.FloatField(db_column='Deduction', blank=True, null=True)  # Field name made lowercase.
    deductionpercent = models.FloatField(db_column='DeductionPercent', blank=True,
                                         null=True)  # Field name made lowercase.
    twicededuction = models.FloatField(db_column='TwiceDeduction', blank=True, null=True)  # Field name made lowercase.
    twicedeductionpercent = models.FloatField(db_column='TwiceDeductionPercent', blank=True,
                                              null=True)  # Field name made lowercase.
    moisturecontent = models.FloatField(db_column='MoistureContent', blank=True,
                                        null=True)  # Field name made lowercase.
    ismanualinput = models.NullBooleanField(db_column='IsManualInput')  # Field name made lowercase.
    issurplus = models.NullBooleanField(db_column='IsSurplus')  # Field name made lowercase.
    isreturnpurchase = models.NullBooleanField(db_column='IsReturnPurchase')  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    upload_bit = models.IntegerField(db_column='UploadBit', blank=True, null=True)  # Field name made lowercase.
    upload_time = models.DateTimeField(db_column='UploadTime', blank=True, null=True)  # Field name made lowercase.
    create_user_code = models.CharField(db_column='CreateUserCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CreateUserName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    last_modified_user_code = models.CharField(db_column='LastModifiedUserCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    last_modified_username = models.CharField(db_column='LastModifiedUserName', max_length=50,
                                              blank=True)  # Field name made lowercase.
    last_modified_time = models.DateTimeField(db_column='LastModifiedTime', blank=True,
                                              null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.
    attribute1 = models.CharField(db_column='Attribute1', max_length=100, blank=True)  # Field name made lowercase.
    attribute2 = models.CharField(db_column='Attribute2', max_length=100, blank=True)  # Field name made lowercase.
    attribute3 = models.CharField(db_column='Attribute3', max_length=100, blank=True)  # Field name made lowercase.
    attribute4 = models.CharField(db_column='Attribute4', max_length=100, blank=True)  # Field name made lowercase.
    attribute5 = models.CharField(db_column='Attribute5', max_length=100, blank=True)  # Field name made lowercase.
    attribute6 = models.CharField(db_column='Attribute6', max_length=100, blank=True)  # Field name made lowercase.
    attribute7 = models.CharField(db_column='Attribute7', max_length=100, blank=True)  # Field name made lowercase.
    attribute8 = models.CharField(db_column='Attribute8', max_length=100, blank=True)  # Field name made lowercase.
    attribute9 = models.CharField(db_column='Attribute9', max_length=100, blank=True)  # Field name made lowercase.
    attribute10 = models.CharField(db_column='Attribute10', max_length=100, blank=True)  # Field name made lowercase.
    attribute11 = models.CharField(db_column='Attribute11', max_length=100, blank=True)  # Field name made lowercase.
    attribute12 = models.CharField(db_column='Attribute12', max_length=100, blank=True)  # Field name made lowercase.
    attribute13 = models.CharField(db_column='Attribute13', max_length=100, blank=True)  # Field name made lowercase.
    attribute14 = models.CharField(db_column='Attribute14', max_length=100, blank=True)  # Field name made lowercase.
    attribute15 = models.CharField(db_column='Attribute15', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_datalineinfoiface'


class Deviceinfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    devicecode = models.CharField(db_column='DeviceCode', max_length=50)  # Field name made lowercase.
    devicenumber = models.CharField(db_column='DeviceNumber', max_length=50, blank=True)  # Field name made lowercase.
    devicename = models.CharField(db_column='DeviceName', max_length=50, blank=True)  # Field name made lowercase.
    weigh_house_codes = models.CharField(db_column='WeighHouseCodes', max_length=200,
                                         blank=True)  # Field name made lowercase.
    portname = models.CharField(db_column='PortName', max_length=50, blank=True)  # Field name made lowercase.
    baudrate = models.IntegerField(db_column='BaudRate', blank=True, null=True)  # Field name made lowercase.
    parity = models.CharField(db_column='Parity', max_length=50, blank=True)  # Field name made lowercase.
    databits = models.IntegerField(db_column='DataBits', blank=True, null=True)  # Field name made lowercase.
    stopbits = models.IntegerField(db_column='StopBits', blank=True, null=True)  # Field name made lowercase.
    dtsenable = models.NullBooleanField(db_column='DtsEnable')  # Field name made lowercase.
    rtsenable = models.NullBooleanField(db_column='RtsEnable')  # Field name made lowercase.
    receiveddatalength = models.IntegerField(db_column='ReceivedDataLength', blank=True,
                                             null=True)  # Field name made lowercase.
    iscontinuoussend = models.NullBooleanField(db_column='IsContinuousSend')  # Field name made lowercase.
    startstring = models.CharField(db_column='StartString', max_length=50, blank=True)  # Field name made lowercase.
    endstring = models.CharField(db_column='EndString', max_length=50, blank=True)  # Field name made lowercase.
    isinvertedsequence = models.NullBooleanField(db_column='IsInvertedSequence')  # Field name made lowercase.
    datastaredindex = models.IntegerField(db_column='DataStaredIndex', blank=True,
                                          null=True)  # Field name made lowercase.
    datalength = models.IntegerField(db_column='DataLength', blank=True, null=True)  # Field name made lowercase.
    datapricision = models.IntegerField(db_column='DataPricision', blank=True, null=True)  # Field name made lowercase.
    converttype = models.CharField(db_column='ConvertType', max_length=50, blank=True)  # Field name made lowercase.
    filterstring = models.CharField(db_column='FilterString', max_length=50, blank=True)  # Field name made lowercase.
    status = models.NullBooleanField(db_column='Status')  # Field name made lowercase.
    isbasicrecord = models.NullBooleanField(db_column='IsBasicRecord')  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    upload_bit = models.IntegerField(db_column='UploadBit', blank=True, null=True)  # Field name made lowercase.
    upload_time = models.DateTimeField(db_column='UploadTime', blank=True, null=True)  # Field name made lowercase.
    create_user_code = models.CharField(db_column='CreateUserCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CreateUserName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    last_modified_user_code = models.CharField(db_column='LastModifiedUserCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    last_modified_username = models.CharField(db_column='LastModifiedUserName', max_length=50,
                                              blank=True)  # Field name made lowercase.
    last_modified_time = models.DateTimeField(db_column='LastModifiedTime', blank=True,
                                              null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.
    attribute1 = models.CharField(db_column='Attribute1', max_length=100, blank=True)  # Field name made lowercase.
    attribute2 = models.CharField(db_column='Attribute2', max_length=100, blank=True)  # Field name made lowercase.
    attribute3 = models.CharField(db_column='Attribute3', max_length=100, blank=True)  # Field name made lowercase.
    attribute4 = models.CharField(db_column='Attribute4', max_length=100, blank=True)  # Field name made lowercase.
    attribute5 = models.CharField(db_column='Attribute5', max_length=100, blank=True)  # Field name made lowercase.
    attribute6 = models.CharField(db_column='Attribute6', max_length=100, blank=True)  # Field name made lowercase.
    attribute7 = models.CharField(db_column='Attribute7', max_length=100, blank=True)  # Field name made lowercase.
    attribute8 = models.CharField(db_column='Attribute8', max_length=100, blank=True)  # Field name made lowercase.
    attribute9 = models.CharField(db_column='Attribute9', max_length=100, blank=True)  # Field name made lowercase.
    attribute10 = models.CharField(db_column='Attribute10', max_length=100, blank=True)  # Field name made lowercase.
    attribute11 = models.CharField(db_column='Attribute11', max_length=100, blank=True)  # Field name made lowercase.
    attribute12 = models.CharField(db_column='Attribute12', max_length=100, blank=True)  # Field name made lowercase.
    attribute13 = models.CharField(db_column='Attribute13', max_length=100, blank=True)  # Field name made lowercase.
    attribute14 = models.CharField(db_column='Attribute14', max_length=100, blank=True)  # Field name made lowercase.
    attribute15 = models.CharField(db_column='Attribute15', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_deviceinfo'


class Groupauthority(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_group_code = models.CharField(db_column='UserGroupCode', max_length=50,
                                       blank=True)  # Field name made lowercase.
    authoritycode = models.CharField(db_column='AuthorityCode', max_length=50, blank=True)  # Field name made lowercase.
    weigh_house_codes = models.CharField(db_column='WeighHouseCodes', max_length=200,
                                         blank=True)  # Field name made lowercase.
    status = models.NullBooleanField(db_column='Status')  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    upload_bit = models.IntegerField(db_column='UploadBit', blank=True, null=True)  # Field name made lowercase.
    upload_time = models.DateTimeField(db_column='UploadTime', blank=True, null=True)  # Field name made lowercase.
    create_user_code = models.CharField(db_column='CreateUserCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CreateUserName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    last_modified_user_code = models.CharField(db_column='LastModifiedUserCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    last_modified_username = models.CharField(db_column='LastModifiedUserName', max_length=50,
                                              blank=True)  # Field name made lowercase.
    last_modified_time = models.DateTimeField(db_column='LastModifiedTime', blank=True,
                                              null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.
    attribute1 = models.CharField(db_column='Attribute1', max_length=100, blank=True)  # Field name made lowercase.
    attribute2 = models.CharField(db_column='Attribute2', max_length=100, blank=True)  # Field name made lowercase.
    attribute3 = models.CharField(db_column='Attribute3', max_length=100, blank=True)  # Field name made lowercase.
    attribute4 = models.CharField(db_column='Attribute4', max_length=100, blank=True)  # Field name made lowercase.
    attribute5 = models.CharField(db_column='Attribute5', max_length=100, blank=True)  # Field name made lowercase.
    attribute6 = models.CharField(db_column='Attribute6', max_length=100, blank=True)  # Field name made lowercase.
    attribute7 = models.CharField(db_column='Attribute7', max_length=100, blank=True)  # Field name made lowercase.
    attribute8 = models.CharField(db_column='Attribute8', max_length=100, blank=True)  # Field name made lowercase.
    attribute9 = models.CharField(db_column='Attribute9', max_length=100, blank=True)  # Field name made lowercase.
    attribute10 = models.CharField(db_column='Attribute10', max_length=100, blank=True)  # Field name made lowercase.
    attribute11 = models.CharField(db_column='Attribute11', max_length=100, blank=True)  # Field name made lowercase.
    attribute12 = models.CharField(db_column='Attribute12', max_length=100, blank=True)  # Field name made lowercase.
    attribute13 = models.CharField(db_column='Attribute13', max_length=100, blank=True)  # Field name made lowercase.
    attribute14 = models.CharField(db_column='Attribute14', max_length=100, blank=True)  # Field name made lowercase.
    attribute15 = models.CharField(db_column='Attribute15', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_groupauthority'


class Groupauthorityusers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_group_code = models.CharField(db_column='UserGroupCode', max_length=50,
                                       blank=True)  # Field name made lowercase.
    usercode = models.CharField(db_column='UserCode', max_length=50, blank=True)  # Field name made lowercase.
    weigh_house_codes = models.CharField(db_column='WeighHouseCodes', max_length=200,
                                         blank=True)  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    upload_bit = models.IntegerField(db_column='UploadBit', blank=True, null=True)  # Field name made lowercase.
    upload_time = models.DateTimeField(db_column='UploadTime', blank=True, null=True)  # Field name made lowercase.
    create_user_code = models.CharField(db_column='CreateUserCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CreateUserName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    last_modified_user_code = models.CharField(db_column='LastModifiedUserCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    last_modified_username = models.CharField(db_column='LastModifiedUserName', max_length=50,
                                              blank=True)  # Field name made lowercase.
    last_modified_time = models.DateTimeField(db_column='LastModifiedTime', blank=True,
                                              null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.
    attribute1 = models.CharField(db_column='Attribute1', max_length=100, blank=True)  # Field name made lowercase.
    attribute2 = models.CharField(db_column='Attribute2', max_length=100, blank=True)  # Field name made lowercase.
    attribute3 = models.CharField(db_column='Attribute3', max_length=100, blank=True)  # Field name made lowercase.
    attribute4 = models.CharField(db_column='Attribute4', max_length=100, blank=True)  # Field name made lowercase.
    attribute5 = models.CharField(db_column='Attribute5', max_length=100, blank=True)  # Field name made lowercase.
    attribute6 = models.CharField(db_column='Attribute6', max_length=100, blank=True)  # Field name made lowercase.
    attribute7 = models.CharField(db_column='Attribute7', max_length=100, blank=True)  # Field name made lowercase.
    attribute8 = models.CharField(db_column='Attribute8', max_length=100, blank=True)  # Field name made lowercase.
    attribute9 = models.CharField(db_column='Attribute9', max_length=100, blank=True)  # Field name made lowercase.
    attribute10 = models.CharField(db_column='Attribute10', max_length=100, blank=True)  # Field name made lowercase.
    attribute11 = models.CharField(db_column='Attribute11', max_length=100, blank=True)  # Field name made lowercase.
    attribute12 = models.CharField(db_column='Attribute12', max_length=100, blank=True)  # Field name made lowercase.
    attribute13 = models.CharField(db_column='Attribute13', max_length=100, blank=True)  # Field name made lowercase.
    attribute14 = models.CharField(db_column='Attribute14', max_length=100, blank=True)  # Field name made lowercase.
    attribute15 = models.CharField(db_column='Attribute15', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_groupauthorityusers'


class Log(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    operationtype = models.CharField(db_column='OperationType', max_length=50, blank=True)  # Field name made lowercase.
    operationresult = models.CharField(db_column='OperationResult', max_length=150,
                                       blank=True)  # Field name made lowercase.
    operationdescription = models.CharField(db_column='OperationDescription', max_length=1000,
                                            blank=True)  # Field name made lowercase.
    weigh_house_codes = models.CharField(db_column='WeighHouseCodes', max_length=200,
                                         blank=True)  # Field name made lowercase.
    generatetime = models.DateTimeField(db_column='GenerateTime', blank=True, null=True)  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    upload_bit = models.IntegerField(db_column='UploadBit', blank=True, null=True)  # Field name made lowercase.
    upload_time = models.DateTimeField(db_column='UploadTime', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.
    attribute1 = models.CharField(db_column='Attribute1', max_length=100, blank=True)  # Field name made lowercase.
    attribute2 = models.CharField(db_column='Attribute2', max_length=100, blank=True)  # Field name made lowercase.
    attribute3 = models.CharField(db_column='Attribute3', max_length=100, blank=True)  # Field name made lowercase.
    attribute4 = models.CharField(db_column='Attribute4', max_length=100, blank=True)  # Field name made lowercase.
    attribute5 = models.CharField(db_column='Attribute5', max_length=100, blank=True)  # Field name made lowercase.
    attribute6 = models.CharField(db_column='Attribute6', max_length=100, blank=True)  # Field name made lowercase.
    attribute7 = models.CharField(db_column='Attribute7', max_length=100, blank=True)  # Field name made lowercase.
    attribute8 = models.CharField(db_column='Attribute8', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_log'


class Material(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    material_code = models.CharField(db_column='MaterialCode', max_length=50)  # Field name made lowercase.
    erp_code = models.CharField(db_column='ErpCode', max_length=50, blank=True)  # Field name made lowercase.
    materialnumber = models.CharField(db_column='MaterialNumber', max_length=50,
                                      blank=True)  # Field name made lowercase.
    material_name = models.CharField(db_column='MaterialName', max_length=100, blank=True)  # Field name made lowercase.
    weigh_house_codes = models.CharField(db_column='WeighHouseCodes', max_length=200,
                                         blank=True)  # Field name made lowercase.
    status = models.NullBooleanField(db_column='Status')  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    upload_bit = models.IntegerField(db_column='UploadBit', blank=True, null=True)  # Field name made lowercase.
    upload_time = models.DateTimeField(db_column='UploadTime', blank=True, null=True)  # Field name made lowercase.
    create_user_code = models.CharField(db_column='CreateUserCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CreateUserName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    last_modified_user_code = models.CharField(db_column='LastModifiedUserCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    last_modified_username = models.CharField(db_column='LastModifiedUserName', max_length=50,
                                              blank=True)  # Field name made lowercase.
    last_modified_time = models.DateTimeField(db_column='LastModifiedTime', blank=True,
                                              null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.
    attribute1 = models.CharField(db_column='Attribute1', max_length=100, blank=True)  # Field name made lowercase.
    attribute2 = models.CharField(db_column='Attribute2', max_length=100, blank=True)  # Field name made lowercase.
    attribute3 = models.CharField(db_column='Attribute3', max_length=100, blank=True)  # Field name made lowercase.
    attribute4 = models.CharField(db_column='Attribute4', max_length=100, blank=True)  # Field name made lowercase.
    attribute5 = models.CharField(db_column='Attribute5', max_length=100, blank=True)  # Field name made lowercase.
    attribute6 = models.CharField(db_column='Attribute6', max_length=100, blank=True)  # Field name made lowercase.
    attribute7 = models.CharField(db_column='Attribute7', max_length=100, blank=True)  # Field name made lowercase.
    attribute8 = models.CharField(db_column='Attribute8', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_material'


class Menu(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    menucode = models.CharField(db_column='MenuCode', max_length=50, blank=True)  # Field name made lowercase.
    menunumber = models.CharField(db_column='MenuNumber', max_length=50, blank=True)  # Field name made lowercase.
    menuname = models.CharField(db_column='MenuName', max_length=100, blank=True)  # Field name made lowercase.
    status = models.NullBooleanField(db_column='Status')  # Field name made lowercase.
    weigh_house_codes = models.CharField(db_column='WeighHouseCodes', max_length=200,
                                         blank=True)  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    upload_bit = models.IntegerField(db_column='UploadBit', blank=True, null=True)  # Field name made lowercase.
    upload_time = models.DateTimeField(db_column='UploadTime', blank=True, null=True)  # Field name made lowercase.
    create_user_code = models.CharField(db_column='CreateUserCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CreateUserName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    last_modified_user_code = models.CharField(db_column='LastModifiedUserCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    last_modified_username = models.CharField(db_column='LastModifiedUserName', max_length=50,
                                              blank=True)  # Field name made lowercase.
    last_modified_time = models.DateTimeField(db_column='LastModifiedTime', blank=True,
                                              null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.
    attribute1 = models.CharField(db_column='Attribute1', max_length=100, blank=True)  # Field name made lowercase.
    attribute2 = models.CharField(db_column='Attribute2', max_length=100, blank=True)  # Field name made lowercase.
    attribute3 = models.CharField(db_column='Attribute3', max_length=100, blank=True)  # Field name made lowercase.
    attribute4 = models.CharField(db_column='Attribute4', max_length=100, blank=True)  # Field name made lowercase.
    attribute5 = models.CharField(db_column='Attribute5', max_length=100, blank=True)  # Field name made lowercase.
    attribute6 = models.CharField(db_column='Attribute6', max_length=100, blank=True)  # Field name made lowercase.
    attribute7 = models.CharField(db_column='Attribute7', max_length=100, blank=True)  # Field name made lowercase.
    attribute8 = models.CharField(db_column='Attribute8', max_length=100, blank=True)  # Field name made lowercase.
    attribute9 = models.CharField(db_column='Attribute9', max_length=100, blank=True)  # Field name made lowercase.
    attribute10 = models.CharField(db_column='Attribute10', max_length=100, blank=True)  # Field name made lowercase.
    attribute11 = models.CharField(db_column='Attribute11', max_length=100, blank=True)  # Field name made lowercase.
    attribute12 = models.CharField(db_column='Attribute12', max_length=100, blank=True)  # Field name made lowercase.
    attribute13 = models.CharField(db_column='Attribute13', max_length=100, blank=True)  # Field name made lowercase.
    attribute14 = models.CharField(db_column='Attribute14', max_length=100, blank=True)  # Field name made lowercase.
    attribute15 = models.CharField(db_column='Attribute15', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_menu'


class Model(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    modelcode = models.CharField(db_column='ModelCode', max_length=50, blank=True)  # Field name made lowercase.
    modelnumber = models.CharField(db_column='ModelNumber', max_length=50, blank=True)  # Field name made lowercase.
    modelname = models.CharField(db_column='ModelName', max_length=50, blank=True)  # Field name made lowercase.
    length = models.FloatField(db_column='Length', blank=True, null=True)  # Field name made lowercase.
    width = models.FloatField(db_column='Width', blank=True, null=True)  # Field name made lowercase.
    height = models.FloatField(db_column='Height', blank=True, null=True)  # Field name made lowercase.
    length_unit = models.CharField(db_column='LengthUnit', max_length=50, blank=True)  # Field name made lowercase.
    width_unit = models.CharField(db_column='WidthUnit', max_length=50, blank=True)  # Field name made lowercase.
    height_unit = models.CharField(db_column='HeightUnit', max_length=50, blank=True)  # Field name made lowercase.
    status = models.NullBooleanField(db_column='Status')  # Field name made lowercase.
    weigh_house_codes = models.CharField(db_column='WeighHouseCodes', max_length=200,
                                         blank=True)  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    upload_bit = models.IntegerField(db_column='UploadBit', blank=True, null=True)  # Field name made lowercase.
    upload_time = models.DateTimeField(db_column='UploadTime', blank=True, null=True)  # Field name made lowercase.
    create_user_code = models.CharField(db_column='CreateUserCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CreateUserName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    last_modified_user_code = models.CharField(db_column='LastModifiedUserCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    last_modified_username = models.CharField(db_column='LastModifiedUserName', max_length=50,
                                              blank=True)  # Field name made lowercase.
    last_modified_time = models.DateTimeField(db_column='LastModifiedTime', blank=True,
                                              null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.
    attribute1 = models.CharField(db_column='Attribute1', max_length=100, blank=True)  # Field name made lowercase.
    attribute2 = models.CharField(db_column='Attribute2', max_length=100, blank=True)  # Field name made lowercase.
    attribute3 = models.CharField(db_column='Attribute3', max_length=100, blank=True)  # Field name made lowercase.
    attribute4 = models.CharField(db_column='Attribute4', max_length=100, blank=True)  # Field name made lowercase.
    attribute5 = models.CharField(db_column='Attribute5', max_length=100, blank=True)  # Field name made lowercase.
    attribute6 = models.CharField(db_column='Attribute6', max_length=100, blank=True)  # Field name made lowercase.
    attribute7 = models.CharField(db_column='Attribute7', max_length=100, blank=True)  # Field name made lowercase.
    attribute8 = models.CharField(db_column='Attribute8', max_length=100, blank=True)  # Field name made lowercase.
    attribute9 = models.CharField(db_column='Attribute9', max_length=100, blank=True)  # Field name made lowercase.
    attribute10 = models.CharField(db_column='Attribute10', max_length=100, blank=True)  # Field name made lowercase.
    attribute11 = models.CharField(db_column='Attribute11', max_length=100, blank=True)  # Field name made lowercase.
    attribute12 = models.CharField(db_column='Attribute12', max_length=100, blank=True)  # Field name made lowercase.
    attribute13 = models.CharField(db_column='Attribute13', max_length=100, blank=True)  # Field name made lowercase.
    attribute14 = models.CharField(db_column='Attribute14', max_length=100, blank=True)  # Field name made lowercase.
    attribute15 = models.CharField(db_column='Attribute15', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_model'


class Operator(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    usercode = models.CharField(db_column='UserCode', max_length=50)  # Field name made lowercase.
    usernumber = models.CharField(db_column='UserNumber', max_length=50, blank=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100, blank=True)  # Field name made lowercase.
    weigh_house_codes = models.CharField(db_column='WeighHouseCodes', max_length=200,
                                         blank=True)  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    upload_bit = models.IntegerField(db_column='UploadBit', blank=True, null=True)  # Field name made lowercase.
    upload_time = models.DateTimeField(db_column='UploadTime', blank=True, null=True)  # Field name made lowercase.
    status = models.NullBooleanField(db_column='Status')  # Field name made lowercase.
    create_user_code = models.CharField(db_column='CreateUserCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CreateUserName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    last_modified_user_code = models.CharField(db_column='LastModifiedUserCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    last_modified_username = models.CharField(db_column='LastModifiedUserName', max_length=50,
                                              blank=True)  # Field name made lowercase.
    last_modified_time = models.DateTimeField(db_column='LastModifiedTime', blank=True,
                                              null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.
    attribute1 = models.CharField(db_column='Attribute1', max_length=100, blank=True)  # Field name made lowercase.
    attribute2 = models.CharField(db_column='Attribute2', max_length=100, blank=True)  # Field name made lowercase.
    attribute3 = models.CharField(db_column='Attribute3', max_length=100, blank=True)  # Field name made lowercase.
    attribute4 = models.CharField(db_column='Attribute4', max_length=100, blank=True)  # Field name made lowercase.
    attribute5 = models.CharField(db_column='Attribute5', max_length=100, blank=True)  # Field name made lowercase.
    attribute6 = models.CharField(db_column='Attribute6', max_length=100, blank=True)  # Field name made lowercase.
    attribute7 = models.CharField(db_column='Attribute7', max_length=100, blank=True)  # Field name made lowercase.
    attribute8 = models.CharField(db_column='Attribute8', max_length=100, blank=True)  # Field name made lowercase.
    attribute9 = models.CharField(db_column='Attribute9', max_length=100, blank=True)  # Field name made lowercase.
    attribute10 = models.CharField(db_column='Attribute10', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_operator'


class Parameters(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    table_name = models.CharField(db_column='TableName', max_length=128, blank=True)  # Field name made lowercase.
    columnid = models.IntegerField(db_column='ColumnID', blank=True, null=True)  # Field name made lowercase.
    columnname = models.CharField(db_column='ColumnName', max_length=128, blank=True)  # Field name made lowercase.
    defaultname = models.CharField(db_column='DefaultName', max_length=128, blank=True)  # Field name made lowercase.
    aliasname = models.CharField(db_column='AliasName', max_length=128, blank=True)  # Field name made lowercase.
    length = models.IntegerField(db_column='Length', blank=True, null=True)  # Field name made lowercase.
    status = models.NullBooleanField(db_column='Status')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=128, blank=True)  # Field name made lowercase.
    isparameter = models.NullBooleanField(db_column='IsParameter')  # Field name made lowercase.
    sqlcodes = models.CharField(db_column='SqlCodes', max_length=200, blank=True)  # Field name made lowercase.
    isresult = models.NullBooleanField(db_column='IsResult')  # Field name made lowercase.
    weigh_house_codes = models.CharField(db_column='WeighHouseCodes', max_length=200,
                                         blank=True)  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    upload_bit = models.IntegerField(db_column='UploadBit', blank=True, null=True)  # Field name made lowercase.
    upload_time = models.DateTimeField(db_column='UploadTime', blank=True, null=True)  # Field name made lowercase.
    create_user_code = models.CharField(db_column='CreateUserCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CreateUserName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    last_modified_user_code = models.CharField(db_column='LastModifiedUserCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    last_modified_username = models.CharField(db_column='LastModifiedUserName', max_length=50,
                                              blank=True)  # Field name made lowercase.
    last_modified_time = models.DateTimeField(db_column='LastModifiedTime', blank=True,
                                              null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_parameters'


class Plan(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    plan_code = models.CharField(db_column='PlanCode', max_length=50)  # Field name made lowercase.
    plan_number = models.CharField(db_column='PlanNumber', max_length=50, blank=True)  # Field name made lowercase.
    organizationcode = models.CharField(db_column='OrganizationCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    weigh_house_codes = models.CharField(db_column='WeighHouseCodes', max_length=200,
                                         blank=True)  # Field name made lowercase.
    supplier_code = models.CharField(db_column='SupplierCode', max_length=50, blank=True)  # Field name made lowercase.
    supplier_name = models.CharField(db_column='SupplierName', max_length=100, blank=True)  # Field name made lowercase.
    recipient_code = models.CharField(db_column='RecipientCode', max_length=50,
                                      blank=True)  # Field name made lowercase.
    recipient_name = models.CharField(db_column='RecipientName', max_length=100,
                                      blank=True)  # Field name made lowercase.
    material_code = models.CharField(db_column='MaterialCode', max_length=50, blank=True)  # Field name made lowercase.
    material_name = models.CharField(db_column='MaterialName', max_length=100, blank=True)  # Field name made lowercase.
    weigh_type = models.CharField(db_column='WeighType', max_length=50, blank=True)  # Field name made lowercase.
    measure_unit = models.CharField(db_column='MeasureUnit', max_length=50, blank=True)  # Field name made lowercase.
    plan_begin_time = models.DateTimeField(db_column='PlanBeginTime', blank=True,
                                           null=True)  # Field name made lowercase.
    plan_end_time = models.DateTimeField(db_column='PlanEndTime', blank=True, null=True)  # Field name made lowercase.
    plan_execute_time = models.DateTimeField(db_column='PlanExecuteTime', blank=True,
                                             null=True)  # Field name made lowercase.
    plan_amount = models.FloatField(db_column='PlanAmount', blank=True, null=True)  # Field name made lowercase.
    plan_execute_amount = models.FloatField(db_column='PlanExecuteAmount', blank=True,
                                            null=True)  # Field name made lowercase.
    is_total_control = models.NullBooleanField(db_column='IsTotalControl')  # Field name made lowercase.
    total_float_range = models.FloatField(db_column='TotalFloatRange', blank=True,
                                          null=True)  # Field name made lowercase.
    total_float_per_range = models.FloatField(db_column='TotalFloatPerRange', blank=True,
                                              null=True)  # Field name made lowercase.
    is_car_control = models.NullBooleanField(db_column='IsCarControl')  # Field name made lowercase.
    is_from_erp = models.NullBooleanField(db_column='IsFromErp')  # Field name made lowercase.
    status = models.NullBooleanField(db_column='Status')  # Field name made lowercase.
    enable_modify = models.NullBooleanField(db_column='EnableModify')  # Field name made lowercase.
    enable_delete = models.NullBooleanField(db_column='EnableDelete')  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    upload_bit = models.IntegerField(db_column='UploadBit', blank=True, null=True)  # Field name made lowercase.
    upload_time = models.DateTimeField(db_column='UploadTime', blank=True, null=True)  # Field name made lowercase.
    create_user_code = models.CharField(db_column='CreateUserCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CreateUserName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    last_modified_user_code = models.CharField(db_column='LastModifiedUserCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    last_modified_username = models.CharField(db_column='LastModifiedUserName', max_length=50,
                                              blank=True)  # Field name made lowercase.
    last_modified_time = models.DateTimeField(db_column='LastModifiedTime', blank=True,
                                              null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.
    attribute1 = models.CharField(db_column='Attribute1', max_length=100, blank=True)  # Field name made lowercase.
    attribute2 = models.CharField(db_column='Attribute2', max_length=100, blank=True)  # Field name made lowercase.
    attribute3 = models.CharField(db_column='Attribute3', max_length=100, blank=True)  # Field name made lowercase.
    attribute4 = models.CharField(db_column='Attribute4', max_length=100, blank=True)  # Field name made lowercase.
    attribute5 = models.CharField(db_column='Attribute5', max_length=100, blank=True)  # Field name made lowercase.
    attribute6 = models.CharField(db_column='Attribute6', max_length=100, blank=True)  # Field name made lowercase.
    attribute7 = models.CharField(db_column='Attribute7', max_length=2000, blank=True)  # Field name made lowercase.
    attribute8 = models.CharField(db_column='Attribute8', max_length=2000, blank=True)  # Field name made lowercase.
    attribute9 = models.CharField(db_column='Attribute9', max_length=500, blank=True)  # Field name made lowercase.
    attribute10 = models.CharField(db_column='Attribute10', max_length=100, blank=True)  # Field name made lowercase.
    attribute11 = models.CharField(db_column='Attribute11', max_length=100, blank=True)  # Field name made lowercase.
    attribute12 = models.CharField(db_column='Attribute12', max_length=100, blank=True)  # Field name made lowercase.
    attribute13 = models.CharField(db_column='Attribute13', max_length=100, blank=True)  # Field name made lowercase.
    attribute14 = models.CharField(db_column='Attribute14', max_length=100, blank=True)  # Field name made lowercase.
    attribute15 = models.CharField(db_column='Attribute15', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_plan'


class Remark(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    remark_code = models.CharField(db_column='RemarkCode', max_length=50)  # Field name made lowercase.
    remark_number = models.CharField(db_column='RemarklNumber', max_length=50, blank=True)  # Field name made lowercase.
    remark_name = models.CharField(db_column='RemarkName', max_length=500, blank=True)  # Field name made lowercase.
    weigh_house_codes = models.CharField(db_column='WeighHouseCodes', max_length=200,
                                         blank=True)  # Field name made lowercase.
    status = models.NullBooleanField(db_column='Status')  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    upload_bit = models.IntegerField(db_column='UploadBit', blank=True, null=True)  # Field name made lowercase.
    upload_time = models.DateTimeField(db_column='UploadTime', blank=True, null=True)  # Field name made lowercase.
    create_user_code = models.CharField(db_column='CreateUserCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CreateUserName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    last_modified_user_code = models.CharField(db_column='LastModifiedUserCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    last_modified_username = models.CharField(db_column='LastModifiedUserName', max_length=50,
                                              blank=True)  # Field name made lowercase.
    last_modified_time = models.DateTimeField(db_column='LastModifiedTime', blank=True,
                                              null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.
    attribute1 = models.CharField(db_column='Attribute1', max_length=100, blank=True)  # Field name made lowercase.
    attribute2 = models.CharField(db_column='Attribute2', max_length=100, blank=True)  # Field name made lowercase.
    attribute3 = models.CharField(db_column='Attribute3', max_length=100, blank=True)  # Field name made lowercase.
    attribute4 = models.CharField(db_column='Attribute4', max_length=100, blank=True)  # Field name made lowercase.
    attribute5 = models.CharField(db_column='Attribute5', max_length=100, blank=True)  # Field name made lowercase.
    attribute6 = models.CharField(db_column='Attribute6', max_length=100, blank=True)  # Field name made lowercase.
    attribute7 = models.CharField(db_column='Attribute7', max_length=100, blank=True)  # Field name made lowercase.
    attribute8 = models.CharField(db_column='Attribute8', max_length=100, blank=True)  # Field name made lowercase.
    attribute9 = models.CharField(db_column='Attribute9', max_length=100, blank=True)  # Field name made lowercase.
    attribute10 = models.CharField(db_column='Attribute10', max_length=100, blank=True)  # Field name made lowercase.
    attribute11 = models.CharField(db_column='Attribute11', max_length=100, blank=True)  # Field name made lowercase.
    attribute12 = models.CharField(db_column='Attribute12', max_length=100, blank=True)  # Field name made lowercase.
    attribute13 = models.CharField(db_column='Attribute13', max_length=100, blank=True)  # Field name made lowercase.
    attribute14 = models.CharField(db_column='Attribute14', max_length=100, blank=True)  # Field name made lowercase.
    attribute15 = models.CharField(db_column='Attribute15', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_remark'


class Shift(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    shift_code = models.CharField(db_column='ShiftCode', max_length=50)  # Field name made lowercase.
    shift_name = models.CharField(db_column='ShiftName', max_length=50, blank=True)  # Field name made lowercase.
    start_time = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    end_time = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    status = models.NullBooleanField(db_column='Status')  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    upload_bit = models.IntegerField(db_column='UploadBit', blank=True, null=True)  # Field name made lowercase.
    upload_time = models.DateTimeField(db_column='UploadTime', blank=True, null=True)  # Field name made lowercase.
    weigh_house_codes = models.CharField(db_column='WeighHouseCodes', max_length=200,
                                         blank=True)  # Field name made lowercase.
    create_user_code = models.CharField(db_column='CreateUserCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CreateUserName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    last_modified_user_code = models.CharField(db_column='LastModifiedUserCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    last_modified_username = models.CharField(db_column='LastModifiedUserName', max_length=50,
                                              blank=True)  # Field name made lowercase.
    last_modified_time = models.DateTimeField(db_column='LastModifiedTime', blank=True,
                                              null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_shift'


class Specification(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    specification_code = models.CharField(db_column='SpecificationCode', max_length=50,
                                          blank=True)  # Field name made lowercase.
    specification_number = models.CharField(db_column='SpecificationNumber', max_length=50,
                                            blank=True)  # Field name made lowercase.
    specification_name = models.CharField(db_column='SpecificationName', max_length=50,
                                          blank=True)  # Field name made lowercase.
    length = models.FloatField(db_column='Length', blank=True, null=True)  # Field name made lowercase.
    width = models.FloatField(db_column='Width', blank=True, null=True)  # Field name made lowercase.
    height = models.FloatField(db_column='Height', blank=True, null=True)  # Field name made lowercase.
    length_unit = models.CharField(db_column='LengthUnit', max_length=50, blank=True)  # Field name made lowercase.
    width_unit = models.CharField(db_column='WidthUnit', max_length=50, blank=True)  # Field name made lowercase.
    height_unit = models.CharField(db_column='HeightUnit', max_length=50, blank=True)  # Field name made lowercase.
    status = models.NullBooleanField(db_column='Status')  # Field name made lowercase.
    weigh_house_codes = models.CharField(db_column='WeighHouseCodes', max_length=200,
                                         blank=True)  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    upload_bit = models.IntegerField(db_column='UploadBit', blank=True, null=True)  # Field name made lowercase.
    upload_time = models.DateTimeField(db_column='UploadTime', blank=True, null=True)  # Field name made lowercase.
    create_user_code = models.CharField(db_column='CreateUserCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CreateUserName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    last_modified_user_code = models.CharField(db_column='LastModifiedUserCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    last_modified_username = models.CharField(db_column='LastModifiedUserName', max_length=50,
                                              blank=True)  # Field name made lowercase.
    last_modified_time = models.DateTimeField(db_column='LastModifiedTime', blank=True,
                                              null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.
    attribute1 = models.CharField(db_column='Attribute1', max_length=100, blank=True)  # Field name made lowercase.
    attribute2 = models.CharField(db_column='Attribute2', max_length=100, blank=True)  # Field name made lowercase.
    attribute3 = models.CharField(db_column='Attribute3', max_length=100, blank=True)  # Field name made lowercase.
    attribute4 = models.CharField(db_column='Attribute4', max_length=100, blank=True)  # Field name made lowercase.
    attribute5 = models.CharField(db_column='Attribute5', max_length=100, blank=True)  # Field name made lowercase.
    attribute6 = models.CharField(db_column='Attribute6', max_length=100, blank=True)  # Field name made lowercase.
    attribute7 = models.CharField(db_column='Attribute7', max_length=100, blank=True)  # Field name made lowercase.
    attribute8 = models.CharField(db_column='Attribute8', max_length=100, blank=True)  # Field name made lowercase.
    attribute9 = models.CharField(db_column='Attribute9', max_length=100, blank=True)  # Field name made lowercase.
    attribute10 = models.CharField(db_column='Attribute10', max_length=100, blank=True)  # Field name made lowercase.
    attribute11 = models.CharField(db_column='Attribute11', max_length=100, blank=True)  # Field name made lowercase.
    attribute12 = models.CharField(db_column='Attribute12', max_length=100, blank=True)  # Field name made lowercase.
    attribute13 = models.CharField(db_column='Attribute13', max_length=100, blank=True)  # Field name made lowercase.
    attribute14 = models.CharField(db_column='Attribute14', max_length=100, blank=True)  # Field name made lowercase.
    attribute15 = models.CharField(db_column='Attribute15', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_specification'


class SqlStatements(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    table_name = models.CharField(db_column='TableName', max_length=128, blank=True)  # Field name made lowercase.
    table_description = models.CharField(db_column='TableDescription', max_length=50,
                                         blank=True)  # Field name made lowercase.
    sqlcode = models.CharField(db_column='SqlCode', max_length=50, blank=True)  # Field name made lowercase.
    sql_statement = models.CharField(db_column='SqlStatement', max_length=1000,
                                     blank=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True)  # Field name made lowercase.
    status = models.NullBooleanField(db_column='Status')  # Field name made lowercase.
    weigh_house_codes = models.CharField(db_column='WeighHouseCodes', max_length=200,
                                         blank=True)  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    upload_bit = models.IntegerField(db_column='UploadBit', blank=True, null=True)  # Field name made lowercase.
    upload_time = models.DateTimeField(db_column='UploadTime', blank=True, null=True)  # Field name made lowercase.
    create_user_code = models.CharField(db_column='CreateUserCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CreateUserName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    last_modified_user_code = models.CharField(db_column='LastModifiedUserCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    last_modified_username = models.CharField(db_column='LastModifiedUserName', max_length=50,
                                              blank=True)  # Field name made lowercase.
    last_modified_time = models.DateTimeField(db_column='LastModifiedTime', blank=True,
                                              null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_sql_statements'


class Unit(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    unit_name = models.CharField(db_column='UnitName', max_length=50, blank=True)  # Field name made lowercase.
    unit_symbol = models.CharField(db_column='UnitSymbol', max_length=50, blank=True)  # Field name made lowercase.
    status = models.NullBooleanField(db_column='Status')  # Field name made lowercase.
    weigh_house_codes = models.CharField(db_column='WeighHouseCodes', max_length=200,
                                         blank=True)  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    upload_bit = models.IntegerField(db_column='UploadBit', blank=True, null=True)  # Field name made lowercase.
    upload_time = models.DateTimeField(db_column='UploadTime', blank=True, null=True)  # Field name made lowercase.
    create_user_code = models.CharField(db_column='CreateUserCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CreateUserName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    last_modified_user_code = models.CharField(db_column='LastModifyUserCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    last_modified_username = models.CharField(db_column='LastModifyUserName', max_length=50,
                                              blank=True)  # Field name made lowercase.
    last_modified_time = models.DateTimeField(db_column='LastModifyTime', blank=True,
                                              null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.
    attribute1 = models.CharField(db_column='Attribute1', max_length=100, blank=True)  # Field name made lowercase.
    attribute2 = models.CharField(db_column='Attribute2', max_length=100, blank=True)  # Field name made lowercase.
    attribute3 = models.CharField(db_column='Attribute3', max_length=100, blank=True)  # Field name made lowercase.
    attribute4 = models.CharField(db_column='Attribute4', max_length=100, blank=True)  # Field name made lowercase.
    attribute5 = models.CharField(db_column='Attribute5', max_length=100, blank=True)  # Field name made lowercase.
    attribute6 = models.CharField(db_column='Attribute6', max_length=100, blank=True)  # Field name made lowercase.
    attribute7 = models.CharField(db_column='Attribute7', max_length=100, blank=True)  # Field name made lowercase.
    attribute8 = models.CharField(db_column='Attribute8', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_unit'


class UserGroup(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_group_code = models.CharField(db_column='UserGroupCode', max_length=50,
                                       blank=True)  # Field name made lowercase.
    user_group_name = models.CharField(db_column='UserGroupName', max_length=50,
                                       blank=True)  # Field name made lowercase.
    weigh_house_codes = models.CharField(db_column='WeighHouseCodes', max_length=200,
                                         blank=True)  # Field name made lowercase.
    status = models.NullBooleanField(db_column='Status')  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    upload_bit = models.IntegerField(db_column='UploadBit', blank=True, null=True)  # Field name made lowercase.
    upload_time = models.DateTimeField(db_column='UploadTime', blank=True, null=True)  # Field name made lowercase.
    create_user_code = models.CharField(db_column='CreateUserCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CreateUserName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    last_modified_user_code = models.CharField(db_column='LastModifiedUserCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    last_modified_username = models.CharField(db_column='LastModifiedUserName', max_length=50,
                                              blank=True)  # Field name made lowercase.
    last_modified_time = models.DateTimeField(db_column='LastModifiedTime', blank=True,
                                              null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.
    attribute1 = models.CharField(db_column='Attribute1', max_length=100, blank=True)  # Field name made lowercase.
    attribute2 = models.CharField(db_column='Attribute2', max_length=100, blank=True)  # Field name made lowercase.
    attribute3 = models.CharField(db_column='Attribute3', max_length=100, blank=True)  # Field name made lowercase.
    attribute4 = models.CharField(db_column='Attribute4', max_length=100, blank=True)  # Field name made lowercase.
    attribute5 = models.CharField(db_column='Attribute5', max_length=100, blank=True)  # Field name made lowercase.
    attribute6 = models.CharField(db_column='Attribute6', max_length=100, blank=True)  # Field name made lowercase.
    attribute7 = models.CharField(db_column='Attribute7', max_length=100, blank=True)  # Field name made lowercase.
    attribute8 = models.CharField(db_column='Attribute8', max_length=100, blank=True)  # Field name made lowercase.
    attribute9 = models.CharField(db_column='Attribute9', max_length=100, blank=True)  # Field name made lowercase.
    attribute10 = models.CharField(db_column='Attribute10', max_length=100, blank=True)  # Field name made lowercase.
    attribute11 = models.CharField(db_column='Attribute11', max_length=100, blank=True)  # Field name made lowercase.
    attribute12 = models.CharField(db_column='Attribute12', max_length=100, blank=True)  # Field name made lowercase.
    attribute13 = models.CharField(db_column='Attribute13', max_length=100, blank=True)  # Field name made lowercase.
    attribute14 = models.CharField(db_column='Attribute14', max_length=100, blank=True)  # Field name made lowercase.
    attribute15 = models.CharField(db_column='Attribute15', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_usergroup'


class WeighBridgeOffice(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    weigh_house_code = models.CharField(verbose_name='磅房编码', db_column='WeighHouseCode', max_length=200)  # Field name made lowercase.
    erp_code = models.CharField(verbose_name='ERP编码', db_column='ErpCode', max_length=50, blank=True)  # Field name made lowercase.
    weigh_house_name = models.CharField(verbose_name='磅房名称', db_column='WeighHouseName', max_length=200,
                                        blank=True)  # Field name made lowercase.
    company_name = models.CharField(verbose_name='单位名称', db_column='CompanyName', max_length=100, blank=True)  # Field name made lowercase.
    manager = models.CharField(db_column='Manager', max_length=50, blank=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=100, blank=True)  # Field name made lowercase.
    interface_user_id = models.CharField(verbose_name='接口用户ID', db_column='InterfaceUserID', max_length=50,
                                         blank=True)  # Field name made lowercase.
    interface_user_name = models.CharField(verbose_name='接口用户编码', db_column='InterfaceUserName', max_length=50,
                                           blank=True)  # Field name made lowercase.
    interface_password = models.CharField(verbose_name='接口密码', db_column='InterfacePassword', max_length=100,
                                          blank=True)  # Field name made lowercase.
    config_file_name = models.CharField(db_column='ConfigFileName', max_length=100,
                                        blank=True)  # Field name made lowercase.
    config_file_path = models.CharField(db_column='ConfigFilePath', max_length=1000,
                                        blank=True)  # Field name made lowercase.
    status = models.NullBooleanField(db_column='Status')  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    upload_bit = models.IntegerField(db_column='UploadBit', blank=True, null=True)  # Field name made lowercase.
    upload_time = models.DateTimeField(db_column='UploadTime', blank=True, null=True)  # Field name made lowercase.
    create_user_code = models.CharField(db_column='CreateUserCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CreateUserName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    last_modified_user_code = models.CharField(db_column='LastModifiedUserCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    last_modified_username = models.CharField(db_column='LastModifiedUserName', max_length=50,
                                              blank=True)  # Field name made lowercase.
    last_modified_time = models.DateTimeField(db_column='LastModifiedTime', blank=True,
                                              null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.
    attribute1 = models.CharField(db_column='Attribute1', max_length=100, blank=True)  # Field name made lowercase.
    attribute2 = models.CharField(db_column='Attribute2', max_length=100, blank=True)  # Field name made lowercase.
    attribute3 = models.CharField(db_column='Attribute3', max_length=100, blank=True)  # Field name made lowercase.
    attribute4 = models.CharField(db_column='Attribute4', max_length=100, blank=True)  # Field name made lowercase.
    attribute5 = models.CharField(db_column='Attribute5', max_length=100, blank=True)  # Field name made lowercase.
    attribute6 = models.CharField(db_column='Attribute6', max_length=100, blank=True)  # Field name made lowercase.
    attribute7 = models.CharField(db_column='Attribute7', max_length=100, blank=True)  # Field name made lowercase.
    attribute8 = models.CharField(db_column='Attribute8', max_length=100, blank=True)  # Field name made lowercase.
    attribute9 = models.CharField(db_column='Attribute9', max_length=100, blank=True)  # Field name made lowercase.
    attribute10 = models.CharField(db_column='Attribute10', max_length=100, blank=True)  # Field name made lowercase.
    attribute11 = models.CharField(db_column='Attribute11', max_length=100, blank=True)  # Field name made lowercase.
    attribute12 = models.CharField(db_column='Attribute12', max_length=100, blank=True)  # Field name made lowercase.
    attribute13 = models.CharField(db_column='Attribute13', max_length=100, blank=True)  # Field name made lowercase.
    attribute14 = models.CharField(db_column='Attribute14', max_length=100, blank=True)  # Field name made lowercase.
    attribute15 = models.CharField(db_column='Attribute15', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_weighbridgeoffice'
        verbose_name = '磅房'
        verbose_name_plural = '磅房'


class WeighType(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    type_code = models.CharField(db_column='TypeCode', max_length=50, blank=True)  # Field name made lowercase.
    type_name = models.CharField(db_column='TypeName', max_length=50, blank=True)  # Field name made lowercase.
    weigh_house_codes = models.CharField(db_column='WeighHouseCodes', max_length=200,
                                         blank=True)  # Field name made lowercase.
    status = models.NullBooleanField(db_column='Status')  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    upload_bit = models.IntegerField(db_column='UploadBit', blank=True, null=True)  # Field name made lowercase.
    upload_time = models.DateTimeField(db_column='UploadTime', blank=True, null=True)  # Field name made lowercase.
    create_user_code = models.CharField(db_column='CreateUserCode', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CreateUserName', max_length=50,
                                        blank=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    last_modified_user_code = models.CharField(db_column='LastModifyUserCode', max_length=50,
                                               blank=True)  # Field name made lowercase.
    last_modified_user_name = models.CharField(db_column='LastModifyUserName', max_length=50,
                                               blank=True)  # Field name made lowercase.
    last_modified_time = models.DateTimeField(db_column='LastModifyTime', blank=True,
                                              null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True)  # Field name made lowercase.
    attribute1 = models.CharField(db_column='Attribute1', max_length=100, blank=True)  # Field name made lowercase.
    attribute2 = models.CharField(db_column='Attribute2', max_length=100, blank=True)  # Field name made lowercase.
    attribute3 = models.CharField(db_column='Attribute3', max_length=100, blank=True)  # Field name made lowercase.
    attribute4 = models.CharField(db_column='Attribute4', max_length=100, blank=True)  # Field name made lowercase.
    attribute5 = models.CharField(db_column='Attribute5', max_length=100, blank=True)  # Field name made lowercase.
    attribute6 = models.CharField(db_column='Attribute6', max_length=100, blank=True)  # Field name made lowercase.
    attribute7 = models.CharField(db_column='Attribute7', max_length=100, blank=True)  # Field name made lowercase.
    attribute8 = models.CharField(db_column='Attribute8', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_weigh_weigh_type'


class Query(models.Model):
    weigh_house_code = models.CharField(db_column='WeighHouseCode', max_length=200)  # Field name made lowercase.
    weigh_house_name = models.CharField(db_column='WeighHouseName', max_length=100,
                                        blank=True)  # Field name made lowercase.
    company_name = models.CharField(db_column='CompanyName', max_length=12)  # Field name made lowercase.
    interface_user_id = models.CharField(db_column='InterfaceUserID', max_length=50,
                                         blank=True)  # Field name made lowercase.
    interface_user_name = models.CharField(db_column='InterfaceUserName', max_length=50,
                                           blank=True)  # Field name made lowercase.
    interface_password = models.CharField(db_column='InterfacePassword', max_length=100,
                                          blank=True)  # Field name made lowercase.
    status = models.NullBooleanField(db_column='Status')  # Field name made lowercase.
    operate_bit = models.IntegerField(db_column='OperateBit', blank=True, null=True)  # Field name made lowercase.
    attribute2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '查询'

